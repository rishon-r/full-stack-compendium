from fastapi import FastAPI # importing the FastAPi class that is used to create our app instance
from fastapi.responses import HTMLResponse # allows our server to return HTML rendered as a response
from fastapi import Request # Jinja 2 templates require the Request object
from fastapi.templating import Jinja2Templates # Importing Jinja2Templates
from fastapi.staticfiles import StaticFiles # Used to serve static content
from fastapi import HTTPException, status # Used to raise appropriate HTTP exceptions, status is used to indicate appropriate status code
from fastapi import Depends # Used for Dependency Injection
from fastapi.exceptions import RequestValidationError # Used for handling validation error (e.g when unexpected type is passed)
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException # fastAPI is built on starlette
# Useful when writing exception handlers, because FastAPI's exception handler listens for Starlette's version (which catches both since FastAPI's is a subclass)
from schemas import PostCreate, PostResponse, UserResponse, UserCreate # Importing our Pydantic schemas that we will ad as response_models to our route decorators
from typing import Annotated

from sqlalchemy import select # This is for querying
from sqlalchemy.orm import Session # This is for type hints so that our orm knows what type our db_session that we are injecting is

from database import Base, engine, get_db
import models

Base.metadata.create_all(bind=engine) # Looks at all of our models that inherit from Base and creates the tables if they don't already exist
# This is an idmepotent command: means that it is safe to run multiple times and that if the data already exists it doesn't interfere with it

# This creates a templates object that knows to look in our templates directory to find our templates files
templates = Jinja2Templates(directory="templates") 
# JINJA 2 TEMPLATES: Templates allow us to serve HTML pages to our users while still maintaining JSON endpoints for our backend
# With jinja 2 we can pass data to templates and also implement for loops and conditionals in our template
# Templates also allow us to write our html in HTML files rather than simply writing our HTML in Python strings
# For larger projects, writing our HTML in Python strings will be almost impossible
# jinja 2 is the templating engine that fastapi uses and comes preinstalled when we install fastapi with fastapi[standard]
# NOTE ON TEMPLATE INHERITANCE: Allows us to create a parent template with a default structure that child templates can inherit from
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
# Same for media files
app.mount("/media", StaticFiles(directory="media"), name="media")

@app.get("/", include_in_schema= False, name="home") # The first argument passed here is the path corresponding to endpoint
# FastAPI also allows us to stack decorators: this means that the same output will be rendered at the path of both decorators
# include_in_schema=False means that these endpoints won't be available for us to test in the SwaggerUI docs
# We generally do this for files that generate frontend as we only want to test the API routes in the SwaggerUI docs
@app.get("/posts", include_in_schema=False, name="posts") # The name argument gives a route an internal identifier that you can use to reference it elsewhere in your code — primarily with url_for
# url_for generates a URL for a named route or static file dynamically, rather than hardcoding URLs as strings
def home(request: Request, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(models.Post))
    posts = result.scalars().all()
    # Below we return the template in our home.html file using our templates object
    # The first argument is always request
    # The second is the name of the file you want to render
    # The third is a context dictionary consisting of key value pairs
    # Every key value pair in the context dictionary acts as a variable available to us in the jinja template
    # View the template to see jinja syntax
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": posts, "title": "Home"},
    )


@app.get("/posts/{post_id}", include_in_schema=False)
def post_page(request: Request, post_id: int, db: Annotated[Session, Depends(get_db)]):
    # path parameter is automatically captured and passed as a variable into our function when function takes argument of the same name
    # and when it's type is type hinted accurately
    # The type hint is important as fastapi automatically uses that to validate requests
    result = db.execute(select(models.Post).where(models.Post.id == post_id))
    post = result.scalars().first()
    if post:
        title = post.title[:50]
        return templates.TemplateResponse(
            request,
            "post.html",
            {"post": post, "title": title},
        )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@app.get("/users/{user_id}/posts", include_in_schema=False, name="user_posts")
