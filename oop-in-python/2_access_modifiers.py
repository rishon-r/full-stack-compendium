# Assume we are creating the data for a login system
class User:

  def __init__(self, username, email, password):
    self.username = username
    # A single underscore before the attribute name makes it a PRIVATE ATTRIBUTE
    # This means that the attribute should not be accessed and modified outside the class simply via dot notation
    # We need to define getters and setters in order to modify it 
    # getters and setters are essentially methods that allow us to set and see values of private attributes
    # More generally, in Python, an underscore _ prefacing a name is used to indicate that that entity is private for use internally within a class, module, etc.
    self._email = email
    self._password = password

  def get_email(self):
    # This method is an example of a getter
    return self._email
    
  def set_email(self, email):
    # This method is an example of a setter
    # This method does seem weird and probably won't be implemented as such in a real system due to security concerns
    # However, I have used it simply to illustrate how a setter will work so don't think about anything else for now
    self._email = email
    
# IMPORTANT NOTE: A single underscore is just a CONVENTION - Python will not throw an error
# or give any warning if you access it directly outside the class. It is simply a signal
# to other developers that this attribute is intended for internal use only.
# A double underscore __ enforces privacy more strictly
# Python will raise an AttributeError if you try to access it directly outside the class
# E.g self.__password = password
# _ variables are said to be PROTECTED and __ variables are said to be PRIVATE

# When to use PROTECTED and when to use PRIVATE?
# Generally protected are preferred over private as they provide more flexibility. 
# However, it is recommended to use private variables when absolutely necessary

user_1= User("Pythonnprogrammer", "ppgram@email.com", "asdfghjkl")
print(user_1.get_email()) # Using a getter to access protected data
user_1.set_email("new_email@email.com") # Using a setter to change protected data

# Whiile getters and setter provide an adequaate mans of accessing and setting the values of protected and private attributes,
# The Pythonic way of doing this is through something known as properties
# We essentially use something known as a decorator here
# A decorator is a function that wraps another function to add extra behaviour to it, without modifying the original function's code.
# The syntax uses @ placed above a function definition
# E.g
"""
@some_decorator
def my_function():
    pass
"""
# This is just shorthand for: my_function = some_decorator(my_function)

# An example:
def shout(func):
    def wrapper():
        result = func()
        return result.upper()  # added behaviour - make it uppercase
    return wrapper

@shout
def greet():
    return "hello"

print(greet())  # HELLO  ← the decorator modified the output without touching greet()

# To use properties in Python, we use the @property decorator
# The @property decorator lets you access a method as if it were an attribute — no parentheses needed
# E.g

class OtherUser:
   
  def __init__(self, username, email, password):
      self.username = username
      self._email = email
      self.password = password

  @property # This is the decorator for getter properties
  def email(self): # It is imperative that we name the method under property decorator the same as that of the attribute so we can access it elegantly
     return self._email
  
  @email.setter # This is how decorators for setter properties are defined
  def email(self, new_email):
     self._email=new_email
  
user_2= OtherUser("Javaprogrammer", "Jpgram@email.com", "asdfghjkl")
# Now due to the property decorator, we can do the following
print(user_2.email) # It looks like e are simply accessing it via dot notation
# But internally what I presume the @property decorator does is that it wraps the getter method in a fucntion that allows us to access 
# attributes simply via dot notation instead of having to run a getter method

# Due to the setter decorator, we can set values of private/protected attributes as follows
user_2.email= "newemail@email.com"
print(user_2.email) # Will print new email


  

