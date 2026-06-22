from __future__ import annotations # Required for forward references on versions older than Python 3.14

from datetime import UTC, datetime # We need this for our timestamps

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text # Here we import some column types and relationships (ForeignKey)
from sqlalchemy.orm import Mapped, mapped_column, relationship
# Mapped[...] is a type hint tool that serves two primary purposes: it brings full type safety and auto-complete to your IDE, and it standardizes how SQLAlchemy builds your database columns.

from database import Base # importing Base from our database file


# 1. We declare a Python class named 'User' that inherits from 'Base'.
# 'Base' is the SQLAlchemy declarative base class which tells SQLAlchemy that this Python class maps directly to a database table.
class User(Base):
    
    # 2. '__tablename__' tells SQLAlchemy exactly what the SQL table should be named inside the database.
    # In this case, instances of the User class will be stored in a table called "users".
    __tablename__ = "users" 
    # We set up a user table as we want blog posts to be connected to a user

    # 3. 'id' is defined as the table's primary key.
    # 'Mapped[int]' is a Python type hint for static analysis tools, while 'mapped_column(Integer, ...)' tells the database
    # to make this an auto-incrementing integer (primary_key=True does this auto increment). 'index=True' optimizes search speeds when looking up users by their ID.
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    # 4. 'username' is defined as a string column with a maximum length of 50 characters.
    # 'unique=True' prevents two users from having the same username, and 'nullable=False' ensures a username is mandatory.
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    
    # 5. 'email' is defined as a string column maxing out at 120 characters.
    # It must be unique (no duplicate accounts per email) and cannot be left blank ('nullable=False').
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    
    # 6. 'image_file' is defined as an optional string column ('Mapped[str | None]') up to 200 characters.
    # 'nullable=True' and 'default=None' mean users don't have to upload a profile picture right away; it will default to None.
    image_file: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
        default=None,
    )

    # 7. 'posts' sets up an ORM "Relationship" between the User model and the Post model.
    # This is a Python-only convenience tool (not a database column). It lets you type 'user.posts' to instantly get a list of all posts written by this user.
    # 'back_populates="author"' creates a bidirectional link, meaning the Post model must have a matching 'author' relationship pointing back to this User.
    posts: Mapped[list[Post]] = relationship(back_populates="author", cascade="all, delete-orphan") # Cascade= "all, delete-orphan" means that when a user is deleted, so should all their posts

    # 8. The '@property' decorator turns this standard Python method into a read-only property attribute.
    # It allows you to access this logic like a normal variable (e.g., 'user.image_path') instead of calling it like a function ('user.image_path()').
    @property
    def image_path(self) -> str:
        
        # 9. Checks if the user has uploaded a custom image file name to the database.
        if self.image_file:
            # 10. If they have an image, return the dynamic URL path pointing to their custom media folder upload.
            return f"/media/profile_pics/{self.image_file}"
        
        # 11. If 'self.image_file' is None/empty, fallback and return the static URL path to the default silhouette image.
        return "/static/profile_pics/default.jpg"


# 1. We declare a Python class named 'Post' that inherits from 'Base'.
# This tells SQLAlchemy that this class represents a table schema in the database.
class Post(Base):
    
    # 2. '__tablename__' defines the exact name of the table inside the database.
    # All instances of the Post class will map to rows inside the "posts" table.
    __tablename__ = "posts"

    # 3. 'id' is defined as the primary key for the posts table.
    # It is an auto-incrementing integer ('Mapped[int]'), and 'index=True' ensures 
    # that querying or sorting posts by their unique ID happens incredibly fast.
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    # 4. 'title' is a string column with a strict maximum limit of 100 characters.
    # 'nullable=False' makes the title mandatory; a post cannot exist without one.
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    
    # 5. 'content' is defined using the 'Text' type instead of 'String'.
    # While 'String' has character limits, 'Text' is used for large blocks of unrestricted text,
    # making it perfect for the actual body/paragraphs of a blog post. It cannot be null.
    content: Mapped[str] = mapped_column(Text, nullable=False)
    
    # 6. 'user_id' establishes a database-level link to the 'users' table using a ForeignKey.
    # 'ForeignKey("users.id")' explicitly links this column to the 'id' column of the 'users' table.
    # This enforces relational integrity (a post must belong to a real user) and 'index=True' 
    # dramatically speeds up lookups when fetching all posts belonging to a specific user ID.
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )
    
    # 7. 'date_posted' records when the blog post was created, mapping to a Python 'datetime' object.
    # 'DateTime(timezone=True)' ensures the database stores time zone information (avoiding server time zone bugs).
    # 'default=lambda: datetime.now(UTC)' runs a function to automatically stamp the exact current UTC time 
    # the moment a new post is inserted, meaning you don't have to provide the date manually when creating a post.
    date_posted: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    # 8. 'author' sets up an ORM "Relationship" pointing to a single 'User' Python object.
    # This is not a physical column in the database; it is a virtual convenience link for Python.
    # It allows you to type 'post.author' to instantly get the full User object of whoever wrote it.
    # 'back_populates="posts"' pairs it bidirectionally with the 'posts' relationship we wrote inside the User model.
    author: Mapped[User] = relationship(back_populates="posts")