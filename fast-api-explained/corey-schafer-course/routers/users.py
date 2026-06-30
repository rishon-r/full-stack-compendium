from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile
from sqlalchemy import select, func # func is used to run case insensitive queries
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

import models
from database import get_db
from schemas import PostResponse, UserCreate, UserPublic, UserPrivate, UserUpdate, Token # Importing our Pydantic schemas that we will ad as response_models to our route decorators

from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

from auth import create_access_token, hash_password, verify_password, CurrentUser
from config import settings

from PIL import UnidentifiedImageError
from starlette.concurrency import run_in_threadpool # Used for the CPU bound task of image processing
from image_utils import process_profile_image, delete_profile_image

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

# ENDPOINT TO GET CURRENT USER
@router.get("/me", response_model=UserPrivate)
async def get_current_user(current_user: CurrentUser):
    """Get the currently authenticated user."""
    return current_user


@router.get("/{user_id}", response_model=UserPublic)
async def get_user(user_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
  # This is to generally view another user's page. That's why the response model is UserPublic as well
  # And it does not require token authenitication
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
    current_user: CurrentUser,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    

    if user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail= "Not authorized to update this user"
        )
    
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
async def delete_user(user_id: int, current_user: CurrentUser, db: Annotated[AsyncSession, Depends(get_db)]):

    if user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail= "Not authorized to delete this user"
        )
    

    result = await db.execute(select(models.User).where(models.User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    await db.delete(user) # delete operation needs to interact with the session in a manner that needs await
    await db.commit()


# Deals with profile picture uploads
# Register this endpoint as a PATCH request on /{user_id}/picture.
# response_model=UserPrivate tells FastAPI to serialize the returned object
# using the UserPrivate schema (controls which fields are exposed in the response).
# We use patch because we are updating an existing resource
@router.patch("/{user_id}/picture", response_model=UserPrivate)
async def upload_profile_picture(
    # user_id is parsed from the URL path, e.g. /42/picture -> user_id=42
    user_id: int,

    # file is the uploaded file, parsed from multipart/form-data by FastAPI.
    # UploadFile is memory-efficient: it streams to disk if the file is large,
    # rather than loading everything into RAM immediately.
    file: UploadFile,

    # current_user is a custom dependency type (CurrentUser) that
    # extracts/validates the authenticated user from the request (e.g. via a
    # JWT token), so you know who is making the request.
    current_user: CurrentUser,

    # db is an async database session, injected via FastAPI's dependency
    # injection system (Depends). get_db  yields a session tied
    # to this request's lifecycle.
    db: Annotated[AsyncSession, Depends(get_db)],
):
    # Authorization check: only allow a user to update their OWN profile picture.
    # Without this, any logged-in user could overwrite someone else's picture
    # just by passing a different user_id in the URL.
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this user's picture",
        )

    # Read the entire uploaded file into memory as raw bytes.
    # "await" is needed because UploadFile.read() is an async operation
    # (it may be reading from disk/network under the hood).
    content = await file.read()

    # Reject the upload if it exceeds the configured maximum size.
    # This protects the server from abuse (e.g. someone uploading a huge file
    # to exhaust disk/memory/bandwidth).
    if len(content) > settings.max_upload_size_bytes:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            # Convert bytes to MB for a human-readable error message.
            detail=f"File too large. Maximum size is {settings.max_upload_size_bytes // (1024 * 1024)}MB",
        )

    try:
        # process_profile_image() (defined in image_utiles) is a synchronous, CPU-bound
        # function (image decoding/resizing/saving), which would normally block
        # the async event loop and freeze the whole server for other requests.
        # run_in_threadpool() runs it in a separate worker thread instead, so
        # the event loop stays free to handle other requests while this runs.
        new_filename = await run_in_threadpool(process_profile_image, content)
    except UnidentifiedImageError as err:
        # PIL raises UnidentifiedImageError if the uploaded bytes aren't a
        # recognizable image format at all (e.g. someone uploaded a .txt file
        # renamed to .jpg). Catch it and turn it into a clean 400 error
        # instead of a raw 500 server error.
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid image file. Please upload a valid image (JPEG, PNG, GIF, WebP).",
        ) from err  # "from err" preserves the original exception as the cause, for debugging/logging

    # Keep track of the user's previous picture filename so it can be deleted
    # later, after the new one is successfully saved in the database.
    old_filename = current_user.image_file

    # Update the user's record in memory with the new filename.
    current_user.image_file = new_filename

    # Persist the change to the database.
    await db.commit()

    # Refresh the current_user object with the latest data from the database
    # (e.g. to pick up any DB-generated values like updated timestamps).
    await db.refresh(current_user)

    # Only now that the DB update has succeeded, delete the old picture file
    # from disk. Doing this last avoids a situation where the old file is
    # deleted but the DB update then fails, leaving the user with no picture
    # referenced at all.
    if old_filename:
        delete_profile_image(old_filename)

    # FastAPI will serialize this returned user object according to the
    # UserPrivate response_model declared in the decorator.
    return current_user

# Uses the same pattern as upload_profile_pic function, so I've cut out verbose explanation
@router.delete("/{user_id}/picture", response_model=UserPrivate)
async def delete_user_picture(
    user_id: int,
    current_user: CurrentUser,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this user's picture",
        )

    old_filename = current_user.image_file

    if old_filename is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No profile picture to delete",
        )

    current_user.image_file = None
    await db.commit()
    await db.refresh(current_user)

    delete_profile_image(old_filename)

    return current_user
