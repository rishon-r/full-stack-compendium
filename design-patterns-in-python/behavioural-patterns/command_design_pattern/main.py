# Notes for this design pattern are taken from the ArjanCodes video on it

# COMMAND DESIGN PATTERN
# The command design pattern is a behavioural pattern
# Used to represent commands and have control over when they are executed
# It provides a way to encapsulate all knowledge about performing a particular operation into a single object
# The Command pattern wraps a request or action inside an object, 
# letting you pass actions around, queue them, undo them, or log them — without the caller needing to know how they work

# MTY FINAL UNDERSTANDING:
'''
In a typical system, objects will have operations defined as methods in their class.
The Command pattern involves creating a separate class for each significant operation you want to perform on an object.
Each command class has an execute() method which can call any number of the original object's methods in any sequence — 
this single unified interface brings consistency across the codebase. Importantly, 
each command holds a reference to its target object at construction time, so the two are already linked before execution.
An invoker object is then used to trigger these commands — it receives a command and calls execute() on it,
without any knowledge of the underlying object or what the operation actually does. 
This makes the invoker completely decoupled from the implementation. 
An added benefit of wrapping operations as objects is that they can be batched, queued,
or even undone if an undo() method is also implemented
The main advantage of the Command Pattern is DECOUPLING:
The invoker has zero knowledge of what it's triggering or on what object. 
You can swap, extend, or change commands without touching the invoker at all.

'''

# Banking systems are a great way to understand the command pattern
# Since they involve a lot of transactions

from banking.bank import Bank
from banking.commands import Batch, Deposit, Transfer, Withdrawal
from banking.controller import BankController


def main() -> None:

    # create a bank
    bank = Bank()

    # create a bank controller
    controller = BankController()

    # create some accounts
    account1 = bank.create_account("ArjanCodes")
    account2 = bank.create_account("Google")
    account3 = bank.create_account("Microsoft")

    # deposit some money in my account
    controller.execute(Deposit(account1, 100000))
    controller.undo()
    controller.redo()

    # execute a batch of commands
    controller.execute(
        Batch(
            commands=[
                Deposit(account2, 100000),
                Deposit(account3, 100000),
                # Withdrawal(account1, 100000000),
                Transfer(account2, account1, 50000),
            ]
        )
    )

    # undo and redo
    controller.undo()
    controller.undo()
    controller.redo()
    controller.redo()

    # get the money out of my account
    controller.execute(Withdrawal(account1, 150000))

    print(bank)


if __name__ == "__main__":
    main()