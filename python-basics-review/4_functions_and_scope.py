# FUNCTIONS

# Functions are a core part of the Python programming language
# The keyword def introduces a new function.
# The def keyword must be followed by the function name and a list of formal parameters
# The first line of the function is called the function header or the function definition
# Statements below the function header that are a part of the function are called the function body and are indented
# They start at the line following the function body
# The function body may start with a STRING LITERAL that is called the function's DOCSTRING (short for documentation string)
# It is good to get into the habit of writing docstrings as there are many tools which produce documentation automatically using docstrings
# It is also a great way to interactively browse through your code.

# What happens when a function is executed?
# When a function is executed, a new symbol table is created (In Python, a symbol table is a maping of names to objects)
# This symbol table, often called the local symbol table, stores all the variable assignments of the function
# So, when a variable is referenced in a function, the Python interpreter first looks in the local symbol table of the function
# Then the local symbol tables of  enclosing functions (Remember that functions can be nested)
# Then it looks in the global symbol table and finally in the list of built in names
# This type of searching for the variable name is known as the LEGB rule in Python
# LEGB is an acronym for Local, Enclosing, Global, Built-in
# Thus, global variables and variables of enclosing functions cannot be directly assigned a value within a function- we need to use the global statement or an alternative

# Actual parameters (arguments) passed to a function in a function call are stored in the local symbol table of the called function when it is called
# When a function calls a function or itself recursively, a new local symbol table is formed for that call
# Hence, we can say that arguments are passed using call by value which essentially means just the values of the arguments are passed and inside the function there exists a new local variable with a copy of that value
# Changes to these local variables are not reflected outside the function
# However, Python uses neither call-by-value or call-by-reference in the traditional sense
# Python uses call by value where the value is an object reference
# So the object reference is stored in the local symbol table
# (Python uses call-by-object-reference or call-by-assignment)
# This basically means that changes to mutable objects made by the function are reflected in the original whereas changes made to immutable objects made by the function are not reflected in the original.

# Functions are objects in Python
# A function definition associates the function name with the function object in current symbol table
# Another name can also be used to refer to the function object
# Then, we can access the function using the new name
# Example below:

def print_num(num):
    print(num)

p= print_num
p(100) # Will print 100

# return STATEMENT
# return statement is used in the body of a Python function in order to return a value
# Even when there is no return statement, functions in Python return a value. They return the None value
# None is basically an analogue for NULL in Python
# return statement when used without an expression as well just returns None
# Example:
def addr(a,b):
    return a+b # returns the sum of a and b
print(addr(5,7)) # Will print 12

# Methods are functions that belong to an object
# They are referred to as obj.methodname
# We will come across these more when we study classes
# A good example of a method is the list.append() method which belongs to list objects

# ARGUMENTS
# The variables specified in parentheses after the function name are called arguments
# In Python it is possible to provide a variable number of arguments to the function
# There are chiefly three ways to do this and they can be combined together

# SOME TERMINOLOGY: Variable names that are part of the function definition are called FORMAL PARAMETERS or FORMAL ARGUMENTS
# Values passed in the function call are called ACTUAL PARAMETERS or ACTUAL ARGUMENTS

# WAY 1: POSITIONAL ARGUMENTS
# These are the most basic kind of arguments and are matched by order
# Example:

def create_id(name, age, city):
    return {'NAME': name, 'AGE': age, 'CITY': city}

result= create_id("James", 24, 'Toronto')
print(result) # Will print {NAME': 'James', 'AGE': 24, 'CITY': 'Toronto'}

# WAY 2: DEFAULT ARGUMENTS. 
# Default arguments provide a way of predefining the values of the arguments in the function definition
# This way, we can pass fewer arguments than required innthe function call
# When calling the function you can pass none, some or all of the default arguments
# Newer arguments passed in place of default arguments in the function call replace the default values of these arguments (i.e the arguments passed in function call are given the priority)
# Note that all default arguments in function definition must be placed after all the positional arguments
# Example:

def make_id(name, age=18, city="Vancouver"):
    return {'NAME': name, 'AGE': age, 'CITY': city}

d1= make_id("Joe")
print(d1) # prints {NAME': 'Joe', 'AGE': 18, 'CITY': 'Vancouver'}

d2=make_id('Jane', 21, 'Victoria')
print(d2) # prints {NAME': 'Jane', 'AGE': 21, 'CITY': 'Victoria'}

# The default values are evaluated at the point of function definition in the defining scope, so that the below code will print 5.

i = 5

def f(arg=i):
    print(arg)

i = 6
f()

# However, when the default argument is a mutable object, changes to the mutable object are reflected in the function as well
# Example

l=[1,2,3]
def print_list(list=l):
    print(l)

l.append(4)
print_list() # Will print [1,2,3,4] not [1,2,3]

# WAY 3: KEYWORD ARGUMENTS
# Python functions can also be called with keyword arguments in the form of kwarg=value
# When passed in the function call, all keyword arguments must follow all positional arguments
# After all the positional arguments have been passed, the keyword arguments can be passed in any order
# Every keyword argument passed in the function call must match one of the arguments in the function definition
# No argument may receive a value more than once
# Both Positional and Default arguments can be called in this form of kwarg=value
# Example: Calling above make_id function with keyword arguments

