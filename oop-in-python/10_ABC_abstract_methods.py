# ABSTRACT BASE CLASSES (ABC) & ABSTRACT METHODS

# When writing object-oriented code, you will often design a parent class that represents a 
# broad concept (e.g., "Animal", "PaymentProcessor", or "DatabaseDriver").
# However, you don't actually want anyone creating a generic "Animal" or "PaymentProcessor" object, 
# because a generic version doesn't make sense—it needs specific implementations (like "Dog", "PayPal", or "Postgres").

# The Abstract Base Class (ABC) pattern allows you to:
# 1. Prevent a class from being directly instantiated (you cannot do processor = PaymentProcessor()).
# 2. Define a strict blueprint (contract) that all subclasses MUST follow.

# ABSTRACT METHOD:
# An abstract method is a method declared in the abstract class that HAS NO IMPLEMENTATION there.
# It acts as a mandatory rule: Any child class inheriting from this abstract class 
# MUST implement this method, or Python will refuse to let you instantiate the child class.

# REAL WORLD EXAMPLES OF WHERE ABC IS USED:
# - Payment Processing: An abstract `PaymentProcessor` requires all children (`Stripe`, `PayPal`) to implement `process_payment()`.
# - Database Connectors: An abstract `DBConnector` forces (`MySQL`, `MongoDB`) to implement `connect()` and `execute()`.
# - Graphic Engines: An abstract `Shape` forces (`Circle`, `Square`) to implement `calculate_area()`.

import abc # Standard library module for Abstract Base Classes

# To make a class abstract, inherit from abc.ABC
class PaymentProcessor(abc.ABC):
    """
    This is the Abstract Base Class (Blueprint).
    It defines what every payment processor in our system MUST be able to do.
    """

    @abc.abstractmethod
    def authenticate(self):
        """Every payment gateway must authenticate with its API."""
        pass

    @abc.abstractmethod
    def process_payment(self, amount: float):
        """Every payment gateway must be able to process a specific amount."""
        pass

    # Note: Abstract classes CAN contain normal, concrete methods!
    # All subclasses will inherit this method automatically without being forced to rewrite it.
    def print_receipt(self, amount: float):
        print(f"Receipt generated for total: ${amount}")


# --- SUBCLASSING THE ABSTRACT CLASS ---

class StripeProcessor(PaymentProcessor):
    """
    A concrete implementation of PaymentProcessor.
    Because we implement BOTH abstract methods, Python allows us to use this class.
    """
    def authenticate(self):
        print("Authenticating securely with Stripe API using Secret Key...")

    def process_payment(self, amount: float):
        print(f"Successfully charged ${amount} via Stripe.")


class BrokenProcessor(PaymentProcessor):
    """
    This class is BROKEN. 
    It implements 'authenticate' but FORGOT to implement 'process_payment'.
    Because it fails the blueprint contract, Python will crash if we try to create it.
    """
    def authenticate(self):
        print("Authenticating...")


def main():
    print("--- Testing Successful Abstract Implementation ---")
    # This works perfectly because StripeProcessor fulfilled the contract!
    stripe = StripeProcessor()
    stripe.authenticate()
    stripe.process_payment(99.99)
    stripe.print_receipt(99.99) # Using the shared concrete method from the parent

    print("\n--- Testing Abstract Guardrails ---")
    
    # CRASH 1: Trying to instantiate the abstract class itself
    try:
        base = PaymentProcessor()
    except TypeError as e:
        print(f"Caught Expected Error: {e}")
        # Message: Can't instantiate abstract class PaymentProcessor...

    # CRASH 2: Trying to instantiate a class that forgot to implement an abstract method
    try:
        broken = BrokenProcessor()
    except TypeError as e:
        print(f"Caught Expected Error: {e}")
        # Message: Can't instantiate abstract class BrokenProcessor with abstract method process_payment


if __name__ == '__main__':
    main()

# THE KEY ADVANTAGE: Polymorphism and Interface Security.
# By forcing a common interface via ABCs, you can safely write functions that accept 
# ANY `PaymentProcessor` subclass, confident that they all guarantee to have a `.process_payment()` method.
# It catches structural bugs early at runtime instantiation rather than failing deep inside application logic.