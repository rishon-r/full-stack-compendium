from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Here, Metadata, Table, and Column are all classes
# Integer and String are data types for columns

engine = create_engine('sqlite:///mydatabase.db', echo=True)

# Metadata
# A container that holds all your table definitions in one place.
# Think of it as a registry or catalog of your database schema
# It doesn't do much on its own, but it's needed as a central reference point.
# When you create tables, you attach them to it. You can also use it to create or drop all tables at once

metadata = MetaData()

# Table
# Represents a database table. You attach it to a MetaData object and define its columns inside it
# This is the Python equivalent of CREATE TABLE people (...). Once defined, you use this object to run queries against that table

# Column
# Represents a single column in a table. You specify the name, data type, and any constraints

people = Table("people", metadata,
               Column('id', Integer, primary_key=True),
               Column('name', String, nullable=False),
               Column('age', Integer)
)
# Note that the above line of code does not really create a table
# It simply adds a table definition to metadata
# Then to create all tables in metadata, we run metadat.create_all() and pass the engine as the argument

metadata.create_all(engine) # Will create all tables 
