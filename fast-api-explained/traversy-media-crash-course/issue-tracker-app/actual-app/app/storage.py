# Here, we are simply storing our data in JSON objects for the sake of demonstration
# However, in a production level project, it is typical to store the data in a database like PostgreSQL

# Path is a class from Python's built in pathlib module.
# It represents a file or directory path and provides helpful methods
# to work with paths in a clean, readable way
# json is a built in Python module for reading and writing JSON data
from pathlib import Path
import json

# Path("data") creates a Path object pointing to a folder called "data"
# This folder is where we will store our JSON file
DATA_DIR = Path("data")

# The / operator is overloaded by the Path class to mean path joining
# So this is equivalent to "data/issues.json"
# DATA_FILE now points to the file: data/issues.json
DATA_FILE = DATA_DIR / "issues.json"


def load_data():
  # .exists() is a method on the Path object that checks if the file
  # actually exists on disk before trying to open it
  # This prevents a FileNotFoundError if the file hasn't been created yet
  if DATA_FILE.exists():

    # open() is a built in Python function that opens a file
    # 'r' means open in read mode
    # "with" is a context manager — it automatically closes the file
    # when the block is done, even if an error occurs
    # f is the file object we use to read the file
    with open(DATA_FILE, 'r') as f:

      # .read() reads the entire file content as a string
      content = f.read()

      # .strip() removes any whitespace or newlines from both ends of the string
      # We check this because an empty file would cause json.loads() to throw an error
      # So we only try to parse if there is actual content
      if content.strip():

        # json.loads() converts a JSON string into a Python object
        # For example: '[{"id": 1, "title": "Bug"}]' becomes a Python list of dicts
        # This is the data we return to whoever called load_data()
        return json.loads(content)

  # If the file does not exist OR the file is empty, return an empty list
  # This is the default starting state — no issues yet
  return []


def save_data(data):
  # .mkdir() creates the "data" directory if it does not already exist
  # parents=True means it will also create any missing parent directories
  # exist_ok=True means it will NOT throw an error if the directory already exists
  DATA_DIR.mkdir(parents=True, exist_ok=True)

  # open() again but this time with 'w' which means write mode
  # 'w' will create the file if it does not exist
  # 'w' will also OVERWRITE the file if it does already exist
  # This is intentional — we always want to save the latest state of our data
  with open(DATA_FILE, "w") as f:

    # json.dump() converts a Python object into JSON and writes it directly to the file
    # data is the Python object we want to save (a list of issues)
    # f is the file we are writing to
    # indent=2 makes the JSON human readable by adding 2 spaces of indentation
    json.dump(data, f, indent=2)