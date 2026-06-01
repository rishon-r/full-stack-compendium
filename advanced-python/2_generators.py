# GENERATOR

# An iterator is any object that delivers values one at a time when you call next() on it.
# An object is said to be an iterator if it has the two following methods:
# (i) __iter__() which returns itself
# (ii) __next__() returns the next value, or raises StopIteration when done
# Example of an iterator:

class CountUp:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        value = self.i
        self.i += 1
        return value

for x in CountUp(3):
    print(x)  # 0, 1, 2

# An iterable is anything you can loop over — it produces an iterator when you call iter() on it. 
# An iterator is the thing doing the actual stepping
numbers = [1, 2, 3]       # iterable, not an iterator
it = iter(numbers)         # now it's an iterator
next(it)  # 1
next(it)  # 2
next(it)  # 3
# next(it)  # StopIteration
# Every iterator is an iterable, but not every iterable is an iterator.

# Generators are a way to create iterators in Python without building the entire sequence in memory at once.
# Instead of computing all values upfront, they produce values one at a time, on demand.

def count_up(n):
    i = 0
    while i < n:
        yield i   # pause here, send value out, resume next time
        i += 1

# You can simply iterate through a generator
for x in count_up(3):
    print(x)  # 0, 1, 2

# Or you can use next
values = count_up(5)
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

# When Python hits yield, it pauses the function, sends the value to the caller,
# and remembers exactly where it left off — local variables, position, everything. 
# The next call resumes from that exact point.

# You can only iterate once. After a generator is exhausted, it's done
# a generator function can be called multiple times, but each call creates a new, independent generator object that can only be iterated once

# GENERATOR EXPRESSIONS: An inline syntax (using parentheses) that directly returns a generator object.
squares = (x**2 for x in range(10))   # generator
print(squares)
squares_list = [x**2 for x in range(10)]  # list