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