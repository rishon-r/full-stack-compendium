# A lot of programming involves working with files
# Python has in built functionality to do this
# You can open files with the open() function
# The open function takes two arguments, a path and a mode
# Mode can be 'r', 'r+', 'w', 'w+', 'a' or 'a+' which stand for read, write and append respectively
# Modes can be described as follows:
# 'r' – Read (default). Opens for reading; error if file doesn't exist.
# 'w' – Write. Creates file if it doesn't exist; truncates (overwrites) if it does.
# 'a' – Append. Writes to the end of the file; creates it if it doesn't exist
# 'r+' – Read & write, file must exist, no truncation.
#'w+' – Read & write, creates/truncates.
# 'a+' – Read & append, creates if needed.

# we assign the open function to a file handle
fh = open('test.txt', 'r') #  opening a file in read mode

# You can iuse the read() function to read a file character by character
content = fh.read(12) # Will read the first 12 characters and move the file pointer before the start of the 13th character
new_content = fh.read(10) # Will read characters 13 to 23 (note that the newline character \n counts as a character)
newer_content= fh.read() # Using read() with no argument reads the entirety of the file

# Let us print everything we have read
for i in (content, new_content, newer_content):
  print(i) 

fh.close() # If we open a file without a context manager, we also have to close it

fh = open('test.txt', 'r') 

# Now, we will study the readline() function which will allows us to read a file line by line (including the '\n' character)
# After readline(), the file pointer advances to the start of the next line
# Add the end of the file, readline() will return an empty string "" which is a falsy value
line= fh.readline()
while line:
  print(line, end="")
  line=fh.readline()

fh.close()

# We can also use the readlines function to get every line from the file and store it in a list
# It will store lines of the file in the list line by line

fh = open('test.txt', 'r') 

linez = fh.readlines()

for line in linez:
  print(line, end = "") 

fh.close() 

# Another pythonic way of reading from a file is just itr=erating through it
fh = open('test.txt', 'r')

for line in fh:
  print(line, end="")

fh.close()

# Using a CONTEXT MANAGER
# In Python it is convention to read a file with a context manager
# This is because you don't have to worry about closing the file as it will automatically close it for you

with open("test.txt", "r") as f:
    content = f.read()

print(content)