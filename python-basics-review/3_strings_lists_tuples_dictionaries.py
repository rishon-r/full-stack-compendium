# Stings, Lists, Tuples, Dictionaries and sets in Python are generally called SEQUENCE TYPES
# They are some of the most important datatypes in hte programming language and values of their kind can be assigned to variables

# STRINGS
# Python is well capable of handling text as well as numbers
# Text is usually referred to as a string in Python and is represented by type str
# In Python, strings are immutable sequences of UNICODE POINTS.
# They can be enclosed in single quotes or double quotes for single line strings and in triple quotes for multiline strings
# Strings can hold any character inside them, however there are some characters with special meaning to thhe Python interpreter that we have to format in a particular way
# To format these, we use characters known as escape sequences 
# A good practical usecase of this is when we need a quote in a string and a= 'they're here' will return an error. So we do it as follows
a= 'they\'re here'
# this will not return an error
# Some other common escape sequences are \'' for double quotes, \\ is used to represent a backslash and \n is used to represent a newline character the \ character itself is called the escape sequence character
# When we don't want \ to be interpreted as a special character in the entire string, we use something known as a raw string
# In a rawstring, \ characters are not treated as special characters. 
# We can create rawstrings by adding a r in front of the first quote. Example:
b= r"hey\ we\ printing\ backslashes \'"
print(b)
# NOTE: A rawstring may not end in an odd number of \ characters as this causes some weird internal stuff with the quote character ending the string.
# The print() statement removes the quotes when outputting a string so as to make it look better
# By strings are immutable we mean that their value cannot be changed in place
# That is after they have been created, we can't change the values in the string. e.g a[3]="h" will return an error whereas it might not in a mutable type
# MULTI LINE STRINGS
# Python supports multi-line strings. Primary way of creating them involves using triple quotes. In this case, End of Line characters (\n) are automatically added by Python
m= """This
is
a
multi!!"""
print(m[4]) # Will print an EOL character (newline)
# Adding a \ at the end of every line prevents python from adding an EOL character at the end of every line
m= """This\
is\
a\
multi!!"""
print(m[4]) # Will not print an EOL character (newline)
# STRING OPERATIONS
# CONACATENATION: Process of adding multiple strings using the + operator (it is called the concatenation operator here)
# Example:
print("py"+ "thonnn")
# REPLICATION: Process of repeating a particular string multiple times ( a string anologue for multiplication).
# We use an integer in combination with the replication operator * and the string we want to repeat. Example:
print( 3 * "hello")
print(4*"my"+"heavens") #they can also be used in combination

# Another feature which is not very important is when dealing with two string literals placed next to each other
# They will automatically get concatenated with each other
# This does not work for more than 2 string literals and when either of the string literals is of the form of a variable

# INDEXING
# Indexes serve as a valid means of accessing individual characters of the string and works as a good means to slice strings
# Strings are indexed both with forward indexes from 0 to (length - 1) and backwards from -1 to -length
# Slicing works based on the [start:stop:step] syntax
# Default value for start is zero, step is 1 and end is length
# step indicates the number of characters to be skipped
# The end value is not inclusive in the slice
# We can use the len() function to get length of a sequence
# Examples:
s= "hello world"
print(s[0]) #prints h (first character)
print(s[-1]) #prints d (last character)
print(s[-11]) #prints h (first character)
print(s[0:4]) #prints hell (first four characters)
print(s[4:]) #prints every character from 4th to end 
print(s[::-1]) # will print the string in reverse
print(len(s)) # Will print 11 as the string has 11 characters
# The length of a slice for non negative indices is the difference between the two indices mentioned
# If the end index is out of bounds, this will not return an error. It will simply slice the string until its last character

