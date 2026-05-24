# IF STATEMENT
# The if statement is the most basic control flow statement available
# It executes a set of statements once if a condition is True
# The most basic form of the if statement consists of the if statement alone and this does nothing if the condition is not true
# If we want to execute some statements if the condition is False, we use the else statement
# The statements under the if and else statements are indented and are said to be a part of the if block and else block respectively
# Python does not use brackets but instead indentation and colons to differentiate between different blocks of code
# Example:
a=7
b=4
if a>b:
    print("Hello")
else:
    print('hi')

# If there are a series of intermediate conditions we also want to check, we can us the elif block for that.
# We can use as many elif blocks as required within a particular set of if-elif-else statements
# Note that all elif blocks and the else block are optional with the if statement
# Example: 
num= 70

if num > 90:
    print('A')
elif num > 80:
    print('B')
elif num > 70:
    print('C')
elif num > 60:
    print('D')
elif num>0:
    print("FAIL")
else:
    print("ERROR")

# It is also possible to nest if statement within each other
# An if, elif or else block can have multiple nested if statements within it

#E.g

color="red"
num=5

if num>3:
    if color=="red":
        print("Success")
    else:
        print("Failure")
elif num>2:
    if color=="red":
        print("Success")
    else:
        print("Failure")
else:
    print("Failure")

# MATCH Statements
# A match statement is superficially analogous to the switch case in Java or C
# It takes an expression and checks if that expression matches up with a series of different values (should be literals), each labelled by case
# At the point of the first match, the statements under that respective case will be executed
# The variable _ is a wildcard and never fails to match. Use it as the analogue for the default statement in switch case
# The or symbol | can also be used to help assess multiple values in a given case
# Example below:
status=409

match status:
    case 404:
        print("ERROR TYPE !")
    case 401 | 403:
        print("ERROR TYPE 2")
    case _:
        print("NEW ERROR!")

# FOR STATEMENT
# For loop is a countable loop
# A for statement traditionally in programming languages such as C and Java iterates over a given arithmetic progression of numbers
# In these languages, the programmer is given the ability to choose the starting condition, halting condition and iteration condition
# Python however differs in this case
# In Python, a for statement is used always in conjunction with a sequence (think for example list or string)
# In Python, the for statement iterates over the elements of a sequence
# Examples:
names= ["Michael", "Creed", "Janet", "Kirsten"]
# Below for statement prints out every name in names
for name in names:
    print(name)

city="Chennai"
# Below statement prints every vowel in the name of city
# It is a good example of how the if statements work together with the looping statements
for i in city:
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        print(i)

# THE range() FUNCTION
# The range() function exists in order to generate a sequence of an arithmetic progression of numbers
# This helps us when we want to iterate over an arithmetic progression of numbers
# The range() function takes the three same arguments as slices and determines the sequence of numbers in the same way- range(start, stop, step)
# start and step has same default values (0 and 1) as in slicing wherease end here has no default value
# As such if no end value is provided, it results in an error
# Examples:

print(range(3,10,2)) # Will print odd numbers from 3 upto but not including 10 in the form of a list

# For statement will print odd numbers from 1 upto but not including 100
for i in range(1, 100, 2):
    print(i)

# Note that statements in the body of a loop are all considered part of the same block and are indented appropriately
# In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t. It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.
# The range() function is a form of iterable.
# An ITERABLE in Python refers to an object that is capable of returning its elements one at a time (i.e allowing you to iterate over it)
# These iterables serve as a target for functions and constructs that expect something from which they can take successive elements until none are left
# A good example of such a statement is the for Statement and an example of such function is sum()

# WHILE LOOP (CONDITIONAL LOOP)
# Executes statements in the loop body as long as the condition in the loop header remains True
# The while loop repeatedly checks whether the expression is true after every iteration before executing again
# In practical day to day use it is common to use while loops with an exit condition at which point the loop gets broken with the break statement.
# It is also common to have an update statement for the variable in the condition in the loop body so that it gets updated after every iteration
# We say while True in order to enter an uncountable loop
a=10
while a<20: # a<20 is the condition or expression being tested for Truth
    print(a)
    a+=1 #Update statement for variable in condition
# Above loop prints numbers from 10 to 19

# NESTED LOOPS
# It is possible to nest loops within each other multiple times in order to get our desired result
# You can nest for loop in a for loop, while loop in a while loop, for loop in a while loop or while loop in a for loop
# Example

for i in range(1,6):
    print()
    for j in range(i):
        print('*', end="")
print()
'''
Above code will print a pattern of form:

.
..
...
....
.....

'''


# break STATEMENT
# The break statement is used as a means to force quit the innermost for or while loop
#E.g

for i in range(10):
    if i==5:
        break
    print(i)

