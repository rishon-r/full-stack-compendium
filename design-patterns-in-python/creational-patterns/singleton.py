# SINGLETON PATTERN

# When writing code, you will often have multiple components (think objects) that want to acces the same resource (might be an external API Object)
# Instead of creating one instance of the external resource for each of the components that wish to access it, 
# the Singleton Pattern involves creating only one instance of the external resource that is shared by all the components that wish to access it

# In other words:

# The Singleton pattern ensures that a class has ONLY ONE INSTANCE throughout the entire program
# and provides a global point of access to that instance
# This is useful when exactly one object is needed to coordinate actions across the system

# REAL WORLD EXAMPLES OF WHERE SINGLETON IS USED:
# - A database connection - you only want one connection to the database at a time
# - A logger - you only want one logger writing to a log file at a time
# - A configuration manager - you only want one set of configuration settings at a time

# The core idea is simple:
# - The class keeps track of whether an instance has already been created
# - If it has, it returns the existing instance instead of creating a new one
# - If it hasn't, it creates one and stores it for future use

# E.g

class Config: # This is the Singleton object, Config for example
  _instance= None # protected variable
  _initialized = False  # Add a flag to track initialization (this is to prevent multiple initializations)

  def __init__(self):
    if Config._initialized:
      return
    
    print("Initializing Config") # Should only print once
    self.db_url = "db_url.com"
    self.debug = True
    Config._initialized= True #  should only be set once

  def __new__(cls):
    # We override the new dunder method that automatically creates a new object when a class is instantiated
    # Such that it only creates a new object if the value of _instance is None
    # If it is none, we assign the instance to be the new __config__ object
    if cls._instance is None:
      print("Creating new Instance")
      cls._instance= super().__new__(cls) # super class is the object class
      print("Config created") # Should only print once
    return cls._instance

def main():
  s1= Config()
  s2= Config() # Trying to create two singleton objects

  print(s1 is s2) # They are the same object
  print(id(s1))
  print(id(s2)) # They exist at the same location
  # No new object is created
  # i.e singleton preserves the fact that only one object exists
        

if __name__ == '__main__':
  main()

# THE KEY DRAWBACK: The singleton pattern creates only one global instance of the object
# So, if we make changes to it locally and expect them not to be reflected in the global scope, we would be wrong
# This means we have to be very careful when interacting with the singleton object as there are a lot of components of our program which depend on it
# This drawback is called the HIDDEN GLOBAL STATE