# STRING METHODS: strings come with a lot of helpful methods that are of use
print(s.capitalize()) # Returns the String with its first letter capitalized
print(s.upper()) # Prints fully uppercase version of string
print(s.lower()) # Prints fully lowercase version of string
print(s.isupper()) # Returns True if string is fully uppercase, false otherwise
print(s.islower()) #  Returns True if string is fully lowercase, false otherwise
print(s.title()) # Returns string with first letter of every word capitalized
print(s.istitle()) # Returns True if string is in title format, false if otherwise
print(s.isalnum()) # Returns True if string is comprised of only alphabet and numeric characters, false otherwise
print(s.isspace()) # Returns True if string is only comprised of spaces, false if otherwise
print(s.strip()) # Removes all whitespaces at the ends of the strings
print(s.lstrip()) # Removes all leading whitespaces from the string (at the start)
print(s.rstrip()) # Removes all trailing whitespaces from the string (at the end)
print(s.find("hel")) # Takes a substring at argument, returns index of first occurence of that substring withing the string, returns -1 if nothing is found
print(s.startswith("he")) # Returns True if the string starts with "hel", False if otherwise (takes substring as an argument)
print(s.endswith("ppp")) # Returns True if the string ends with "ppp", False if otherwise (takes substring as an argument)
print(s.split()) # Returns a list of substrings that have been split up at every instance of the substring mentioned as optional argument (called the delimiter), if no argument is mentioned takes space as the default delimiter

# FORMATTED STRING LITERALS
# These are often called f-strings. 
# These are strings prefixed with the letter f or F
# When compared to normal string literals that are constant values, the f-strings are different.
# Their value is only known at run time.
# They have replacement fields indicated by {} that are filled in at runtime
# A replacement field is indicated by a single open curly brace { and starts with a python expression
# Example:
name= "Michael"
age= 47
result= f"My name is {name} and age is {age}"
print(result) # Will output: My name is Michael and age is 47
# Parts of the string outside the curly braces are treated like normal string literals and escape sequences are treated in the same way
# Any double curly braces in an f-string are replaced by single curly braces. Example:
result_2 = f"My name is {{name}} and age is {{age}}"
print(result_2) # Will output: My name is {name} and age is {age}
# We see that it works analogous to the \\ escape sequence

# FORMAT STRING
# Format strings are an older version of what the f-string now does.
# Strings can have placeholders indicated by {} which are then replaced by the .format() method
# Examples:
print("Roses are {}, Violets are {}".format("Red", "Blue")) # Will print: Roses are Red, Violets are Blue
# We can also use positional indexes and named arguments
print("Roses are {1}, Violets are {0}".format("Blue", "Red")) # Will print: Roses are Red, Violets are Blue (POSITIONAL INDEXES)
print("Roses are {clr1}, Violets are {clr2}".format(clr2= "Blue", clr1 ="Red")) # Will print: Roses are Red, Violets are Blue (NAMED ARGUMENTS)
# f-strings do the same in a more elegant way. Example:
clr1="Red"
clr2="Blue"
print(f"Roses are {clr1}, Violets are {clr2}") # Will print: Roses are Red, Violets are Blue

# printf() style formatting
# This is the old school way of formating that comes from C. It is not used very often as f-strings and .format() do a much better job at achieving the same required result
# In C, we use things called format specifiers when we want to print out the valuse of variables in a printf statement
# In Python, we adopt this printf style formatting
# In Python, String objects have one built in operation: the modulo operator %
# This is also known as the string formatting or interpolation operator
# We use it with string objects in the form: format % values where format is a string and values is a tuple (if the string only has one argument or format specifier, values can be a single non tuple object)
# In the string format, replacement fields are marked by format specifiers (we call format specifiers arguments in this case)
# The elements of values replace the format specifiers in the string
# Example:

name= "Jim"
age= 31
result= "%s is their name and %d is their age" % (name,age)
print(result)

# LISTS

# Lists serve as our first encounter with COMPOUND DATA TYPES
# These are datatypes used to group together other values
# Lists are mutable which means their values can be changed in place
# Lists consist of comma separated values stored between square braces
# They can store multiple different kind of datatypes (values stored can be of any type)
# In a manner similar to strings, they can be indexed and sliced (this serves for all sequence data types)

