# POLYMORPHISM

# Polymorphism is the fourth FUNDAMENTAL OOP PRINCIPLE
# The word polymorphism is derived from greek and means "to have many forms" (Poly = many, morph= forms)
# Polymorphism refers to how objects that are instances of different classes (i.e different objects) can respond to the same method in a different way
# This usually happens when all those said objects are subclasses of the same parent class
# polymorphism allows you to treat different objects uniformly (like putting them all in an animals list) while maintaining their unique, specialized behaviors when a method is invoked
# In a similar manner to which encapsulation allows for abstraction, inheritance allows for polymorphism

# There are two main ways polymorphism is achieved in Python:
# 1. METHOD OVERRIDING - a child class redefines a method from the parent class
# 2. DUCK TYPING - different unrelated classes implement the same method name

# 1. POLYMORPHISM VIA METHOD OVERRIDING

# Here we have a parent class Animal with a speak() method
# Each child class overrides speak() with its own unique implementation

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # This is a generic implementation in the parent class
        # Child classes will override this with their own behaviour
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        # Dog overrides the parent speak() method with its own implementation
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        # Cat overrides the parent speak() method with its own implementation
        print(f"{self.name} says Meow!")

class Cow(Animal):
    def speak(self):
        # Cow overrides the parent speak() method with its own implementation
        print(f"{self.name} says Moo!")

dog = Dog("Rex")
type(dog)
cat = Cat("Whiskers")
cow = Cow("Bessie")

# The same method speak() is called on each object
# but each object responds in its own unique way - this is polymorphism
dog.speak()   # Rex says Woof!
cat.speak()   # Whiskers says Meow!
cow.speak()   # Bessie says Moo!

# The real power of polymorphism is seen when we loop over a list of different objects
# We can call the same method on each object without caring about what type it is
animals = [dog, cat, cow]
for animal in animals:
    animal.speak()  # Python figures out which speak() to call based on the object type
                    # This is polymorphism in action


# 2. POLYMORPHISM VIA DUCK TYPING

# Duck typing comes from the phrase "if it walks like a duck and quacks like a duck, it is a duck"
# In Python, we don't care about the TYPE of an object
# We only care about whether it HAS the method we want to call
# If it does, we can call it - regardless of what class it belongs to

# Notice that these classes do NOT inherit from a common parent class
# They are completely unrelated - yet they all implement an area() method
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Again, we can loop over a list of different unrelated objects
# and call the same method on each one - this is duck typing
shapes = [circle, rectangle, triangle]
for shape in shapes:
    print(shape.area())  # Python doesn't care what type shape is
                         # It just checks if it has an area() method and calls it


# SUMMARY

# Polymorphism allows us to write cleaner and more flexible code
# Instead of writing separate logic for each object type, we can treat them uniformly
# and let each object handle the method call in its own way

# METHOD OVERRIDING  → child classes redefine a method inherited from a parent class
# DUCK TYPING        → unrelated classes implement the same method name independently
# Both achieve the same goal - the same method call producing different behaviour
# depending on the object it is called on
