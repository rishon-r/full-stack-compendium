from fastapi import FastAPI # importing the FastAPi class that is used to create our app instance
from fastapi import Request # Jinja 2 templates require the Request object
from fastapi.templating import Jinja2Templates # Importing Jinja2Templates
from fastapi.staticfiles import StaticFiles # Used to serve static content
from fastapi import HTTPException, status # Used to raise appropriate HTTP exceptions, status is used to indicate appropriate status code
from fastapi import Depends # Used for Dependency Injection
from fastapi.exceptions import RequestValidationError # Used for handling validation error (e.g when unexpected type is passed)
from starlette.exceptions import HTTPException as StarletteHTTPException # fastAPI is built on starlette
# Useful when writing exception handlers, because FastAPI's exception handler listens for Starlette's version (which catches both since FastAPI's is a subclass)
from typing import Annotated

from sqlalchemy import select # This is for querying
from sqlalchemy.ext.asyncio import AsyncSession # This is for type hints so that our orm knows what type our db session that we are injecting is

from database import Base, engine, get_db
import models

from contextlib import asynccontextmanager
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler
from sqlalchemy.orm import selectinload

# IMPORTING ROUTERS
from routers import users, posts

# Below function defines what happens when a FastAPI app starts up and shuts down
# Everything before yield runs as startup, everything after yield runs as shutdown
# The python mechanism that makes this work: generator based context manager
# A context manager is a python object with two hooks: "do this when entering" and "do this when exiting"
# Python typically wants you to implement two methods: __enter__ and __exit__ for this to happen
# However, importing asynccontextmanageer from contextlib provides us a shortcut to do this with the below @aynccontextmanager decorator
# It allows us to write a Python context manager as a single function with a yield instead of an object with two methods
# the code before yield acts as enter behaviour and code after yield acts as exit behaviour
# The _app: FastAPI parameter is the app instance, passed in by FastAPI (prefixed with _ to signal "received but unused"
@asynccontextmanager # Turns the below into an async context manager
async def lifespan(_app: FastAPI):
    # Startup: all the code before the yield runs before startup
    # engine below is the SQLAlchemy engine, this is the object that knows how to talk to your database
    # engine.begin() opens a connetion and begins a transaction, autocomitting if the block exits cleanly
    # It's itself an async context manager, so it needs async with
    async with engine.begin() as conn: # engine.begin() is used to create an async connection
        await conn.run_sync(Base.metadata.create_all) # run_sync allows us to run the synchronous create_all method that creates all our tables
        # Base.metadata.create_all is a synchronous SQLAlchemy command that inspects all your models and creates tables if they don't already run clearly
        # It is also idempotent: it can be run multiple times safely
        # The problem with the above code is that Base.metadat.create_all is a synchronous command
        # conn.run_sync acts as a bridge and under the hood runs the synchronous command asynchronouslyt
        
    yield # This is where our application actually begins running
    # Shutdown: Here, we dispose of the engine properly
    # It releases all open database connections so that the app exits cleanly
    await engine.dispose()

# ASYNC WITH vs REGULAR WITH
# A regular with calls synchronous methods: __enter__() and __exit__(). 
# These run to completion immediately, blocking whatever thread they're on — there's no way to "pause" them
# An async with calls asynchronous methods: __aenter__() and __aexit__(). 
# These are coroutines — they can await other things inside them,
# and pause/yield control back to the event loop while waiting

# await EXPLAINED
# await pauses execution of the current coroutine at that point, without blocking the thread.
# It hands control back to the event loop, saying
# "I'm waiting on this operation (network, disk, timer); go run something else until it's ready." 
# The event loop then schedules other pending tasks. 
# Once the awaited operation completes, the event loop resumes the coroutine exactly where it left off, 
# with the result of that operation as the expression's value. So await is really a checkpoint:
# it converts blocking-style waiting into cooperative scheduling,
# letting one thread juggle many concurrent operations efficiently, while still reading like ordinary, 
# linear, top-to-bottom code.


app = FastAPI(lifespan=lifespan)  # Creating an instance of our app (this is our app object)
# An app object is what we add all our routes to
# FastAPI uses decorators for routes (similar to flask)
# lifespan refers to the asynccontext manager we use for startup and teardown that is defined above

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

