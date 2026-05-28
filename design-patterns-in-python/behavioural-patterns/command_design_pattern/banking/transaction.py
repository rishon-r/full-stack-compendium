from typing import Protocol

'''
Protocol is imported from Python's typing module and lets you define structural interfaces —
specifying what methods/attributes a class must have, without requiring it to explicitly inherit from anything

It's Python's way of doing "duck typing" formally

E.g 



from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        ...

Now any class that has a draw() method is considered a Drawable — no inheritance needed

'''
class Transaction(Protocol):
    def execute(self) -> None:
        ...

    def undo(self) -> None:
        ...

    def redo(self) -> None:
        ...