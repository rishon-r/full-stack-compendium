# FILTER
# filter() takes a function and an iterable, and returns only the elements where the function returns True
# This is an inbuilt function
# E.g
nums = [1,2,3,4,5,6,7,8,9,10]
even_nums = filter(lambda x: x%2==0, nums) # returns only those numbers that are even
print(list(even_nums)) # Returns an iterator, so we have to type cast explicitly

# MAP
# map() takes a function and an iterable, and applies the function to every element, returning the transformed results
# This is also an in built function
squared_nums= map(lambda x: x ** 2, nums)
print(list(squared_nums))

# REDUCE
# reduce() collapses an iterable down to a single value by repeatedly applying a function to accumulate a result
# The function always takes two arguments — the accumulated result so far, and the next element
# You have to uimport it as it lives in functools
from functools import reduce

sum_of_nums= reduce(lambda acc, x: acc + x, nums) # acc starts as the first element of the sequence
print(sum_of_nums)
