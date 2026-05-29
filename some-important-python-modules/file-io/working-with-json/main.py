# JSON (Java Script Object Notation)
# JSON is essentially just a lightweight data format used for storing and exchanging data
# Despite having JavaScript in its name, it is language agnostic and used everywhere
# It represents data in a human readable format
# JSON is heavily used to facilitate data transfer in web applications between a client, such as a web browser, and a server

# JSON consists of key: value pairs, wrapped in {}
# These key : value pairs wrapped in {} are called OBJECTS, we often call the JSON Objects
# Different key : value pairs are separated by commas
# square brackets [] hold arrays
# Keys are called property names and are strings wrapped in double quotes
# Values can be strings, numbers, booleans, numbers (integers and floats are just considered numbers in JSON), nulls and arrays

'''
E.g
{
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "cycling"],
    "address": {
        "city": "Vancouver",
        "zip": "V6B 1A1"
    }
}

'''

# JSON translates very naturally to python (looks like a dictionary) and we can work with them by importing the json module 

# Examples are taken from Corey Schafer's video on JSON in Python

''' JavaScript Object Notation '''
import json # json module is a part of the standard library

# json.loads(json_string) loads a json string as a dictionary in Python

# json.dumps(python_dict, indent=2, sort_keys=True) will make a python dictionary a json string, also takes indent argument that takes an integer value
# This will makeit easier to read
# We can also sort_keys = True which will sort all the keys


# CONVERSION TABLE:
'''
JSON Python 
string str
number int / float
boolean bool
null None
array list
object dict

'''

with open('states.json') as f:
  # json.load() reads a JSON file and converts it into a Python object (typically a dictionary). 
  # It takes a file object as its argument, so it's used in conjunction with open()
  data = json.load(f) 

for state in data['states']:
  del state['area_codes']

with open('new_states.json', 'w') as f:
  # json.dump() is the opposite of json.load() — it takes a Python object and writes it to a JSON file.
  # It takes two arguments: the data to write, and the file object to write to
  # indent – pretty prints the JSON with indentation, making it human readable
  json.dump(data, f, indent=2)