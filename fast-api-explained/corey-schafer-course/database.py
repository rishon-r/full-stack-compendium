from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db" # Tells SQLAlchemy where to connect, when we want to switch databases, this is the main thing we must aim to change

# This engine is our connection to the database
# It is the core hub for any database application
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}, # This is sqllite specific because sqlite allows only one thread while fastapi allows many (don't worry too much about this)
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # This is a factory that creates database sessions
# A session can be viewed as a transaction with a database
# Each request gets its own session
# We set autocommit and autoflush to false as we want to control whenc changes get committed and flushed
# bind=engine connects your Session factory directly to your database configuration
# Call SessionLocal() to create an actual session from the session factory

# DeclarativeBase is a base class that all our ORM models will inherit from
class Base(DeclarativeBase): # In SQLAlchemy 2 we inherit from DeclarativeBase directly instead of having to do base = declarative_base()
    pass


def get_db(): # This is a dependency function that provides sessions to our routes. FastAPI's dependency injection will call this function for each request
    with SessionLocal() as db: # With makes the session work in a manner similar to a context manager, taking care of cleanup and error handling
        # The with block guarantees that no matter what happens inside it, SQLAlchemy will cleanly close the database connection when the block finishes.
        yield db # In Python, the yield statement is used to turn a standard function into a generator
        # Because the function uses yield instead of return, it becomes a generator. This is the secret sauce for managing the lifecycle of your database request
        # yield db does three things:
        # 1. It pauses the execution of the get_db function right there
        # 2. It hands over the active database session to whatever route/function that requested it
        # 3. It waits patiently in the background
        '''
        FULL EXPLANATION: 

        [ HTTP Request Arrives ]
        │
        ▼
        1. FastAPI calls get_db()
                │
                ▼
        2. 'with SessionLocal()' opens a DB connection
                │
                ▼
        3. 'yield db' pauses get_db() and hands the connection to your Route
                │
                ▼
        4. Your Route executes (e.g., fetches a user, saves a post)
                │
                ▼
        5. Route finishes and sends HTTP Response back to the user
                │
                ▼
        6. FastAPI returns to get_db() right after the 'yield' line
                │
                ▼
        7. 'with' block ends and AUTOMATICALLY closes the DB connection safely

        If you used return db instead of yield db, the function would instantly hit the end of the with block
        and close the database connection before your route even had a chance to use it.
        By using yield, the function stays alive and open while your route does its work,
        and cleanly tidies up after itself the exact moment your route is finished      
        '''

