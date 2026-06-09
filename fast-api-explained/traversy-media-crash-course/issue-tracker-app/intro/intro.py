from fastapi import FastAPI # This imports the FastAPI class from the fastapi library you installed
# FastAPI is the main class that contains all the functionality needed to build your API


# This below line of code creates an instance of the FastAPI class and assigns it to a variable called app
# This app object is essentially your entire API application
# It is the core object that: holds all routes/endpoints, handles all incoming requests, manages all responses and stores your configuration
app = FastAPI()

# List of items for testing item route and path parameters
items = [
  {"id": 1},
  {"id": 2},
  {"id": 3}
]

# @app.get — tells FastAPI this function handles GET requests (used for retrieving data)
# "/health" — this is the endpoint/route path, meaning this function will be triggered when a client sends a request to yourapi.com/health
# A decorator is a way of adding extra functionality to a function — in this case @app.get("/health") is wrapping health_check()
# so that FastAPI registers it as the handler for GET requests to /health, meaning FastAPI now knows to call that function whenever that route is hit.
@app.get("/health")
def health_chack():
  '''
  This is a regular Python function that returns a dictionary
  FastAPI automatically converts it to JSON and sends it back to the client

  So essentially, when the client hits the /health endpoint, FastAPI will run the health_check() function
  and return {"status" : "ok"} as JSON data
  '''
  return {"status": "ok"}

# We allow get requests to be made at a new endpoint /items
# This will return a JSON response with a list of items
@app.get("/items")
def get_items():
  return items

# Here, we create our first path parameter
# A path parameter is a variable part of the URL path that allows you to pass dynamic values to your endpoint
# The {} curly braces in the path tell FastAPI that this part of the URL is dynamic/variable
# Whatever value the client puts in that part of the URL gets captured and passed to your function
# FastAPI also validates it using Pydantic under the hood
@app.get("/items/{item_id}")
def get_item(item_id: int):
  for item in items:
    if item["id"] == item_id:
      return item
  return {"error": "Item not found"}


# Query parameters are another way to pass data to your endpoint, 
# but instead of being part of the URL path they are added at the end of the URL after a ?
# What they look like in a url: /users?age=25&city=Vancouver
# age=25 is a query parameter and & is used to separate multiple query parameters
# Below is how you implement a get request with query parameters
# Notice there are no curly braces in the path like path parameters
# FastAPI automatically knows these arguments passed are query parameters because they are not in the path
# Just like path parameters, FastAPI uses Pydantic validation on query parameters too — 
# so if age expects an int and the client passes age=abc, 
# FastAPI automatically returns a 422 error
@app.get("/users")
def get_users(age: int, city:str):
  return {"age": age, "city":city}

'''
You may also provide optional parameters as follows:

from typing import Optional

@app.get("/users")
def get_users(age: int, city: Optional[str] = None):
    return {"age": age, "city": city}

Here: city is optional and defaults to None if not provided
'''

# POST request
@app.post("/items")
def create_item(item: dict):
  items.append(item)
  return item
