from pydantic import BaseModel, Field, ConfigDict, EmailStr
from datetime import datetime

'''
Pydantic is a data validation library that uses Python type hints. 
These type hints don’t simply exist for documentation purposes (like in regular python)
 but are actually enforced by Pydantic at run time. 
 If data sent doesn’t adhere to the types specified by the type hints, Pydantic will return an error message.
Pydantic comes installed with fastapi and we don’t have to install it separately. 
One of fastapi’s major strengths comes from how it integrates with Pydantic. 
Pydantic schemas define what data we accept from clients and what data we send back. 
This is different from the database, which defines what we store. 
This allows for a good separation of concerns. 
Pydantic also provides us with automatic generated documentation when used with fastapi which is a great bonus.
'''

# Base Model is the base class that all our Pydantic models will inherit from
# Field allows us to add constraints like minimum and maximum length
# ConfigDict is the modern Pydantic 2 way to configure models

class UserBase(BaseModel):
  
  username: str = Field(min_length=1, max_length=50)
  email: EmailStr = Field(max_length=100) # EmailStr validates whether or not this string is automatically in email format and we don't need a min length as EmailStr automatically checks if it is an empty string

class UserCreate(UserBase):
  pass

class UserResponse(UserBase):
  # In Pydantic 2, we configure models with ConfigDict
  # from_attributes=True tells Pydantic that it can read data from objects with attributes and not just dictionaries.
  # This is important when working with databases
  # Right now our data is in dictionaries and we read like this: dictname['attr']
  # But when using databases our data will be in objects and we need to read them with dot notation
  # from_attribute=True essentially allows Pydantic to read data with . notation
  model_config = ConfigDict(from_attributes=True)

  id: int
  image_file: str | None
  image_path: str # See that this is a property in our model, however from_attributes=True in the configuration allows us to read from this as well

# You can generally update resources via two HTTP Methods: PUT and PATCH
# PUT is used to make complete updates: this involves updating every field of a resource
# PATCH is used for partial updates: this involves updating only select fields of a resource
# In APIs it is generally suggested to use PATCH as we don't want our users to resend all the fields
class UserUpdate(BaseModel):

  # PATCH style implementation, see that None values are permitted for bothe the fields
  # We can simply reuse PostCreate for a PUT style update as it already requires all the fields
  
  username: str | None = Field(default=None, min_length=1, max_length=50)
  email: EmailStr | None = Field(default=None, max_length=100)
  image_file: str | None = Field(default=None, min_length=1, max_length=200)


class PostBase(BaseModel):
  '''
  This is our base model for posts used when we both create and display posts.
  Using the same base model for both tasks follows from the DRY principle (Don't Repeat Yourself)
  which is a very important principle in software development
  '''

  # Below is how fields are specified
  # Note that we have not specified default values for any of the fields below
  # This makes them mandatory
  title: str = Field(min_length=1, max_length=100)
  content: str = Field(min_length=1)

class PostCreate(PostBase):
  # Empty class with just pass makes it essentially follow the same rules as PostBase
  # This is the class we will use when creating posts
  
  user_id: int # TEMPORARY FOR TESTING

# You can generally update resources via two HTTP Methods: PUT and PATCH
# PUT is used to make complete updates: this involves updating every field of a resource
# PATCH is used for partial updates: this involves updating only select fields of a resource
# In APIs it is generally suggested to use PATCH as we don't want our users to resend all the fields
class PostUpdate(BaseModel):

  # PATCH style implementation, see that None values are permitted for bothe the fields
  # We can simply reuse PostCreate for a PUT style update as it already requires all the fields
  
  title: str | None  = Field(default=None, min_length=1, max_length=100)
  content: str | None = Field(default=None, min_length=1)

class PostResponse(PostBase):
  # This is what we will return from the api and will contain fields that the client does not provide


  model_config = ConfigDict(from_attributes=True)

  id: int
  user_id: int
  date_posted: datetime
  author: UserResponse
  