# ENCAPSULATION
# Encapsulation is a FUNDAMENTAL OOP PRINCIPLE
# Encapsulation is the practice of bundling data and operations on that data into an entity called a class
# in order to control access to the data and operations from anywhere outside the class
# The use of private/protected attributes and methods to prevent some data from being accessed outside the class is an example of encapsulation

# Example: 

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance        # data is hidden behind an underscore

    def deposit(self, amount):         # controlled way to modify the data
        if self._is_valid_amount(amount):
            self._balance += amount

    @staticmethod
    def _is_valid_amount(amount):      # internal logic hidden from outside
        return amount > 0
    
# The data and methods are said to be encapsulated in the class
# You will often here people say: "Implementation details are encapsulated in the class"
# This almost directly leads us to the SECOND FUNDAMENTAL OOP PRINCIPLE: ABSTRACTION