from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

import models
from database import get_db
from schemas import PostResponse, UserCreate, UserResponse, UserUpdate # Importing our Pydantic schemas that we will ad as response_models to our route decorators

router = APIRouter()

# CONTAINS ALL API ROUTES PERTAINING TO USERS

# We don't need to specify a path here as we will include the router in main with the prefix "/api/users"
@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED) # here status-code dictates the status code we want to return in the case of a success (by default it's 200)
async def create_user(user: UserCreate, db: Annotated[AsyncSession, Depends(get_db)]):
  # What this line does: db: Annotated[Session, Depends(get_db)]
  # It manages the database lifecycle using Dependency Injection
  # db -> The local variable name you will use inside this function to talk to your database.
  # Session' -> The Python type hint. It tells your IDE that 'db' is a SQLAlchemy database session, giving you full auto-complete for database methods like 'db.add()', 'db.commit()', and 'db.query()'
  # Depends(get_db)' -> The FastAPI dependency magic. It tells FastAPI: "Before running this route, go run the 'get_db()' function we wrote earlier, open a database connection, and inject that
  # active connection right here into the 'db' variable." Once the route finishes, 'Depends' automatically closes that connection for you
  # 'Annotated[...]' -> A standard Python feature used to cleanly bundle the structural type ('Session')
  # together with FastAPI's metadata instructions ('Depends(get_db)') without breaking standard Python syntax.
  
  # Checking if user with given username exists
  result = await db.execute(
      select(models.User).where(models.User.username == user.username)
      )
  existing_user = result.scalars().first()

  if existing_user: # raising exception if the user already exists
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Username already exists"
    )
  
  # Checking if user with given email exists
  result = await db.execute(select(models.User).where(models.User.email == user.email))
  existing_email = result.scalars().first()

  if existing_email: # raising exception if the user already exists
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Email already exists"
    )
  
  new_user= models.User(username=user.username, email=user.email) # Creating row in User database table

  db.add(new_user) # Stages insert. add does not get an await as it simply stages the new user. commit is the command that actually pushes changes to the database
  await db.commit() # Commiting to commit changes to database (executes insert and saves to database)
  await db.refresh(new_user) # Reloads the object from the database

  return new_user # Pydantic will automatically convert this to a UserResponse

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Annotated[AsyncSession, Depends(get_db)]):

  result = await db.execute(select(models.User).where(models.User.id== user_id))
  existing_user = result.scalars().first()

  if existing_user:
    return existing_user
  
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")

@router.get("/{user_id}/posts", response_model=list[PostResponse])
async def get_user_posts(user_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    '''
    Returning a particular user's posts
    '''
    result = await db.execute(select(models.User).where(models.User.id == user_id)) # First we query to find user with appropriate user id
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    result = await db.execute(
        select(models.Post)
        .options(selectinload(models.Post.author)) # We need options here as our response_model Postresponse requires it
        .where(models.Post.user_id == user_id)) # Then, we query and retrieve all posts that have the given user_id as a foreign key
    posts = result.scalars().all()
    return posts

# PATCH style update: Partial Update
@router.patch("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    result = await db.execute(select(models.User).where(models.User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    if user_update.username is not None and user_update.username != user.username:
        result = await db.execute(
            select(models.User).where(models.User.username == user_update.username),
        )
        existing_user = result.scalars().first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists",
            )

    if user_update.email is not None and user_update.email != user.email:
        result = await db.execute(
            select(models.User).where(models.User.email == user_update.email),
        )
        existing_email = result.scalars().first()
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

    if user_update.username is not None:
        user.username = user_update.username
    if user_update.email is not None:
        user.email = user_update.email
    if user_update.image_file is not None:
        user.image_file = user_update.image_file

    await db.commit()
    await db.refresh(user)
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(select(models.User).where(models.User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    await db.delete(user) # delete operation needs to interact with the session in a manner that needs await
    await db.commit()