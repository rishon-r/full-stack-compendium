# Testing your code is a very importatn aspect of software development as we have seen previously
# Python allows us to test our code with unit tests using the unittest module

# Examples taken from Corey Schafer's video


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y