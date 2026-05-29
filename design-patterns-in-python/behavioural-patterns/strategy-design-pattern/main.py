# STRATEGY PATTERN

# The strategy pattern allows you to swap out the behaviour of a class at run time by encapsulating each variation of that behaviour in its own class

# It tries to solve a commonly occuring problem in code
# Which is the problem of there being multiple variations of performing that task based on the situation

# An example of this problem
'''
E.g 

# Without strategy — all variations crammed into one class
class DataProcessor:
    def process(self, data: str, method: str) -> str:
        if method == "csv":
            # csv processing logic
        elif method == "json":
            # json processing logic
        elif method == "xml":
            # xml processing logic

Every time you need a new processing method you have to modify DataProcessor.
The class grows endlessly and becomes hard to maintain — again a violation of the open/closed principle.
'''

# How the strategy pattern solves this

from typing import Protocol


# The strategy interface — every strategy must implement this
class ProcessingStrategy(Protocol):
    def process(self, data: str) -> str: ...


# Concrete strategies — each encapsulates one variation of the behaviour
class CSVStrategy:
    def process(self, data: str) -> str:
        print("Processing as CSV")
        return data

class JSONStrategy:
    def process(self, data: str) -> str:
        print("Processing as JSON")
        return data

class XMLStrategy:
    def process(self, data: str) -> str:
        print("Processing as XML")
        return data


# The context — holds a strategy and delegates the work to it
class DataProcessor:
    def __init__(self, strategy: ProcessingStrategy) -> None:
        self.strategy = strategy

    def set_strategy(self, strategy: ProcessingStrategy) -> None:
        self.strategy = strategy

    def process(self, data: str) -> str:
        return self.strategy.process(data)


# Main
processor = DataProcessor(CSVStrategy())
processor.process("some data")      # Processing as CSV

processor.set_strategy(JSONStrategy())
processor.process("some data")      # Processing as JSON

