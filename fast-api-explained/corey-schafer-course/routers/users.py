from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, func # func is used to run case insensitive queries
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

import models
from database import get_db
from schemas import PostResponse, UserCreate, UserPublic, UserPrivate, UserUpdate, Token # Importing our Pydantic schemas that we will ad as response_models to our route decorators

from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

from auth import create_access_token, hash_password, oauth2_scheme, verify_access_token, verify_password
from config import settings

router = APIRouter()

# CONTAINS ALL API ROUTES PERTAINING TO USERS

# We don't need to specify a path here as we will include the router in main with the prefix "/api/users"
@router.post("", response_model=UserPrivate, status_code=status.HTTP_201_CREATED) # here status-code dictates the status code we want to return in the case of a success (by default it's 200)
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
      select(models.User).where(func.lower(models.User.username) == user.username.lower())
      )
  existing_user = result.scalars().first()

  if existing_user: # raising exception if the user already exists
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Username already exists"
    )
  
  # Checking if user with given email exists
  result = await db.execute(select(models.User).where(func.lower(models.User.email) == user.email.lower()))
  existing_email = result.scalars().first()

  if existing_email: # raising exception if the user already exists
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Email already exists"
    )
  
  new_user= models.User(
    username=user.username,
    email=user.email.lower(),
    password_hash=hash_password(user.password)
    ) # Creating row in User database table

  db.add(new_user) # Stages insert. add does not get an await as it simply stages the new user. commit is the command that actually pushes changes to the database
  await db.commit() # Commiting to commit changes to database (executes insert and saves to database)
  await db.refresh(new_user) # Reloads the object from the database

  return new_user # Pydantic will automatically convert this to a UserResponse

# This is a FastAPI login endpoint — it's where create_access_token actually gets used in practice
# @router.post(...) — this endpoint responds to POST requests at the path /token (a conventional path name for OAuth2 token endpoints).
# response_model=Token — tells FastAPI to validate/serialize the return value against a Pydantic model called Token (likely something like {access_token: str, token_type: str}), 
# and to document this shape in the auto-generated API docs (Swagger/OpenAPI)
# form_data: Annotated[OAuth2PasswordRequestForm, Depends()] -
# This parameter uses FastAPIs dependency Injection system
# OAuth2PasswordRequestForm is a built-in FastAPI class that expects form-encoded data (not JSON)
# with fields like username and password — this matches the OAuth2 "password flow" spec
# Depends() tells FastAPI: "extract this from the incoming request automatically" 
# (parse the form body, validate it against OAuth2PasswordRequestForm's structure)
# When you use Depends() without passing an explicit function or class inside the parentheses, 
# FastAPI automatically uses the type hint declared next to it as the dependency
# Depends() sees OAuth2RequestForm (which is typically OAuth2PasswordRequestForm from fastapi.security)
#  and treats that class exactly as if you had written Depends(OAuth2PasswordRequestForm)
# Because of how OAuth2PasswordRequestForm is built internally, 
# FastAPI recognizes that these fields must come from an HTML form (application/x-www-form-urlencoded).
# It intercepts the incoming HTTP request body and extracts the values matching those field names
# OAuth2PasswordRequestForm is a built-in helper class in FastAPI designed specifically to handle user authentication logins using a username and password
# It tells FastAPI to expect the login credentials submitted through a standard HTML form (application/x-www-form-urlencoded) rather than a JSON body
@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[AsyncSession, Depends(get_db)],
):
    # Look up user by email (case-insensitive)
    # Note: OAuth2PasswordRequestForm uses "username" field, but we treat it as email
    result = await db.execute(
        select(models.User).where(
            func.lower(models.User.email) == form_data.username.lower(),
        ),
    )
    user = result.scalars().first()

    # Verify user exists and password is correct
    # Don't reveal which one failed (security best practice), this is why we send the same error for both
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token with user id as subject
    # timedelta class from the built-in datetime module, which is used to represent and manipulate durations or spans of time
    # While a datetime object represents a specific moment in time (like January 1st at noon), a timedelta object represents an amount of time (like 5 days, 2 hours, or 30 seconds)
    access_token_expires = timedelta(minutes=settings.access_token_expires_minutes)
    access_token = create_access_token(
        data={"sub": str(user.id)},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")

# Endpoint to get the current user
# When you inject oauth2_scheme into a route using Depends(), FastAPI automatically looks at the incoming request's HTTP headers. 
# It searches specifically for a header named Authorization and expects the value to follow the standard Bearer format: Authorization: Bearer <your_jwt_token_here>
# It strips away the word "Bearer " and extracts just the raw token string, passing it directly into your route function.
@router.get("/me", response_model=UserPrivate)
async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[AsyncSession, Depends(get_db)],
):
    """Get the currently authenticated user."""
    user_id = verify_access_token(token)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Validate user_id is a valid integer (defense against malformed JWT)
    try:
        user_id_int = int(user_id)
    except (TypeError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    result = await db.execute(
        select(models.User).where(models.User.id == user_id_int),
    )
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


@router.get("/{user_id}", response_model=UserPublic)
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
@router.patch("/{user_id}", response_model=UserPrivate)
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

    if user_update.username is not None and user_update.username.lower() != user.username.lower():
        result = await db.execute(
            select(models.User).where(func.lower(models.User.username) == user_update.username.lower()),
        )
        existing_user = result.scalars().first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists",
            )

    if user_update.email is not None and user_update.email.lower() != user.email.lower():
        result = await db.execute(
            select(models.User).where(func.lower(models.User.email) == user_update.email.lower()),
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
        user.email = user_update.email.lower()
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