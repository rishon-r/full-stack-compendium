# ABSTRACTION

# The aim of abstraction is to REDUCE UNNECESSARY COMPLEXITY by HIDING UNNECESSARY DETAILS
# Abstraction builds on top of encapsulation
# While encapsulation involves hiding the details of implementation and controlling how the public interface accesses them,
# Abstraction adopts the hiding of implementation details in the class so that users can interact with an object freely,
# simply utilising its functionality without worrying about complexity of implementation
# Abstraction is a fundamental computer science concept and is encountered all through the field
# A good general example refers to how we use the functionality of a TV remote and its buttons without having to worry about how the remote switches channels internally
# We say that the implementation details are "abstracted away"

# Code example

# Example take from FreeCodecamp OOP tutorial

class BadEmailService:
    # def send_email(self):
    #     self.connect()
    #     self.authenticate()
    #     print("Sending email...")
    #     self.disconnect()

    def connect(self):
        print("Connecting to email server...")

    def authenticate(self):
        print("Authenticating...")

    # We could also force clients to call connect, authenticate, send_email, and disconnect to send an email. That wouldn't be very nice tho! No abstraction means more effort for client/dev.
    def send_email(self):
        print("Sending email...")

    def disconnect(self):
        print("Disconnecting from email server...")

email = BadEmailService()

email.connect()
email.authenticate()
email.send_email()
email.disconnect()

class EmailService:
    def send_email(self):
        # Call private methods within the class
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()

    def _connect(self):
        print("Connecting to email server...")

    def _authenticate(self):
        print("Authenticating...")

    def _disconnect(self):
        print("Disconnecting from email server...")

new_email = EmailService()
new_email.send_email()