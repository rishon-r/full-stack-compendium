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

#