li= [3.14, 'Apple', [1,2]] # It is possible to nest lists inside lists
# We can then access them via double indexes
print(li[2][0]) # Will print 1
print(li[0]) # prints 3.14
print(li[1:3]) # prints [ 'Apple', [1,2]]
# All slice operations create a new list containing the requested elements
li[1]= "Orange" # Changes li to [3.14, "Orange", [1,2]] (This shows mutability)
print(li)

# You can add new items to the end of the list using the append method
li.append(420) # adds 420 to the end of list
print(li)
# The built-in len() function also applies to lists and will return the number of elements in a given list

# IMPORTANT 
# Simple assignment in Python never copies data
# Example:
new_li= li # Here, new li simply points to the same list that li refers to
# So changing li in any form will cause the changes to be reflected in new_li
# In Python, variables are essentially labels/references that point to objects in memory, not containers that hold values directly
# Example:
li[0]= 33
print(new_li[0]) # This will also print 33

# It is possible to assign to a slice. This often results in a change in the size of the list or clearing of the list entirely
# Examples:

li[1:2]=["A", "B", "C"]
print(li) # prints [33, "A", "B", "C", [1,2], 420]
li[:]=[] # Will make li point to an empty list

# MEMBERSHIP OPERATORS: in, not in are the two membership operators that are used to check whether or not a particular value belongs in a sequence.
# They return a boolean value as result

# LIST METHODS
# There are a series of useful methods that can be used on lists
li=[1,2,3,4,5]
print(li)
# 1. list.append() is used to add a ssingle element to the back of the list
li.append(6)
print(li)

# 2. list.extend() allows you to add multiple elements to the back of a list.
# It take one argument which is a sequence and every individual element of the sequence is added as an individual element to the list
li.extend('hello')
print(li)
li.extend([[7,8,9]])
print(li)
# Appending a sequence to the list results in the entire sequence being added as a single element to the list

# 3. list.pop() removes and returns last element of the list if no argument is provided. 
# It takes an optional argument which is an index and removes the element at index mentioned if specified instead of arbitrarily removing last element
# It returns an IndexError if an invalid index is provided

li.pop()
print(li)
li.pop(3)
print(li)

# 4. list.remove() takes an element as an argument and removes the first occurence of that element from the list
# Returns ValueError if the element is not found
li.remove('l')
print(li)

# 5. list.index() takes an element that is a part of the list as an argument and returns the index of its first occurence
# If the element does not exist, it returns ValueError
print(li.index('h'))

# 6. list.clear() removes every eelement in the list without deleting the list object. The list just becomes an empty list
li.clear()
print(li)

li=[1,2,3,4,5]
print(li)

#7. list.reverse() reverse the order of elements in the list in place
li.reverse()
print(li)

# 8. list.sort() sorts the list in place, it takes an optional keyworrd argument called reverse which can be Boolean value either true or false. 
# It is False by default. If True it will sort in descending order
# This is done provided that all elements in the list are of a comparable type

li.sort()
print(li)
li.sort(reverse=True)
print(li)

# 9. list.insert(pos, elem): Inserts the element elem at the index mentioned as pos.
#  All the elements in list at that index and further will be moved one index up

li.insert(3, 300)
print(li)

# 10. li.count(elem) counts the number of times an element elem occurs in the list. Returns 0 if the element is not found
print(li.count(1))

# 11. list.copy() creates a shallow copy of the list
new_li=li.copy()
print(li, new_li)
li.append(5)
print(new_li) # changes made in li are reflected in new_li as it is a shallow copy

# Note that insert, remove and sort all return no value (i.e they return None)
# This is a design principle implemented through all mutable objects in Python

# del statement
# The del statement provides a way of deleting elements from a list using indexes and slices rather than using their value unlike remove
# It differs from pop() as it does not return a value
# Examples:

del li[1] # deletes element at index 1

del li[3:] # deletes every element from list after and including index position 3

del li # clears the list and deletes the list object

