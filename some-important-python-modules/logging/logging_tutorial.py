# As an amateur programmer, one will typically use print statements for debugging and in order to print out errors that have occurred in code
# Although this is not a bad method for small programs, as your projects get larger you will typically want to use some kind of persistent log
# The word PERSISTENT is important in computer science and refers to data that continues to exist after the process that create s it terminates

# We can write logs in python using the logging module. First, we will have to import it
import logging

# First we need to configure our logger
# The below command can only be run one time
# You can read more about formatting in the Python documentation section covering the logging module, under the basicConfig function
logging.basicConfig(level=logging.INFO, filename="logs.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")
# When you set level in basicConfig(), it sets the minimum severity threshold for the root logger — any message below that level is silently ignored
# The root logger is the top-level logger that sits at the root of the logger hierarchy. Every logger you create is a descendant of it

# There are five levels of logging, listed below in order of least to most important
logging.debug("debug") # Won't be printed to log
logging.info("info")
# Only after this, for warning, error and critical will you get output (by output I mean log to your console)
logging.warning("warning")
logging.error("error")
logging.critical("critical")

# logging a variable
x = 67
logging.info(f"The value of x is {x}")

# logging a stack trace

try:
  1/0
except:
  logging.error("ZeroDivisionError", exc_info=True) # Passing exc_info=True will print out information regarding that Exception
  # We will then get the excepton info (stack trace) after ZeroDivisionError

  # You can also use the built in exception function
  logging.exception("ZeroDivisionError") # Here we don't have to specify exc_info=True and will still get the stack trace