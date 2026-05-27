# DUNDER METHODS

# Dunder methods (double underscore methods) are special methods in Python
# They are also called MAGIC METHODS
# They have two underscores before and after their name e.g __init__, __str__, __len__
# Python calls them AUTOMATICALLY behind the scenes - you do not call them directly
# You have already seen __init__ which is called automatically when you create an object
# We can define dunder methods in our classes to customise the behaviour of our objects

class Dog:

  def __init__(self, name, age, weight):
    # __init__ is called automatically when we create a Dog object
    # E.g dog_1 = Dog("Rex", 5, 30) automatically calls __init__
    self.name = name
    self.age = age
    self.weight = weight

  def __str__(self):
    # __str__ is called automatically when we print an object or convert it to a string
    # Without this, print(dog_1) would give us <__main__.Dog object at 0x...>
    # With this, we can define a human readable string representation of our object
    return f"Dog: {self.name}, Age: {self.age}, Weight: {self.weight}kg"

  def __len__(self):
    # __len__ is called automatically when we call len() on an object
    # Here we define len() to return the age of the dog
    # We get to decide what len() means for our object
    return self.age

  def __add__(self, other):
    # __add__ is called automatically when we use the + operator on two objects
    # Here we define + to return the combined weight of two dogs
    # 'other' refers to the second object in the operation e.g dog_1 + dog_2
    return self.weight + other.weight

  def __eq__(self, other):
    # __eq__ is called automatically when we use the == operator on two objects
    # Here we define == to return True if two dogs have the same name and age
    return self.name == other.name and self.age == other.age

  def __gt__(self, other):
    # __gt__ is called automatically when we use the > operator
    # Here we define > to compare the weight of two dogs
    return self.weight > other.weight


dog_1 = Dog("Rex", 5, 30)
dog_2 = Dog("Buddy", 3, 25)
dog_3 = Dog("Rex", 5, 20)

print(dog_1)              # Dog: Rex, Age: 5, Weight: 30kg        ← __str__ called
print(len(dog_1))         # 5                                     ← __len__ called
print(dog_1 + dog_2)      # 55                                    ← __add__ called
print(dog_1 == dog_2)     # False