# INCLUDING ROUTERS
# prefix parameter adds given string as prefix to URLs of all routes in the router
# tags here is purely about documentation/organization — it has zero effect on routing, URLs, or request handling
# In that generated documentation, every endpoint can be grouped under one or more labeled sections. 
# tags=["users"] tells FastAPI: "every route inside users.router should be filed under the 'users' group in the docs
app.include_router(posts.router, prefix="/api/posts", tags=["posts"])
app.include_router(users.router, prefix="/api/users", tags=["users"])

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

'''
SYNCHRONOUS vs. ASYNCHRONOUS FastAPI

In Synchronous SQLAlchemy, lazy loading just works.
E.g In synchronous SQLAlchemy, if you have post object and want to access its author, you can do so with post.author
and SQLAlchemy will automatically run a query to obtain the author of that post. This is a relationship and our templates
can also access posts.author.username. This works and is known as LAZY LOADING

In Async SQLAlchemy however, Lazy loading is not supported. If you try to access post.author without loading it,
you get an error message. This happens because lazy loading requires running a synchronous query in an asynchronous context,
which is not allowed. The solution is eager loading with selectinload that we have imported from sqlalchemy.orm

So in short, any part that has lazy loading of relationshps must be replaced with eagerloading via selectinload


'''


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
async def home(request: Request, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.Post)
        .options(selectinload(models.Post.author))
        .order_by(models.Post.date_posted.desc()), # Eager loading for an async function
        # Now, when we iterate through posts in our templates and access post.author, it is going to work
        # As we already loaded in that data via eager loading above

      )
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
async def post_page(request: Request, post_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    # path parameter is automatically captured and passed as a variable into our function when function takes argument of the same name
    # and when it's type is type hinted accurately
    # The type hint is important as fastapi automatically uses that to validate requests
    result = await db.execute(
        select(models.Post)
        .options(selectinload(models.Post.author))
        .where(models.Post.id == post_id)
        )
        
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
async def user_posts_page(
    request: Request,
    user_id: int,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    '''
    Returns all posts of a particular user
    '''
    result = await db.execute(
        select(models.User).where(models.User.id == user_id) 
        # This does not need eager loading with selectinload
        # This is because none of our templates are using posts.author
        )
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    result = await db.execute(
        select(models.Post)
        .options(selectinload(models.Post.author))
        .where(models.Post.user_id == user_id)
        .order_by(models.Post.date_posted.desc())
        )
    posts = result.scalars().all()
    return templates.TemplateResponse(
        request,
        "user_posts.html",
        {"posts": posts, "user": user, "title": f"{user.username}'s Posts"},
    )

# LOG IN AND REGISTER ROUTES
@app.get("/login", include_in_schema=False)
async def login_page(request: Request):
    return templates.TemplateResponse(
        request,
        "login.html",
        {"title": "Login"},
    )


@app.get("/register", include_in_schema=False)
async def register_page(request: Request):
    return templates.TemplateResponse(
        request,
        "register.html",
        {"title": "Register"},
    )

# ACCOUNT PAGE FOR USER
@app.get("/account", include_in_schema=False)
async def account_page(request: Request):
    return templates.TemplateResponse(
        request,
        "account.html",
        {"title": "Account"},
    )



# This is a global exception handler that catches all HTTP exceptions across the entire app
# StarletteHTTPException is the base class for all HTTP exceptions, so this catches everything
@app.exception_handler(StarletteHTTPException)
async def general_http_exception_handler(request: Request, exception: StarletteHTTPException):


  # Check if the request is coming from an API route (i.e. the URL starts with "/api")
  # API routes should return JSON responses, not HTML pages
  if request.url.path.startswith("/api"):
    return await http_exception_handler(request, exception)
  
  # Use the exception's detail message if it exists, otherwise fall back to a generic message
  message = (
    exception.detail
    if exception.detail
    else "An error occurred. Please check your request and try again"
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
async def validation_exception_handler(request: Request, exception: RequestValidationError):

   # Check if the request is coming from an API route (i.e. the URL starts with "/api")
   # API routes should return JSON responses, not HTML pages
   if request.url.path.startswith("/api"):
    return await request_validation_exception_handler(request, exception)
   
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