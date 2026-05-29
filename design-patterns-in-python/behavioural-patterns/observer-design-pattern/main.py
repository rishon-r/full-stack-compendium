# THE OBSERVER PATTERN

# The observer design pattern allows objects to subscribe to and be notified of events occuring in other objects,
#  without the two being tightly coupled

# The problem it aims to solve: sometimes when something changes in your system, several other parts of your system need to react to that change

'''
E.g 

# Without observer — the subject has to know about every dependent
class Stock:
    def update_price(self, price: float) -> None:
        self.price = price
        email_service.send_alert(price)      # tightly coupled
        dashboard.refresh(price)             # tightly coupled
        trading_bot.evaluate(price)          # tightly coupled

Basically what we see above is that whenever the stock price changes, there are  anumber of other operations that need to be done
These things that need to be done all act on different objects
By running those operations on the different objects within the Stock class when stock price is updated, we tightly couple those classes with the stock class

Every time you add a new thing that needs to react, you have to modify Stock.
That's a violation of the open/closed principle — open for extension, closed for modification.

The observer pattern solves this through the creation of an Observer interface. 
All the objects that need to change when Stock is modified, now have concrete observer classes implemented that will implement the necessary reaction to the change

The Stock class will now maintain a list of observers, and have subscribe and unsubscribe methods
which allow these concrete observers to choose to be added to and removed from the observer list respectively

It will also contain a notify method that will run the required reactionary method in each concrete observer class for every observer in the observer list when the change occurs

In this way, the Stock object is completely decoupled from any of the other objects that react when price is updated
This is due to  the fact that all these objects are updated in their respective concrete observer classes

The Observer interface is the key — it allows Stock to notify any number of 
dependents without knowing anything about them, making the system freely extensible

See below for example
'''

from typing import Protocol


# The observer interface — anything that wants to listen must implement this
class Observer(Protocol):
    def update(self, price: float) -> None: ...


# The subject — maintains a list of observers and notifies them
class Stock:
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol
        self.price = 0.0
        self._observers: list[Observer] = [] # Here stock needs to liste, so it implements ovservers

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self.price)

    def set_price(self, price: float) -> None:
        self.price = price
        self.notify()  # automatically notifies all observers


# Concrete observers (these are essentially implementations of the observer interface)
class EmailAlert:
    def update(self, price: float) -> None:
        print(f"Email: price changed to {price}")

class Dashboard:
    def update(self, price: float) -> None:
        print(f"Dashboard: refreshing with price {price}")

class TradingBot:
    def update(self, price: float) -> None:
        print(f"TradingBot: evaluating price {price}")


# Main
stock = Stock("AAPL")

stock.subscribe(EmailAlert())
stock.subscribe(Dashboard())
stock.subscribe(TradingBot())

stock.set_price(150.0)
# Email: price changed to 150.0
# Dashboard: refreshing with price 150.0
# TradingBot: evaluating price 150.0