from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Here declarative_base acts as a replacement for metadata (sort of)
# and we also aim to use sessions instead of connections (it is very important to do so when using ORM) so we import sessionmaker

# The essential function of the ORM is that it maps Python classes to tables in the database
# so, we are no longer using Table to create tables


engine = create_engine('sqlite:///myotherdatabase.db', echo=True)

# declarative_base() creates a base class that all your ORM model classes will inherit from.
# When a class inherits from Base, SQLAlchemy recognizes it as a mapped class — meaning it represents a database table
Base = declarative_base() # We will make all our classes inherit this base

class Person(Base):
  __tablename__ = 'people' # This defines the name of the actual table in the database
  id = Column(Integer, primary_key=True) # Name of the column is automatically taken from the variable name id
  # NOTE: when you define a column as primary_key=True with an Integer type, SQLAlchemy automatically sets it up as an auto-incrementing column. So you never need to supply an id yourself
  name = Column(String, nullable=False)
  age = Column(Integer)

  # This is not a database column — it creates a Python-level relationship between Person and Thing.
  # It tells SQLAlchemy that a Person can have many Things. This lets you do: person.things which returns a list of thing objects belonging to a person
  things = relationship('Thing', back_populates='person')

class Thing(Base):
  __tablename__ = 'things'
  id = Column(Integer, primary_key=True)
  description = Column(String, nullable=False)
  value = Column(Float)
  # Creating a foreign key
  owner= Column(Integer, ForeignKey('people.id'))

  # The other side of the relationship. Lets you do: thing.person
  # Together with things = relationship(...) in Person, this creates a bidirectional relationship — 
  # you can navigate from a person to their things, or from a thing to its owner
  person = relationship('Person', back_populates='things')
  # back_populates doesn't change anything in the database — 
  # the foreign key (owner = Column(Integer, ForeignKey('people.id'))) is what creates the real database-level link. 
  # back_populates is purely about keeping your Python objects in sync in memory 
  # so you don't get stale or inconsistent data before you commit


# Looks at all classes that inherited from Base, and creates their corresponding tables in the database 
#  if they don't already exist.
#  This is the equivalent of running all your CREATE TABLE statements at once.
Base.metadata.create_all(engine)

# Creates a Session factory — a class configured to create Session objects connected to your engine. 
# Note that at this point Session is still just a class, not an open session yet.
Session = sessionmaker(bind=engine)
session = Session() # create an actual session instance

# Below code creates a new Person Python object in memory.
#  Nothing has touched the database yet — this is just a regular Python object at this point.
new_person = Person(name='Sam', age=21)

# session.add() stages new_person to be inserted — 
# it tells SQLAlchemy to track this object and include it in the next commit, but still hasn't written to the database
session.add(new_person)
session.flush() # flush() does write to the database (it sends the SQL), but inside an open transaction that hasn't been committed yet


new_thing = Thing(description='Camera', value=750, owner= new_person.id)
session.add(new_thing)
session.flush()

print(new_person.things) # will print list of things owned by new_person
print(new_thing.person) # Will print the person owning new_thing
# Due to back_populates, we don't need to add the items manually

new_thing = Thing(description='Vase', value=35, owner=new_person.id)
session.add(new_thing)

new_thing = Thing(description='PS5', value=350, owner=new_person.id)
session.add(new_thing)

new_thing = Thing(description='IPAD', value=1000, owner=new_person.id)
session.add(new_thing)

# Flushes all staged changes to the database and commits the transaction, making them permanent.
# This is the moment the INSERT statement actually runs.
session.commit()

result = session.query(Person.name, Person.age) # This will return all the rows pertaining to the two columns as two element tuples

for row in result.all(): # .all is the equivalent of fetch all for sessions
  print(row)


# This is how you filter data in queries
# You use filter instead of .where()
result = session.query(Person).filter(Person.age > 50)
final_result = result.all()

for row in final_result:
  print(row)


# We can also delete as follows
result = session.query(Thing).filter(Thing.value < 50).delete()
session.commit()

# Updates work as follows
result = session.query(Person).filter(Person.name == 'Sam').update({'name': 'BigDawg'})
session.commit()

# Joins work as follows
result = session.query(Person.name, Thing.description).join(Thing, Person.id == Thing.owner).all()

for row in result:
  print(row)

# Group by and having
result = session.query(Thing.owner, func.sum(Thing.value)).group_by(Thing.owner).having(func.sum(Thing.value) > 50).all()
for row in result:
  print(row)

# Will close the current session and rolls back all uncommited changes
session.close()