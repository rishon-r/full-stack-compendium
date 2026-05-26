# Everything we create in Python is an object
name = "Michael"
age = 17
print(type(name)) # string object i.e <class 'str'>
print(type(age)) # int object i.e <class 'int'>

# Objects are instances of classes - we use classes to make objects
# Strings and Integers as seen above are some of Python's in built classes
# Python also allows us to write our own classes and instantiate objects from them

# Objects can have methods run on them- These methods are defined in the class body
# E.g
print(name.upper()) # upper() is an instance method on the string class

# An example of class
# We use the 'class' keyword to define a class
# A class acts as a sort of blueprint for an object. It displays the attribute that the object will have and all the methods that can be run on it among other things
# Class names use PascalCase by convention (e.g. MyClass not my_class)
class Animal:
  
  def __init__(self, name, kind, zoo_keeper):
    # __init__ is a special (dunder) method that runs automatically when an object is created 
    # It is used to assign attributes (data) to the object at the point of instantiation
    # 'self' refers to the specific instance being created - it must always be the first parameter

    self.name = name # instance attribute - unique to each object
    self.kind = kind # instance attribute - unique to each object
    self.zoo_keeper = zoo_keeper

  def introduce(self):
    print(f"I am a {self.kind} and my name is {self.name}. {self.zoo_keeper.name} takes care of me <3")

class ZooKeeper:

  def __init__(self, name, phone_no):
    self.name = name
    self.phone_no = phone_no
    

# Creating an object: Instance of class ZooKeeper
# We pass values to the object when instantiating it and the __init__constructor stores them as attributes of that object
zoo_keeper_1 = ZooKeeper("Michael", "9940135771")

# Creating an object: Instance of class Animal
# We pass values to the object when instantiating it and the __init__constructor stores them as attributes of that object
animal_1 = Animal("George", "Ape", zoo_keeper_1) # Note here that other objects can be passed as arguments to the function
animal_1.introduce() # Running a method on our animal object

animal_2 = Animal("Doraemon", "Raccoon", zoo_keeper_1)
animal_2.introduce() 

