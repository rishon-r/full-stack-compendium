# TESTING
# Very rearely do programmers test their programs using the output console
# it is very typical in the industry to write other programs that will test your code
# One of the major ways of testing code is through UNIT TEST
# A unit test is a program that tests a small part of your code, typically just a single function
# Typicall if a program is called your_program.py, the unit test file will be titled your_program_test.py

# Typically with testing, you aim to test the functionality of your code with a wide range of arguments
# Test for all cases, especially edge cases where your code has a higher probability of failing or breaking
# A test is said to pass if it produces the desired output/values and fail if it doesn't

# When developing good software, it is important to test code incrementally as you are building in order to ensure that buggy code doesn't affect future code
# It is also paramount to test your code thoroughly before pushing to production

# unit testing is done with the unittesting framework which we will cover in detail later on


# DEBUGGING
# Debugging refers to thte task of detecting and fixing bugs in your code
# A bug is an error or flaw in a program that causes it to behave in an unintended or unexpected way

# There are chiefly three kinds:
# 1. SYNTAX ERRORS: code that violates Python's grammar rules. The interpreter catches these before the program even runs
# 2. RUNTIME ERRORS: code that is syntactically valid but causes a crash during execution
# 3. LOGIC ERRORS: the hardest type to catch because the program runs without crashing but produces the wrong result

# You will typically debug using print() statements or some kind of debugger like the built in VS code debugger

# The STACK TRACE error is an intimidating looking error in Python, often signified by the word Traceback in the Error message
# Think of a stack trace (often called a traceback in Python) as a data-driven crime scene report for your code.
# When your Python program runs into a fatal error that it doesn't know how to handle, 
# it immediately freezes and prints a report showing exactly what went wrong,
#  which line of code caused it, and the sequence of function calls that led you there
# Python prints its stack traces chronologically (from top to bottom). This means the start of the error journey is at the top,
# and the actual final blow that crashed your program is at the very bottom
# It is usual practice to read this error from bottom to top, looking at the exact point that caused the fault and then moving upwards to see what may have caused it

# COMMON ERRORS IN PYTHON
# 1. IndexError - You tried to grab an item from a list that doesn't exist. E.g trying to grab an element from index 5 in a list that only has 3 items
# 2. KeyError - You tried to look up a dictionary key that isn't there
# 3. NameError - You used a variable or function name that hasn't been defined ye
# 4. TypeError - You tried to do an operation on incompatible data types
# 5. SyntaxError- Happens when you don't adhere to the syntax of the language

# EXCEPTIONS AND EXCEPTION HANDLING
# Exceptions in Python are errors detected during execution that interrupt the normal flow of a program
# When something goes wrong, Python raises an exception. You can catch it to handle it gracefully instead of crashing.
# A common example is ZeroDivisionError that occurs when you try dividing by zero
# Python lets us handle exceptions via try and except blocks
# E.g 
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")
# What happens in a try/except block essentially is that Python will try and execute the code under the try block
# If an exception is raised by the Python interpreter, the except block will catch the exception and instead the code under except block will be run
# this prevents ugly error messages from being printed on the console
# A more verbose example of try/except structure:
'''
try:
    # code that might raise an exception
except ExceptionType:
    # runs if ExceptionType occurs
except (TypeA, TypeB):
    # catch multiple types at once
except ExceptionType as e:
    # 'e' holds the exception object/message.  
except Exception as e:
    # Will catch exception of any type and store it in e. Useful when we want to know what exception was caused
except:
    # catches everything (avoid this)
else:
    # runs ONLY if no exception was raised (good place for code that depends on try succeeding)
finally:
    # ALWAYS runs, no matter what (optional) (good for cleanup e.g. closing files/DB connections)
'''

# Raising your own exceptions
# You can manually raise exceptions using the raise keyword
# e.g
def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b
# You can also raise a more generic exception with Exception instead of specifiying the type of error
def set_age(age):
    if age < 0:
        raise Exception("Age cannot be negative")
    return age


# NOTE: Errors are not bugs
# Bug — a mistake in your code logic written by the programmer. The code runs but behaves incorrectly.
# Error — something that goes wrong during execution, which Python detects and reports.
