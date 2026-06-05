'''
SQLAlchemy is a popular Python library for working with relational databases. It serves two main purposes:

1. ORM (Object-Relational Mapper)
Maps Python classes to database tables, letting you interact with your database using Python objects instead of raw SQL

2. Core (SQL Expression Language)
A lower-level databse toolkit for building and executing SQL queries programmatically, giving you fine-grained control while still being Pythonic

'''

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

# Create engine is a function in SQLALchemy that sets up a connection to a database
# It creates an engine object which is the central point of coneectivity to a database in SQLAlchemy
# Manages a connection pool — a cache of reusable database connections
# It implements something known as lazy connection: it doesn't open a connection right away but only does so when you use it
# It takes a database url to connect to as an argument
engine = create_engine('sqlite:///mydatabase.db', echo=True) # echo=True logs all database statements

# engine.connect() opens an actual database connection from the engine's connection pool and returns a Connection object (conn).
conn = engine.connect() 

# We can now run sql commands with the connection_object.execute() function
# We need to wrap the command in text() as weel for it to run
# After we run our queries, we need to run conn.commit() in order to make the changees executed as a result of our queries persistent
conn.execute(text("CREATE TABLE IF NOT EXISTS people (id int, name text, age int)"))
conn.commit()

# We can also work ewith SESSIONS
# SESSIONS are an important concept
# This is because in sqlalchemy it is convention that:
# a) When working with the core database toolkit you use CONNECTIONS
# b) When working with the ORM, you work with SESSIONS

# If we work with sessions when working with sqlalchemy core however it is generally the same as working with connections
# But only work with sessions when working with the ORM as they take care of a lot of backround stuff
# Sessions track object state, handle identity maps, and manage the unit-of-work pattern that the ORM relies on.
# Connections don't do any of that

session = Session(engine)

session.execute(text("INSERT INTO people VALUES(1, 'Rahul', 43)"))
session.commit()

# NOTE: While so far we have been using sqlalchemy to run sql code directly, that is not generally its use case
# The two key uses as discussed before are
# (i) Using the core toolkit of SQLAlchemy to run SQL queries fast with Python functions and Metadata
# (ii) Using the Sqlalchemy ORM to convert python objects into database tables