id_1= make_id("John", city="Kelowna", age=21)
id_1= make_id(city="Calgary", age=41, name="Jack")

# VERY IMPORTANT CONCEPT: *args and **kwargs

# *args allows us to pass multiple non keyword arguments
# * is the unpacking operator and args is just a generic name, you can also pass *numbers or * with any other arbitrary name instead of args and get the same desired result.
# What happens here essentially is that all the positional arguments passed to the function get packed into a tuple called args
# Then we can iterate over args just like any other tuple
# This feature is useful whe you don't know how many arguments a particular function will receive and want a more flexible function definition
# Example:
def display(*args):
    for item in args:
        print(item)

display("Coffee", "Oranges", "Sage", "Thyme") # Will print every element in the tuple out individually

# You can also mix *args along with other positional arguments
# However, note that there can only be one *args in your function definition
# The *args must also follow every other positional parameter previously mentioned
# Any keyword arguments must also be mentioned after *args
# Example:

def display_pets(name, *pets):
    print(f"My name is {name} and my pets' names are:")
    for petname in pets:
        print(petname)

display_pets("Kevin", "Snowy", "Caesar", "Airbud")

# Now, **kwargs works in a manner similar to *args
# **kwargs is used when one does not know the number of keyword arguments that need to be passed to the function
# ** is the double asterisk unpacking operator and similar to args, kwargs is just an arbitrary name
# Here, all keyword arguments passed to the function are stored in a dictionary called kwargs
# Then, we can iterate over the key valeu pairs in kwargs similar to how one does for any dictionaty
# Keys of the dictionary are names of the keyword arguments and values are the respective values passed to those keyword argument names

# When using **kwargs alongside *args and other positional arguments, they have to be listed in a particular order in the function definition
# Positional arguments must go first, then *args will follow after which at the end **kwargs can be listed

def example(var1, var2, *args, **kwargs):
    print(f"These are my positional arguments here: {var1}, {var2}")
    print("These are all the values in the args tuple", end=':\n')
    for arg in args:
        print(arg)

    print("Now these are all my keyword arguments", end=":\n")
    for key in kwargs:
        print(f"Keyword name: {key} and Value: {kwargs[key]}")

example('Default1 baby', 'Default2 baby', "1 ", 'hello ', 7, A="in", B= "kwargs", C='now!')

# Writing readable function headers
# From above we can clearly tell that arguments in Python can be passed to functions as positional arguments or keyword arguments
# It makes sense to describe how the function takes its arguments in the function header
# For this we use the / and * symbol
# Parameters before a / must be passed positionally and not by keyword (called positional-only arguments)
# Parameters after a * can be passed only in the form of keyword arguments (called keyword-only arguments)
# We can use both / and * together to accurately specify all argument types
# Example: 
def example(pos1, pos2, /, std, *, key1, key2):
    print(pos1, pos2, std, key1, key2)
# Here, pos1 and pos2 must be passed positionally
# std can be passed positionally or as a keyword argument
# key1 and key2 must be passed as keyword arguments
# Failure to comply to these conditions results in the function call throwing a TypeError
# If neither / or * are mentioned in a function definition, arguments can be passed any which way as long as they don't violate the initial rules for calling functions with arguments

# Another use of the * operator for Unpacking Argument lists
# Sometimes a function has its parameters defined individually without args but the arguments you want to pass are in a tuple
# In this case we can use the dereference operator at the function call
# Example
def display_names(name_1, name_2, name_3):
    print(f"The three names are: {name_1}, {name_2}, {name_3}")

names= ["Jim", "Michael", "Dwight"]
display_names(*names) # We dereference here in the function call and it provides us with an accurate output

# DOCUMENTATION STRINGS
# Documentation strings refer to the triple quoted multiline comment on the first line of a function body or class body
# The first line of the documentation string should always be a short description of what the object does  (concise summary of the objects purpose)
# When writing this line, it is important to approach the task with brevity in mind
# So, we refrain from explicitly stating the objects name or any other such details that are immediately available through other quick and easy means
# The first line should start with a capital letter and end with a period
# If there is more than one line in the docstring, the second line should be a blank line, clearly separating the first line from the rest of the documentation
# The following lines should be one or more paragraphs describing the object’s calling conventions, its side effects, etc.
# Note that the Python parser does not strip indentation from multi line strings. This means tools that process documentation must strip indentation if required
# There exists a convention for doing this. Basically, the first non blank line after the first line of string determines the amount of indentation for the entire docstring
# Whitespace “equivalent” to this indentation is then stripped from the start of all lines of the string. Lines that are indented less should not occur, but if they occur all their leading whitespace should be stripped.
# Equivalence of whitespace should be tested after expansion of tabs (to 8 spaces, normally).

# FUNCTION ANNOTATIONS
# These are optional metadata about the types that the user defined function uses
# They are stored in the .__annotations__ attribute of the function as a dictionary and have no effect on any otherpart of the function
# It works as follows (taken from documentation)
# Parameter annotations are defined by a colon after the parameter name, followed by an expression evaluating to the value of the annotation. 
# Return annotations are defined by a literal ->, followed by an expression, between the parameter list and the colon denoting the end of the def statement. 
# The following example has a required argument, an optional argument, and the return value annotated:

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')