# USING LISTS AS STACKS
# With the help of list methods, a list in Python can very easily function as a Stack which is a LIFO (Last in, First out) daa structure
# Simply use list.append() to add an element to the back of the list (top of stack) and list.pop() without index mentioned as an argument to return the element last added to list with append.
# Example:
li= [7,6,4,3,2]
li.append(6) # adding to top
li.pop() # removes element at the top

# USING LISTS AS QUEUES
# A Queue is a FIFO data structure (First in, First out)
# Although it is possible to use a list as a queue, lists don't provide an efficient implementation of a queue
# This is because while appends and pops from the end of the list are fast, insert and pop with index operations which are required for queues are slow
# This is because an insert or pop with index operation involves reshuffling of all other elements in the list and this is slow
# collections.deque provides a much better implementation with fast appends and pops from both ends
# An example from the documentation:

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

print(queue)                      # Remaining queue in order of arrival

# TUPLES
# Tuples work similarly to lists except for two main key differences
# DIFFERENCE 1: Tuples use parentheses instead of square brackets []
# DIFFERENCE 2: Tuples are immutable objects whereas lists are mutable objects (Tuples are often called heterogenous sequences while lists are called homogenous sequences)
# This means values in a tuple cannot be changed in place

# In Python, objects like lists, tuples and strings are referred to as sequence data types
# Sequence data types are similar in ways of indexing and slicing
# Example:

t= (1,2, "hello", [1,2,3])
print(t[0])
print(t[1:3])

# As tuples are immutable, you can't assign a new value based on position. e.g t[0]= 4 would result in an error

# Although tuples are immutable, they may contain mutable objects as elements and one is allowed to change values of this mutable object in place.
print(t)
t[3][1]="changed"
print(t)

# SINGLE ELEMENT TUPLES
# When creating single element tuples, it is important to place a comma of the element.
# Otherwise, the Python interpreter considers the object to be the same type as the element inside the single element tuple
# Example:
t=(3)
print(t, type(t)) # t here will be of type integer
t= (3,)
print(t, type(t))
# NOTE: The type() function is a built in Python function that returns type of any object in Python
# Empty tuples are created with an empty set of parentheses
# Example:

t=()
print(t, type(t))

# SEQUENCE CONSTRUCTORS
# Lists, Strings and Tuples have respective sequence constructors list(), str() and tuple() respectively.
# These are used to convert a given sequence into a list, tuple or string respectively
# Example:

s="hello"
l= [1,2,3,4,5]

new_l=list(s)
new_s= str(l)
new_t= tuple(l)

print(new_l, new_s, new_t)

# One can also create empty sequences with the sequence constructor. Just don't provide an argument

new_l=list()
new_s= str()
new_t= tuple()

print(new_l, new_s, new_t)

# PACKING AND UNPACKING TUPLES
# NOTE: Tuples can also be created without mentioning parentheses

t= 3, 4, 5 # this is a valid way of creating the tuple (3,4,5)
# The above statement is a valid example of packing a tuple. The values 3, 4 and 5 are paked into the tuple
# The reverse operation is possible and called tuple unpacking

x, y, z= t
print(x, y, z)

# This is in general called sequence unpacking and can be applied to any sequence
# Example:
s= "hello"
var1, var2, var3, var4, var5, var6= s
print(var1, var2, var3, var4, var5, var6)

# Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.

# DICTIONARIES

# Another very useful data type in Python is the dictionary
# They are often referred to as associative arrays in other language
# Dictionaries are defined as unordered collections of key: value pairs that are separated by commas and enclosed in curly braces {}
# Unlike sequences which are indexed by numbers, Dictionaries are indexed by keys
# Mentioning dictionary name followed by key name in this square brackets results in you referring to the value in the dictionary stored with that particular key
# You can access the value stored at key by typing: d[key]
# Keys in a dictionary must be of an immutable type while values can be of any type
# Tuples can be used as keys if the tuple consists of only immutable values
# It is a requirement that keys in a dictionary must be UNIQUE 
# A pair of curly braces on its own creates an empty dictionary
# Example: Working with a dictionary

