# INHERITANCE

# INHERITANCE is the third fundamental OOP principle
# Inheritance involves creating classes based on preexisting classes
# These pre-existing class' attributes and methods are readily available for use in the newly created class
# The preexisting class is called a PARENT CLASS and the new class created based on the pre existing class is called a CHILD CLASS
# The child class is said to inherit the properties and methods of the parent class
# However, a child class may also override methods and attributes of the parent class
# A child class may also have methods and attributes of its own that aren't described in the parent class

# The below example uses the parent class of animal and child classes of dog and cat
# While dog and cat are animals and have a lot of the same properties animals do, they also have their own special features

# E.g

class Animal:

  def __init__(self, name, weight, age):
    self.name = name
    self.age = age
    self.weight = weight

  def greet(self): 
    print(f"My name is {self.name}")


class Dog(Animal): # This is how we make a child class inherit a parent class
  def __init__(self, name, weight, age, species): # We can store more attributes here than in the parent __init__
    super().__init__(name,weight,age) # super() refers to the parent class. Parent classes are also called super classes and child classes are also called subclasses
    self.species = species

  def bark(self):
    print("Woof Woof")


class Cat(Animal): # This is how we make a child class inherit a parent class
  def __init__(self, name, weight, age, color): # We can store more attributes here than in the parent __init__
    super().__init__(name,weight,age) # super() refers to the parent class. Parent classes are also called super classes and child classes are also called subclasses
    self.color = color

  def meow(self):
    print("Meow Meow")

dog_1 = Dog("Rex", 30, 5, "Labrador")
dog_1.greet()   # inherited from Animal - no need to redefine it
dog_1.bark()    # defined in Dog itself

# One of the key advantages inheritance provides us with is that we need not repeat attribute and function definitions needlessly in multiple classes


