from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, ForeignKey, func

# Here, Metadata, Table, and Column are all classes
# Integer, Float and String are data types for columns
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

things = Table("things", metadata,
              Column('id', Integer, primary_key = True),
              Column('name', String, nullable = False),
              Column('description', String),
              Column('price', Float),
              Column('owner', Integer, ForeignKey('people.id')),
)

# Person to Things is a one to many relationship now

metadata.create_all(engine) # Will create all tables 

# When you call metadata.create_all(engine), you don't need to manually open a connection — SQLAlchemy handles that internally.
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

# INSERTING MULTIPLE VALUES WITH THE HELP OF A DICTIONARY
insert_statement = things.insert().values([
  {'id': 1, 'name': 'bowl', 'description': "blue, ceramic", 'price': 6.7, 'owner': 1}, 
  {'id': 2, 'name': 'wine glass', 'description': "clear, white wine", 'price': 12, 'owner': 1}, 
  {'id': 3, 'name': 'TV', 'description': "LG, OLED", 'price': 300.0, 'owner': 2}, 
  {'id': 4, 'name': 'T Shirt', 'description': "Black, V neck", 'price': 20, 'owner': 3}, 
  {'id': 5, 'name': 'Baseball Bet', 'description': "Louisville Slugger", 'price': 50, 'owner': 4}, 
]) 

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

# UPDATING A TABLE
# Updat statements in SQLAlchemy are also relatively straight forward

update_statement = people.update().where(people.c.age == 30).values(age=31)
result = conn.execute(update_statement)
conn.commit()

# DELETING FROM A TABLE
delete_statement = people.delete().where(people.c.age == 31)
result = conn.execute(delete_statement)
conn.commit()

# JOINS
# .join is besically an inner join
join_statement = people.join(things, people.c.id == things.c.owner)
select_statement = people.select().with_only_columns(people.c.name, things.c.description).select_from(join_statement)

result = conn.execute(select_statement)

for row in result.fetchall():
  print(row)

# GROUP BY

group_by_statement = things.select().with_only_columns(things.c.owner, func.sum(things.c.price)).group_by(things.c.owner).having(func.sum(things.c.value) > 50)
result = conn.execute(group_by_statement)

for row in result.fetchall():
  print(row)