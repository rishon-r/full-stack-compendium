from fastapi import FastAPI # importing the FastAPi class that is used to create our app instance
from fastapi.responses import HTMLResponse # allows our server to return HTML rendered as a response
from fastapi import Request # Jinja 2 templates require the Request object
from fastapi.templating import Jinja2Templates # Importing Jinja2Templates
from fastapi.staticfiles import StaticFiles # Used to serve static content
from fastapi import HTTPException, status # Used to raise appropriate HTTP exceptions
from fastapi.exceptions import RequestValidationError # Used for handling validation error (e.g when unexpected type is passed)
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException # fastAPI is built on starlette
# Useful when writing exception handlers, because FastAPI's exception handler listens for Starlette's version (which catches both since FastAPI's is a subclass)

# This creates a templates object that knows to look in our templates directory to find our templates files
templates = Jinja2Templates(directory="templates") 
# JINJA 2 TEMPLATES: Templates allow us to serve HTML pages to our users while still maintaining JSON endpoints for our backend
# With jinja 2 we can pass data to templates and also implement for loops and conditionals in our template
# Templates also allow us to write our html in HTML files rather than simply writing our HTML in Python strings
# For larger projects, writing our HTML in Python strings will be almost impossible
# jinja 2 is the templating engine that fastapi uses and comes preinstalled when we install fastapi with fastapi[standard]
# NOTE ON TEMPLATE INHERITANCE: Allows us to create a oarent template with a default structure that child templates can inherit from
# Child templates then will simply modify the parts that require modification
# This is a very powerful feature of Jinja 2

# More on Request
# from fastapi import Request imports the Request class from FastAPI, which gives you direct access to the raw incoming HTTP request object
# You use it when you need low-level details about the request that aren't automatically injected by FastAPI, such as
'''
Headers — request.headers
Client IP — request.client.host
Cookies — request.cookies
Query params — request.query_params
Request body (raw) — await request.body()
Form data — await request.form()
Request method — request.method
URL — request.url
'''
# You use it by type-hinting a parameter in your route function
'''
E.g 

from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/items")
async def read_items(request: Request):
    client_ip = request.client.host
    headers = request.headers
    return {"client_ip": client_ip}
'''

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

app = FastAPI()  # Creating an instance of our app (this is our app object)
# An app object is what we add all our routes to
# FastAPI uses decorators for routes (similar to flask)

# Here, we mount all the static files onto our app
# A static file is any file that is served to the client exactly as-is, without any processing or modification by the server
# Common examples are images and CSS style sheets
# below method takes three arguments: 
# first: url path where the static files will be accessible
# second: StaticFiles instance that points to our static directory
# third: a name that we can use to reference in our templates
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", name="home") # The first argument passed here is the path corresponding to endpoint
# FastAPI also allows us to stack decorators: this means that the same output will be rendered at the path of both decorators
@app.get("/posts", name="posts") # The name argument gives a route an internal identifier that you can use to reference it elsewhere in your code — primarily with url_for
# url_for generates a URL for a named route or static file dynamically, rather than hardcoding URLs as strings
def home(request: Request): # This is the function that gets decorated by @app.get

  # Below we return the template in our home.html file using our templates object
  # The first argument is always request
  # The second is the name of the file in your dictionary
  # The third is a context dictionary consisting of key value pairs
  # Every key value pair in the context dictionary acts as a variable available to us in the jinja template
  # View the template to see jinja syntax
  return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"}) 

@app.get("/posts/{post_id}")
def post_page(request: Request, post_id: int):

  # path parameter is automatically captured and passed as a variable into our function when function takes argument of the same name
  # and when it's type is type hinted accurately
  # The type hint is important as fastapi automatically uses that to validate requests
  for post in posts:
    if post["id"]==post_id:
      title = post["title"][:50]
      return templates.TemplateResponse(request, "post.html", {"post": post, "title": title})
    
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

@app.get("/api/posts")
def get_posts():
  return posts # fastapi will automatically convert the list of dictionaries into a JSON array

# Below we illustrate how to use path parameters in fastapi
# Path parameters are a dynamic part of the url that changes based on the request made
# fastapi will automatically recognize a path parameter when it is formatted in the way below with a type hint
@app.get("/api/posts/{post_id}")
def get_post(post_id: int):

  # path parameter is automatically captured and passed as a variable into our function when function takes argument of the same name
  # and when it's type is type hinted accurately
  # The type hint is important as fastapi automatically uses that to validate requests
  for post in posts:
    if post["id"]==post_id:
      return post
    
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found") # Raising HTTP Exception with status code 404 meaning resource not found

# This is a global exception handler that catches all HTTP exceptions across the entire app
# StarletteHTTPException is the base class for all HTTP exceptions, so this catches everything
@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request: Request, exception: StarletteHTTPException):
  
  # Use the exception's detail message if it exists, otherwise fall back to a generic message
  message = (
    exception.detail
    if exception.detail
    else "An error occurred. Please check your request and try again"
  )

  # Check if the request is coming from an API route (i.e. the URL starts with "/api")
  # API routes should return JSON responses, not HTML pages
  if request.url.path.startswith("/api"):
    return JSONResponse(
      status_code=exception.status_code, # Return the original status code (e.g. 404, 403)
      content= {"detail": message} # Note: your original code has a bug here — {"detail".message} should be {"detail": message}
    )
  
  # If the request is not an API route, return an HTML error page using a Jinja2 template
  return templates.TemplateResponse(
    request,
    "error.html", # The template to render
    {
      "status_code": exception.status_code, # e.g. 404
      "title": exception.status_code, # Used as the page title
      "message": message # The error message displayed on the page
    },
    status_code=exception.status_code # Ensures the HTTP response itself carries the correct status code, not 200
  )

# This handles RequestValidationError exceptions, which are separate from HTTP exceptions
# Validation errors occur when the request data doesn't match the expected types or schema
# e.g. sending a string where an integer is expected in a path parameter
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):

   # Check if the request is coming from an API route (i.e. the URL starts with "/api")
   # API routes should return JSON responses, not HTML pages
   if request.url.path.startswith("/api"):
    return JSONResponse(
      status_code = status.HTTP_422_UNPROCESSABLE_CONTENT, # 422 means the server understood the request but couldn't process it due to invalid data
      content= {"detail": exception.errors()} # exception.errors() returns a list of validation errors describing exactly what went wrong
    )
   
   # If the request is not an API route, return an HTML error page using a Jinja2 template
   return templates.TemplateResponse(
     request,
     "error.html", # The template to render
     {
       "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
       "title": status.HTTP_422_UNPROCESSABLE_ENTITY, # Used as the page title
       "message": "Invalid request. Please check your input and try again" # Generic message for the user since validation error details are not user friendly
     },
     status_code = status.HTTP_422_UNPROCESSABLE_CONTENT # Ensures the HTTP response itself carries the correct status code, not 200
   )