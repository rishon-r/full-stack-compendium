# VARIABLES
# Variables are entities in which we can store data such that we can use it later in our program by simply referring to the name of the variable
# Variables in python can hold any type of data
# E.g
name = "Roger" # string type
age = 42 # integer type
weight = 225.6 # float type

# Variable names (also referred to sometimes as identifier names) have some rules regarding their naming: 
# 1. Can only contain letters, digits, and underscores _
# 2. Cannot start with a digit
# 3. Cannot be a reserved keyword (if, for, class, True, etc.)
# 4. Case-sensitive (name and Name are different variables)
# Python also typically uses snake case (underscores to in place of spaces) and lower case letters to name variables E.g this_is_a_variable
# A space before and after assignment operator in variable naming is also typically expected

# The = operator, often called the assignment operator is used to assign a value to a variable
# Python is a DYNAMICALLY TYPED LANGUAGE which means you don't have to declare types alongside variables
# A dynamically typed language is one where types are determined at runtime not in advance
# If a variable is not previously defined it will return an error
# Python is NOT STATICALLY TYPED. Statically typed languages have the types of their variables determined at compile time

# We can also change the value of a variable by reassigning it a new value
# E.g 
age = 20
print(age)
age = 35
print(age)
age = "Thirty Five" # Note here that python also allows us to change the type of the data associated with the variable, this is another advantage of dynamic typing
print(age)

# Python supports multiassignment. The below examples are all valid and kind of unique to python
a, b= 1, 2
a=b=c=3

# Python also allows us to store negative numbers in variables
a=-1

# NUMBERS
# The Python interpreter can act as a simple calculator of sorts and typing in an expression results in it producing the output
# This can be seen as an example in interactive mode
# Creating arithmetic expressions is easy in Python: we use +, /, -, * characters for arithmetic operations (they are called arithmetic operators) and the parentheses () for grouping
# There are two types of numbers that we will primarily be using: The integer numbers are of type int, and the decimal numbers ( Those with a fractional part) are type float
# Besides the standard four arithmetic operations, // operator is used for floor division (this is where you want an integer result for the division)
# % or modulo operator is used to return the remainder upon division of two numbers
# We can use the ** operator for powers E.g 2 ** 4 is a pythonic way of saying 2 raised to the power 4


# COMMENTS
# Comments in Python start with the hashtag character. They acan start at the beginning of a line like here.
print("Inline Comment!") #Or can follow a line of code like here. In this case they are called an Inline comment.
# Multiline comments also exist and are created using triple quotes
'''
This here is an example.
Of a multiline comment!!
'''
# Comments however cannot appear in the middle of a string literal as a hashtag is simply treated as a hash character in a string and not as a comment creation character
print("The # character here does not create a comment")

# VARIABLE TYPES
# Besides floats, integers, and strings, python has some other types
# Boolean values of True and False are another key type and represent numbers 1 and 0 respectively
# Lists, Tuples, Dictionaries are also other types
# The type of a varaibel can be found outbupon passing the name of the variable as an argument to the type() function
# E.g
age=32
print(type(age))
sample_bool=True
print(type(sample_bool))

# FORMATTED STRING LITERALS
# These are often called f-strings. 
# These are strings prefixed with the letter f or F
# When compared to normal string literals that are constant values, the f-strings are different.
# Their value is only known at run time.
# They have replacement fields indicated by {} that are filled in at runtime
# A replacement field is indicated by a single open curly brace { and starts with a python expression
# Example:
name= "Michael"
age= 47
result= f"My name is {name} and age is {age}"
print(result) # Will output: My name is Michael and age is 47
# Parts of the string outside the curly braces are treated like normal string literals and escape sequences are treated in the same way
# Any double curly braces in an f-string are replaced by single curly braces. Example:
result_2 = f"My name is {{name}} and age is {{age}}"
print(result_2) # Will output: My name is {name} and age is {age}
# We see that it works analogous to the \\ escape sequence

# Another important type is the None type
# This is the type used to indicate an empty variable/value
# The none type is essentially the same as a string with a value of "None" although it is usually written as None
# it is analogous to NULL in C, both generally used to indicate an absence of value
# Python
x = None
print(type(x))  # <class 'NoneType'>
x == 0          # False — None is not 0

# IDENTITY OPERATORS
# In Python, is and is not check identity — whether two variables point to the same object in memory, not just whether they have the same value
# it returns a boolean value
x = None
x is None      # True
x is not None  # False
# == checks value equality
a = [1, 2, 3] # this is called a list (more on this later)
b = [1, 2, 3]
a == b   # True — same value

# is checks identity
a is b   # False — different objects in memory

# MORE ON DYNAMIC TYPING
# Dynamic Typing allows variables in dynamically typed languages to not be bound to a particular type when they are created
# This is due to the fact that types of variables in dynamically typed languages are determined at run time and not at compile time
# The key feature of this is that it allows us to change the type of value stored in a variable later in the program after its creation
# Although this can be done, changing the type of value of a variable is generally not considered a good practice