# Below is a good example of dependency injection
# It results in loosely coupled classes resulting in more modular and maintainable code
# Here the Notifier object is passed as an argument to OrderProcessor (i.e it is dependency injected)

from abc import ABC, abstractmethod


# 1. Define an abstraction (interface)
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


# 2. Concrete implementations
class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Email: {message}")

class SMSNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"SMS: {message}")

class SlackNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Slack: {message}")


# 3. Class receives its dependency — doesn't create it
class OrderProcessor:
    def __init__(self, notifier: Notifier):  # notifier is injected from outside
        self.notifier = notifier

    def process(self, order: str) -> None:
        print(f"Processing order: {order}")
        self.notifier.send(f"Order '{order}' confirmed!")


# 4. Compose at the top level — swap freely
processor = OrderProcessor(notifier=EmailNotifier())
processor.process("ORD-001")

processor = OrderProcessor(notifier=SMSNotifier())
processor.process("ORD-002")

# This has a real payoff when testing

# A fake notifier — no real emails sent during tests!
# No network, no side effects — pure, fast, reliable testing
class MockNotifier(Notifier):
    def __init__(self):
        self.sent_messages = []

    def send(self, message: str) -> None:
        self.sent_messages.append(message)  # Just record it


def test_order_processor():
    mock = MockNotifier()
    processor = OrderProcessor(notifier=mock)

    processor.process("ORD-TEST")

    assert len(mock.sent_messages) == 1
    assert "ORD-TEST" in mock.sent_messages[0]
    print("Test passed!")


test_order_processor()