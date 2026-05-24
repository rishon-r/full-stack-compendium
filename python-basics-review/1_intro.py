# INTRO

# Key benefit of Python is that it is  unlike Java/C/C++ where the write/compile/test/re-compile cycle is too slow
# Despite this, Python is a real programming language.

# Python is a HIGH LEVEL PROGRAMMING LANGUAGE
# A high level programming language is one with human readable syntax that abstracts the low level details of computer's hardware
# So, Python supports a lot of high level data types (like flexible arrays and dictionaries)

# Python supports MODULAR PROGRAMMING
# i.e it allows you to split your programs into modules in such a way that they can be reused in other programs
# It comes with a lot of built in modules that can be used for various tasks. E.g os module, random module, math module

# Python is also an INTERPRETED language.
# In a compiled language, all code is converted into executable machine code before running in a process called compiling which produces an executable.
# In an interpreted language however, the code is executed line by line
# This might help us have a reduced runtime as there is no need for compilation or linking.
# C is an example of a compiled language
# The interpreter is also a program that converts the human readable source code we write to machine code

# Another important fact about Python is that it is EXTENSIBLE which means that it is easy to add a new built in function/module if one can write C
# This is due to the fact that Python is written in C

# The print() function outputs text or values to the console.
print("Hello, world!")        # prints a string
print(42)                     # prints a number
print("x =", 42)              # prints multiple values, separated by spaces
print(f"x = {42}")            # f-string formatting
print("line1\nline2")         # \n for newlines
print("a", "b", sep="-")      # custom separator → a-b (default separator is space)
print("no newline", end="")   # custom ending (default is \n)
# Print automatically converts the data it is printing to a string before displaying it on the console
# Another key thing to remember when printing is that there exist certain characters that convey special meaning to the interpreter
# When usng these characters in a string or print statement, we need to use escape sequences \ right before them so that they can be printed
# We have used this above in \n
# E.g below for \
print("\nThis is the escape sequence character: \\")
# Strings in python can also be enclosed either in double or single quotes

# SYNTAX ERRORS: Syntax errors occur when the code we write doesn't adhere to the Python syntax
# Syntax is essentially the correct rules of grammar and structure to be followed when writing code in a programming language such that the interpreter/compiler uncerstands it