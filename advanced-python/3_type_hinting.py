# Python is a DYNAMICALLY TYPED LANGUAGE, not a STATICALLY TYPED LANGUAGE
# This means that types are determined at runtime not compile time
# This also means that we don't generally know the return types of functions and the types of their arguments

# We can however, still indicate their types via TYPE HINTING as this enhancees code readability andd maintainability
# It may also come in handy if in the future, we need to refactor our code into a statically typed language
# Type hints are done as follows

def adding_number(num1: int, num2: int) -> str:

  result = num1 + num2
  return f"The result of adding {num1} and {num2} is: {result}"

print(adding_number(6,7))

# Note that Python doesn't enforce type hints and that at runtime they are ignored by the interpreter
# However, it is bad practice to create type hints and not use them
# Type hints can be viewed in the annotations tab

print(adding_number.__annotations__)
