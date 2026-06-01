# LAMBDA FUNCTIONS

# ANONYMOUS FUNCTIONS are functions without a name
# lambda is the keyword we use to create anonymous functions in Python

multiply = lambda x,y: x * y
print(multiply(5, 6))

# The powerful part of lambdas is that they can be passed as arguments to functions
# This is due to the fact that functions are first class in Python
# Which means that functions can be assigned to variables and passed around as arguments to other functions in a manner similar to any other object in Python

# E.g a function that runs a function 10 times

def run_10_times(fun):
  for i in range(10):
    fun()

run_10_times(lambda: print("hello"))

# lambdas are further used in map and filter, which we will see in the next lesson