# Above loop will print numbers from 0 to 4 and then break at 5 which causes it to halt

# continue STATEMENT
# continue statement forces the next iteration of the loop

for i in range(10):
    if i==5:
        continue
    print(i)

# Above loop will print numbers from 0 to 4 and then ant the 5th iteration, continue forces the next iteration. So, numbers from 0-4 and 6-9 will be printed

# The break and continue statements are often grouped together and called loop control statements or control flow statements

# pass STATEMENT
# The pass statement is called an empty statement in Python
# It means do nothing.
# It is used in a place where your logic requires code but syntax does not allow it
# Example: When you want to create a list of even numbers from a list of numbers and you want to ignore the odd numbers

li=[1,5,2,32,11,24]
even_li=[]
for num in li:
    if num%2!=0:
        pass
    else:
        even_li.append(num)
print(even_li) #even_li will now contain all even elements from li



# ELSE CLAUSE & LOOPS
# The for or while loop may be followed with an else clause.
# Statements under the else clause are executed when the loop terminates normally.
# This happens when the for loop finishes iterating through a sequence or when the condition in a while loop turns False
# They are not executed when the loop terminates through a break statement
# Example:

for i in range(1,21):
    print(i)
else:
    print("We printed numbers 1-20!!!")
# Above code will print the numbers 1-20 and then print the statement under the else clause

# THE enumerate() FUNCTION
# When looping through a sequence, one can obtain the index and value at a given position using the enumerate() function
print(enumerate(['hello', 'world',3,4,5])) # This only returns object reference
for i, v in enumerate(['hello', 'world',3,4,5]):
    print(i, v) # Here we see the values

# THE zip() FUNCTION can be used to loop over 2 sequences at the same time

l1= [1,2,3]
l2= ["apples", "oranges", "lemons"]

for val1, val2 in zip(l1,l2):
    print(val1, val2)

print(zip(l1,l2)) # This also only prints the object reference

# The sorted() function returns a new sorted list while leavoing the original sequeence alone
# This can be useful when you want to loop through a sequence in ascending order

# The set() function can be used when you want to remove duplicate elements from a sequence
# Can be useful when you only want to loop through unique elements in a sequence
# You can use sorted() and set() together like this  sorted(set(l)) in order to get the unique elements of a sequence arranged in order

# The reversed() function returns the sequence in reverse and can be useful when you want to loop through a sequence in reverse order

# MEMBERSHIP OPERATORS: in and not in decide whether or not a particular element exists in a sequence

# IDENTITY OPERATORS: is and is not are used to compare and check whether two objects are really the same object

# COMPARISON OPERATORS
# The comparison operators are >, <, ==, <=, >= and !=
# All comparison operators have same priority and their priority is lower than that of the arithmetic operators
# Membership operators and identity operators are also grouped together with comparison operators

# LOGICAL OPERATORS or BOOLEAN OPERATORS
# and, not, or are the logical operators
# Their priority is as follows: not > and > or
# Their priority is lower than that of comparison operators

# An EXPRESSION in Python is any legal combination of symbols that represents a value
# An expression can contain all the above mentioned operators, and if so they are evaluated with the above mentioned priorities in mind
# This is known as OPERATOR PRECEDENCE
# Parentheses have the highest priority and any point in time can be used when a particular part of the expression is required to be evaluated first
# Expressions in Python are evaluated from left to righ
# The ** operator has precedence over all the other arithmetic operators whose precedence follows from PEMDAS

# Comparison operators can be chained together in an expression and comparisons can be combined with logical operators
# In all cases the above mentioned precedences will follow and work alongside the left to right expression evaluation methodology of Python

# The Boolean operators and and or are so-called short-circuit operators: their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined. 
# For example, if A and C are true but B is false, A and B and C does not evaluate the expression C.
#  When used as a general value and not as a Boolean, the return value of a short-circuit operator is the last evaluated argument.

# Note that in Python, unlike C, assignment inside expressions must be done explicitly with the walrus operator :=
# This avoids a common class of problems encountered in C programs: typing = in an expression when == was intended.

# COMPARING SEQUENCES
# In Python, Sequences may be compared with other sequences of same type
# The result of this comparison is determined based on lexicographical ordering
# i.e first the first two items are compared, and if they differ this determines the outcome of the comparison;
# if they are equal, the next two items are compared, and so on, until either sequence is exhausted.
#  If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively.
#  If all items of two sequences compare equal, the sequences are considered equal.
#  If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one. 
# Lexicographical ordering for strings uses the Unicode code point number to order individual characters.

# It is legal in Python to compare objects of different types as long as the objects have appropriate comparison methods defined
# This is obviously seen in the case where integers and floating point numbers can be compared
# Example:
print(3>3.14)