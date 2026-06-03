# DEPENDENCY INJECTION

# Dependency Injection is a design pattern where the object receives its dependencies from the outisde rather than creating them itself
# This helps make code modular, maintainable and testable

# The core idea is this: instead of a class creating what it needs, you pass in what it needs

# Bad Example below: 
# Without Dependency Injection, you see that classes are tightly coupled
class EmailService:
    def send(self, message):
        print(f"Sending email: {message}")

class OrderProcessor:
    def __init__(self):
        self.notifier = EmailService()  # Hard-wired dependency

    def process(self, order):
        print(f"Processing order: {order}")
        self.notifier.send(f"Order {order} confirmed!")

  # The problem: OrderProcessor is forever married to EmailService. You can't swap it out, and testing is painful

  