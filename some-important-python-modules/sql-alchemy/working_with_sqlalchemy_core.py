from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Here, Metadata, Table, and Column are all classes
# Integer and String are data types for columns
# sqlalchemy automatically maps these datatypes to the datatypes used by the database technology you are connecting to 
# So your python code remains the same regardless of the database you are connecting to

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

# Great question. When you call metadata.create_all(engine), you don't need to manually open a connection — SQLAlchemy handles that internally.
# It opens a connection from the pool, runs the CREATE TABLE statements, and closes it automatically

# You do however, need to manually open a connection any time that you plan on running actual queries
conn = engine.connect()

# The below line of code builds an INSERT statement in Python without writing any SQL
# The result is a Python object representing the SQL query — no query has been sent to the database yet
insert_statement = people.insert().values(name='John', age=67, id=1) 
# This below line of code is where the query actually gets sent to the database.
# The connection executes the INSERT statement and returns a result object containing metadata about what happened
result = conn.execute(insert_statement)
# Saves the change permanently to the database.
#  Without this, the insert would be lost when the connection closes because SQLAlchemy wraps everything in a transaction by default.
conn.commit()

# SOME MORE INSERTS
insert_statement = people.insert().values(name='Jane', age=23, id=2) 
result = conn.execute(insert_statement)

insert_statement = people.insert().values(name='Jack', age=41, id=3) 
result = conn.execute(insert_statement)

insert_statement = people.insert().values(name='Mary', age=31, id=4) 
result = conn.execute(insert_statement)

conn.commit()


# SELECT STATEMENTS

# people.select() - builds a SELECT * FROM people SQL statement on the people table object
# .where(people.c.age > 30) — appends a WHERE age > 30 filter clause (people.c gives access to the table's columns)
# The result is a SQL expression object (not yet executed)
select_statement = people.select().where(people.c.age > 30)
# Below line sends the query to the database via an active connection conn
# Returns a ResultProxy / CursorResult object containing the response
result = conn.execute(select_statement)

# result.fetchall() - Retrieves all matching rows from the result set as a list of Row object
for row in result.fetchall():
  print(row) # Prints each row, which displays as a named tuple, e.g. (1, 'Alice', 35)

'''
Alternatives to fetchall():
result.fetchone()   # returns a single Row object (the next one), or None
result.fetchmany(3) # returns next 3 rows as a list
result.first()      # returns first row and closes the result set
'''

# NOTE: you don't need to commit after a SELECT statement
# commit() is only needed when you modify the database: INSERT, UPDATE, DELETE