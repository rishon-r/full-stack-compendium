from dataclasses import dataclass

# from dataclasses import dataclasses — it imports the @dataclass decorator from Python's built-in dataclasses module.
# It's a way to quickly create classes that mainly exist to store data, without writing a lot of boilerplate.

# E.g
'''
Without dataclass:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

With dataclss:

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

These two are roughly equivalent. dataclass auto generates __init__, __repr__ and __eq__ for you

'''

from dataclasses import dataclass


@dataclass
class Account:
    name: str
    number: str
    balance: int = 0

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

