# A decorator in Python is a function that wraps another function (or class) to modify or extend its behavior, 
# without changing the original function's code

# BASIC SYNTAX
'''
@decorator
def my_function(*args, **kwargs):
    pass
'''

'''
WHAT THE ABOVE CODE MEANS IS

my_function = decorator(my_function)

EXAMPLE OF WHAT THE DECORATOR MIGHT LOOK LIKE:

def decorator(my_function):
    def wrapper(*args, **kwargs):
        print("Before the function runs")
        result = my_function(*args, **kwargs)
        print("After the function runs")
        return result
    return wrapper
'''

# EXAMPLE FROM NEURAL NINE VIDEO

# EXAMPLE 1: MANUALLY ILLUSTRATIG HOW DECORATING WORKS

def the_decorator(sample_func):
  def wrapper():
    print("Hi we are calling the function inside here")
    sample_func()
    print("The function has been decorated")
  
  return wrapper

def hello_world():
  print("Hello World")


the_decorator(hello_world)

# EXAMPLE 2: THE PYTHONIC WAY TO DO THIS

def new_decorator(sample_func):
  def wrapper(*args, **kwargs): # Note that we add *args and **kwargs as we want a decorator to be applicable to multple functions not just one
    print("I am decorating this function")
    value = sample_func(*args, **kwargs)
    return value
  return wrapper

@new_decorator # This is how we say that a function is to be decorated by another functionin in Python. Via a type annotation
def function_to_be_decorated(person):
  return f"Hi {person} I'm your function"

new_result = function_to_be_decorated("Wembanyama")
print(new_result)

# 

