# CSV (Comma Separated Values)
# A CSV file is a plain text file that stores tabular data (like a spreadsheet)
# Each line in the file is a row, and each value in the row is separated by a comma
# E.g a CSV file might look like this:
# name, age, city
# Alice, 30, Vancouver
# Bob, 25, Toronto

# Python has a built-in csv module for reading and writing CSV files
import csv

# READING A CSV FILE


# csv.reader() is the most basic way to read a CSV file
# It returns an iterable reader object where each row is a list of strings
with open("data.csv", "r") as f:
    reader = csv.reader(f)

    # You can iterate over the reader object to get each row
    for row in reader:
        print(row)  # each row is a list e.g ["Alice", "30", "Vancouver"]


# SKIPPING THE HEADER ROW

# CSV files often have a header row with column names
# We can skip it using next() which advances the reader past the first row
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)   # reads and discards the first row
    print(f"Columns: {header}")  # e.g ["name", "age", "city"]

    for row in reader:      # now iterates from the second row onwards
        print(row)

# USING DICTREADER 

# csv.DictReader() is a more convenient way to read CSV files
# Instead of returning each row as a list, it returns each row as a dictionary
# The keys are taken from the header row automatically
# This makes it much easier to work with specific columns by name
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        # Each row is a dict e.g {"name": "Alice", "age": "30", "city": "Vancouver"}
        print(row["name"], row["age"])  # access columns by name

# IMPORTANT NOTE ON DATA TYPES


# csv.reader() and csv.DictReader() always return values as STRINGS
# If you need numbers you must convert them manually
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        name = row["name"]          # already a string
        age = int(row["age"])       # convert to int
        print(f"{name} is {age} years old")

# WRITING TO A CSV FLE

# csv.writer() is the basic way to write to a CSV file
# We open the file in 'w' mode and pass the file object to csv.writer()
# newline="" is important on Windows to prevent extra blank lines being added between rows
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)

    # writerow() writes a single row to the file, accepts a list
    writer.writerow(["name", "age", "city"])        # write header row
    writer.writerow(["Alice", 30, "Vancouver"])     # write a data row
    writer.writerow(["Bob", 25, "Toronto"])         # write another data row

# writerows() writes multiple rows at once, accepts a list of lists
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)

    rows = [
        ["name", "age", "city"],        # header row
        ["Alice", 30, "Vancouver"],
        ["Bob", 25, "Toronto"],
        ["Charlie", 35, "Montreal"]
    ]
    writer.writerows(rows)      # writes all rows at once


# csv.DictWriter() 

# Just like DictReader, DictWriter is the preferred way to write CSV files
# Instead of writing lists, we write dictionaries
# This is more readable and less error prone since we reference columns by name
# We must specify the fieldnames (column names) upfront when creating the writer

with open("data.csv", "w", newline="") as f:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()    # automatically writes the header row from fieldnames
    writer.writerow({"name": "Alice", "age": 30, "city": "Vancouver"})
    writer.writerow({"name": "Bob", "age": 25, "city": "Toronto"})

# writerows() works with DictWriter too, accepts a list of dicts
with open("data.csv", "w", newline="") as f:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    rows = [
        {"name": "Alice", "age": 30, "city": "Vancouver"},
        {"name": "Bob", "age": 25, "city": "Toronto"},
        {"name": "Charlie", "age": 35, "city": "Montreal"}
    ]
    writer.writerows(rows)

# APPENDING TO A CSV FILE


# To add rows without overwriting existing data, open in 'a' (append) mode
# Everything else stays the same, just change 'w' to 'a'
# Note: when appending with DictWriter, do NOT call writeheader()
# as that would add the header row again in the middle of the file

with open("data.csv", "a", newline="") as f:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    # no writeheader() here since the header already exists
    writer.writerow({"name": "Diana", "age": 28, "city": "Calgary"})