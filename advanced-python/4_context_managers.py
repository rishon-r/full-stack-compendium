# CONTEXT MANAGERS (very useful)

# DOING THE TASK WITHOUT A CONTEXT MANAGER
file = open('context_manage_test.txt', 'r')

try:
  file.write('hello') # When this throws error due to wrong mode, the finally will handle it
except:
   pass
finally:
  file.close()

# DOING THE TASK WITH A CONTEXT MANAGER
# The context manager here has file.close() built in and will close the file even if an exception is raised
with open('context_manage_test.txt', 'w') as file:
  file.write("hello world")

# DEFINITION: A context manager is an object that manages setup and teardown of a resource automatically — guaranteeing cleanup even if an error occurs
# The with statement is what invokes a context manager.

# HOW THEY WORK UNDER THE HOOD

class ManagedResource:
    def __enter__(self):
        # setup — runs when entering the `with` block
        print("acquiring resource")
        return self  # this is what `as x` binds to

    def __exit__(self, exc_type, exc_val, exc_tb):
        # teardown — always runs, even on exception
        print("releasing resource")
        # The three other arguments contain debugging information regarding any exception if it is raise
        print(f"Exception type: {exc_type}, Exception value: {exc_val}, Exception traceback: {exc_tb}")
        return False  # False = don't suppress exceptions, True = suppress exceptions (used when we ourselves handle exceptions and don't want them to be printed to the console)
    
with ManagedResource() as r:
    print("using resource")
    raise TypeError

# Output:
# acquiring resource
# using resource
# releasing resource

# There is a lazier and better way to use context manager
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("setup")
    try:
        yield "the resource"  # everything before yield = __enter__
    finally:
        print("teardown")     # everything after yield = __exit__

with managed_resource() as r:
    print(f"using {r}")

# Output:
# setup
# using the resource
# teardown