def user_posts_page(
    request: Request,
    user_id: int,
    db: Annotated[Session, Depends(get_db)],
):
    '''
    Returns all posts of a particular user
    '''
    result = db.execute(select(models.User).where(models.User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    result = db.execute(select(models.Post).where(models.Post.user_id == user_id))
    posts = result.scalars().all()
    return templates.TemplateResponse(
        request,
        "user_posts.html",
        {"posts": posts, "user": user, "title": f"{user.username}'s Posts"},
    )
    
# API ROUTES 


@app.post("/api/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED) # here status-code dictates the status code we want to return in the case of a success (by default it's 200)
def create_user(user: UserCreate, db: Annotated[Session, Depends(get_db)]):
  # What this line does: db: Annotated[Session, Depends(get_db)]
  # It manages the database lifecycle using Dependency Injection
  # db -> The local variable name you will use inside this function to talk to your database.
  # Session' -> The Python type hint. It tells your IDE that 'db' is a SQLAlchemy database session, giving you full auto-complete for database methods like 'db.add()', 'db.commit()', and 'db.query()'
  # Depends(get_db)' -> The FastAPI dependency magic. It tells FastAPI: "Before running this route, go run the 'get_db()' function we wrote earlier, open a database connection, and inject that
  # active connection right here into the 'db' variable." Once the route finishes, 'Depends' automatically closes that connection for you
  # 'Annotated[...]' -> A standard Python feature used to cleanly bundle the structural type ('Session')
  # together with FastAPI's metadata instructions ('Depends(get_db)') without breaking standard Python syntax.
  
  # Checking if user with given username exists
  result = db.execute(select(models.User).where(models.User.username == user.username))
  existing_user = result.scalars().first()

  if existing_user: # raising exception if the user already exists
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Username already exists"
    )
  
  # Checking if user with given email exists
  result = db.execute(select(models.User).where(models.User.email == user.email))
  existing_email = result.scalars().first()

  if existing_email: # raising exception if the user already exists
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Email already exists"
    )
  
  new_user= models.User(username=user.username, email=user.email) # Creating row in User database table

  db.add(new_user) # Stages insert
  db.commit() # Commiting to commit changes to database (executes insert and saves to database)
  db.refresh(new_user) # Reloads the object from the database

  return new_user # Pydantic will automatically convert this to a UserResponse

@app.get("/api/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Annotated[Session, Depends(get_db)]):

  result = db.execute(select(models.User).where(models.User.id== user_id))
  existing_user = result.scalars().first()

  if existing_user:
    return existing_user
  
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")

@app.get("/api/users/{user_id}/posts", response_model=list[PostResponse])
def get_user_posts(user_id: int, db: Annotated[Session, Depends(get_db)]):
    '''
    Returning a particular user's posts
    '''
    result = db.execute(select(models.User).where(models.User.id == user_id)) # First we query to find user with appropriate user id
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    result = db.execute(select(models.Post).where(models.Post.user_id == user_id)) # Then, we query and retrieve all posts that have the given user_id as a foreign key
    posts = result.scalars().all()
    return posts

@app.get("/api/posts", response_model=list[PostResponse]) # Adding a response model will make fastapi automatically validate the data to ensure it matches the type mentioned
def get_posts(db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(models.Post))
    posts = result.scalars().all()
    return posts # fastapi will automatically convert this into a JSON array



'''
This is how decorated functions under @app.get know the type of data that is passed in as a parameter

Is the argument name in the URL path?
                                      /              \
                                   [Yes]             [No]
                                    /                  \
                    It's a Path Parameter.       Is it a simple type (int, str) 
                                                 or a Pydantic Model?
                                                   /              \
                                            [Simple Type]     [Pydantic Model]
                                                 /                  \
                                     It's a Query Parameter.     It's the Request Body.

'''
@app.post(
    "/api/posts",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_post(post: PostCreate, db: Annotated[Session, Depends(get_db)]): # When fastapi sees a type hint, it automatically parses JSON, checks if they match up to the Pydantic schema and returns a 422 error if not
    result = db.execute(select(models.User).where(models.User.id == post.user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    new_post = models.Post(
        title=post.title,
        content=post.content,
        user_id=post.user_id,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# Below we illustrate how to use path parameters in fastapi
# Path parameters are a dynamic part of the url that changes based on the request made
# fastapi will automatically recognize a path parameter when it is formatted in the way below with a type hint
@app.get("/api/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Annotated[Session, Depends(get_db)]):
    
    # path parameter is automatically captured and passed as a variable into our function when function takes argument of the same name
    # and when it's type is type hinted accurately
    # The type hint is important as fastapi automatically uses that to validate requests
    result = db.execute(select(models.Post).where(models.Post.id == post_id))
    post = result.scalars().first()
    if post:
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
      status_code = status.HTTP_422_UNPROCESSABLE_ENTITY, # 422 means the server understood the request but couldn't process it due to invalid data
      content= {"detail": exception.errors()} # exception.errors() returns a list of validation errors describing exactly what went wrong
    )
   
   # If the request is not an API route, return an HTML error page using a Jinja2 template
   return templates.TemplateResponse(
     request,
     "error.html", # The template to render
     {
       "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
       "title": status.HTTP_422_UNPROCESSABLE_ENTITY, # Used as the page title
       "message": "Invalid request. Please check your input and try again" # Generic message for the user since validation error details are not user friendly
     },
     status_code = status.HTTP_422_UNPROCESSABLE_ENTITY # Ensures the HTTP response itself carries the correct status code, not 200
   )