d={} # creates empty dictionary
print(d)
new_d={1: "hello", 'A': 2}
new_d['A']= 'world' # changes value at key 'A'
new_d[2]= "hey" # creates new key 2 in the dictionary with value "hey"
print(new_d)
newer_d=dict() # creates a new empty dictionary using the dictionary constructor
#You can create a dictionary easily using the dict() function and keyword arguments
#Example:
example= dict(name="Jim", age=33, office="Dunder Mifflin")
print(example)

# Looping through a dictionary: Iterating through a dictionary iterates through the set of keys in the dictionary not the values
# The values however can be accessed easily if the keys and name of dictionary are known

for key in new_d:
    print(f"Key: {key} and Value: {new_d[key]}")

# Using any of the sequence constructor methods alongside a dictionary will create a sequence with only the keys in the dictionary
l= list(new_d)
print(l)

# 3 very useful dictionary functions

keys= new_d.keys() # This will return a sequence consisting of only the keys in the dictionary
vals= new_d.values() # This will create a sequence consisting of only the values in the dictionary
its= new_d.items() # This will return a sequence consisting of all the key value pairs in dictionary stored as individual (key, value) tuples
print(keys)
print(vals)
print(its)

# DICTIONARY COMPREHENSIONS exist and can be used according to following syntax

d= {x: x**2 for x in range(10)}
print(d)

# SETS
# Python provides an implementation for the mathematical set
# It is basically an unordered collection with no duplicate elements
# Consists of values separated by commas and enclosed in curly braces {}
# Some common use cases of sets are eliminating duplicate entries and using membership operators for testing
# You can create a set using the set() function
# To create an empty set you cannot use {} but must instead use the set() function
# Using {} on its own will result in creation of an empty dictionary not an empty set
# Some examples:

s= {"hello", 1, 2, "bye", 2} #mentioning a duplicate 2 here will not result in an error but simply the 2 not getting stored the seconnd time
print(s)
s= set("abracadabra")
print(s) # You see that duplicate values of a and b are not stored in the set

# SETS are MUTABLE in python and you can add and remove elements after creating a set
# E.g
s.add(277)
s.remove(1)
print(s)

# SET COMPREHENSIONS
# Similar to list comprehensions, set comprehensions are also supported by Python
# Example

s= {x for x in range(10)}
print(s)

# LIST COMPREHENSIONS

# List comprehensions provide a fast way to create new lists
# This is especially true when the new list to be created consists of elements of another sequence that are changed a bit
# Example: (The below 2 pieces of code do the same thing)

# PIECE 1
li=[]
for x in range(5):
    li.append(x**3)
print(li)

#PIECE 2
new_li= [x**3 for x in range(5)]
print(new_li)

# A list comprehension involves brackets containing an expression followed by a for statement, then zero or more for and if statements
# As a result it returns a list which is a result of evaluating the expression with respect to the for and if statements that follow it
# Another example:

li= [1,2,3,4,5,6,7,8]

even_li= [x for x in li if x%2==0] # Is a list consisting of only the even numbers from li
print(even_li)

# As mentioned above, we can use multiple for statements in a list comprehension
# The below 2 pieces of code mean the same

# PIECE 1
li=[]
for x in range(10):
    for y in ('hey', 'by', 'hello'):
        if len(y)==x:
            li.append((y,x))
print(li)

#PIECE 2
new_li= [(y, x) for x in range(10) for y in ('hey', 'by', 'hello') if len(y)==x]
print(new_li)

# NESTED LIST COMPREHENSION
# The first expression in a list comprehension can be any expression including another list comprehension
# Example: Construction a 3x5 matrix with numbers 1-5 in each row

li= [[x for x in range(1,6)] for i in range(3)]
print(li)

# Example: Construction a 3x5 matrix with numbers 1-15 
li= [[x+ 5*i for x in range(1,6)] for i in range(3)]
print(li)