
# In Python, classes are objects
# This means that we can pass them around in functions and treat them as any other object may be treated
# A regular class is a blueprint for creating objects
# A metaclass is a blueprint for creating objects (since a class is in and of itself an object, the class that creates classes is a metaclass)
# A metaclass defines the rules for all classes 
# type is the metaclass of all classes
# type can be used to create classes dynamically
# type() can take THREE arguments to create a class:
# type(name, bases, attributes)
# name       - the name of the class as a string
# bases      - a tuple of parent classes
# attributes - a dictionary of attributes and methods

# THE NORMAL WAY:
class Dog:
    species = "Canis Familiaris"  # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

# THE type() WAY - exactly what Python does internally:
def __init__(self, name, age):
    self.name = name
    self.age = age

def bark(self):
    print(f"{self.name} says Woof!")

Dog = type(
    "Dog",                                        # class name
    (object,),                                    # parent classes - object is the parent class of every class
    {                                             
        "species": "Canis Familiaris",            # class attribute
        "__init__": __init__,                     # instance method
        "bark": bark                              # instance method
    }
)

# CREATING METACLASSES

class Meta(type): # Note that all metaclasses must inherit from the type class
    def __new__(self, class_name, bases, attrs): # These are the arguments that the new  method takes
        # __new__ is the magic method that is always called first before __init__
        # After the __new__ method is called, it constructs the object, after which __init__ initializes it with parameters
        print(attrs)
        return super().__new__(cls, class_name, bases, attrs)
        # Here, essentially, we are overriding the new method in the type class
    
class Dog(metaclass=Meta): # this is how we change the metaclass of Dog from type to Meta
    x=5
    y=8

# THE __call__ DUNDER METHOD

# __call__ is a dunder method that allows an OBJECT to be called like a FUNCTION
# When you put parentheses () after an object, Python automatically calls __call__ on it
# If a class defines __call__, its instances become CALLABLE

# THE object CLASS

# In Python, object is the ROOT BASE CLASS of every class
# Every class in Python automatically inherits from object
# whether you write it explicitly or not
# object provides a set of default dunder methods that every class inherits
# This is why your classes have these methods even without defining them

# A comprehensive guide to understanding Python's `__new__` dunder method.
# KEY TAKEAWAYS:
# 1. `__new__` is the ACTUAL constructor. It creates and returns the instance.
# 2. `__init__` is the initializer. It configures the already created instance.
# 3. `__new__` is a static method (implicitly), taking the class (`cls`) as its first argument.
# 4. If `__new__` does not return an instance of `cls`, `__init__` will NOT be called.