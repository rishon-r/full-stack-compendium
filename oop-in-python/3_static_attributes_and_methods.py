# STATIC ATTRIBUTES
# Static attributes are the attributes of the class itself
# The previous attributes we saw are called instance attributes, that is they belong to a particular object or instance of a class
# Static attributes, also often called class attributes, refer to the attributes that are shared among all members of the class
# While instance attributes are defined in the __init__ method, static attributes are defined above the __init__method
# Static attributes are useful for data that is common among all elements of the class. A good example are totals of all elements in class and configuration items

# E.g

class FarmAnimal:
  animal_list = [] # This is an example of a static attribute
  animal_count = 0 # This is another example of a static attribute

  def __init__(self, name, kind):
      self.name = name
      self.kind = kind
      FarmAnimal.animal_count+=1 # Updating static variables. We access them via ClassName.attribute_name
      FarmAnimal.animal_list.append({'name': name, 'kind': kind})

  def display(self):
     print(f"This is {self.name} and they are a {self.kind}")

# STATIC METHODS AND PRIVATE/PROTECTED METHODS
# A static method is similar to a static attribute in the way that it belongs to the class itself rather than any instance of the class
# To define a static method, we use the' @staticmethod' decorator

# Private and Protected methods are methods prefaced by __ and _ respectively and refer to those methods that can only be used within a class
class BankAccount:
   MIN_BALANCE = 100 # Remember that it is convention in python to name constants in capitals

   def __init__(self, owner, balance=0):
      self.owner = owner
      self._balance = balance 

   @staticmethod
   def _is_valid_amount(amount):
      # Creating a protected method
      return amount > 0
   
   def deposit(self, amount):
    if BankAccount._is_valid_amount(amount):
       self._balance += amount
       print(f"{self.owner}'s new balance is {self._balance}")

    else:
       print("Deposit amount must be positive")

   @staticmethod
   def is_valid_interest_rate(rate): # see here that static methods do not take the self argument
       return 0 <= rate <= 5 # static methods don't interact with any particular instance of the class
    
account = BankAccount("Jimmy", 5000)
account.deposit(300)
account.deposit(-12)

print(BankAccount.is_valid_interest_rate(3)) # See here that the static method is called on the class itself and does not require an instance of the class to be run on

# When a static method can be used, it is always preferable to use it. This is because static methods help save memory as there is not a copy of the method in every instance of the class
# they are used in operations that do not require a particular intance of the class in order to return a result