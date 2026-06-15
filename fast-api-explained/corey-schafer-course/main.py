from fastapi import FastAPI # importing the FastAPi class that is used to create our app instance
from fastapi.responses import HTMLResponse # allows our server to return HTML rendered as a response

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

@app.get("/", response_class=HTMLResponse) # The first argument passed here is the path corresponding to endpoint, second refers to response type
# FastAPI also allows us to stack decorators: this means that the same output will be rendered at the path of both decorators
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False) # This third argument will prevent the following route from appearing in documentation
# This is primarily due to the fact that SwaggerUI docs are typically meant for API testing whcih in convention is supposed to only return JSON data
# returning HTML data there isn't very productive
def home(): # This is the function that gets decorated by @app.get
  return f"<h1> {posts[0]['title']}</h1>" # Will render a HTML page at this route

@app.get("/api/posts")
def get_posts():
  return posts # fastapi will automatically convert the list of dictionaries into a JSON array