from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

import models
from database import get_db
from schemas import PostCreate, PostResponse, PostUpdate # Importing our Pydantic schemas that we will ad as response_models to our route decorators

from auth import CurrentUser

router = APIRouter()

@router.get("", response_model=list[PostResponse]) # Adding a response model will make fastapi automatically validate the data to ensure it matches the type mentioned
async def get_posts(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.Post)
        .options(selectinload(models.Post.author))
        .order_by(models.Post.date_posted.desc())
    )
    posts = result.scalars().all()
    return posts # fastapi will automatically convert this into a JSON array



@router.post(
    "",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_post(post: PostCreate,
            current_user: CurrentUser,
            db: Annotated[AsyncSession, Depends(get_db)]): # When fastapi sees a type hint, it automatically parses JSON, checks if they match up to the Pydantic schema and returns a 422 error if not

    new_post = models.Post(
        title=post.title,
        content=post.content,
        user_id=current_user.user_id,
    )
    db.add(new_post)
    await db.commit()
    await db.refresh(new_post, attribute_names=["author"])
    return new_post

# Below we illustrate how to use path parameters in fastapi
# Path parameters are a dynamic part of the url that changes based on the request made
# fastapi will automatically recognize a path parameter when it is formatted in the way below with a type hint
@router.get("/{post_id}", response_model=PostResponse)
async def get_post(post_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    
    # path parameter is automatically captured and passed as a variable into our function when function takes argument of the same name
    # and when it's type is type hinted accurately
    # The type hint is important as fastapi automatically uses that to validate requests
    result = await db.execute(
        select(models.Post)
        .options(selectinload(models.Post.author))
        .where(models.Post.id == post_id)
        )
    post = result.scalars().first()
    if post:
        return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found") # Raising HTTP Exception with status code 404 meaning resource not found

# PUT style update: Here we use the PostCreate itself as input as it makes all fields required which we need for a complete update
@router.put("/{post_id}", response_model=PostResponse)
async def update_post_full(post_id: int,
                        current_user: CurrentUser, 
                        post_data: PostCreate, 
                        db: Annotated[AsyncSession, Depends(get_db)]):
    
    result = await db.execute(
     select(models.Post)
     .where(models.Post.id == post_id)
     )
    post = result.scalars().first()
    if not post: # Raising HTTP exception if the post to be updated does not exist
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    if post.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail= "Not authorized to update this post"
        )
    # Updating all major fields
    post.title = post_data.title
    post.content = post_data.content

    await db.commit() # commiting changes
    # db here is an async SQLAlchemy session.
    #  refresh() re-fetches the current state of post (an ORM model instance) from the database,
    #  overwriting whatever values are currently sitting in memory on that object
    # By default, refresh() reloads all columns on the object. The attribute_names parameter narrows this down — 
    # it tells SQLAlchemy to refresh only the listed attribute(s), rather than every column
    # After commit(), SQLAlchemy often expires the object's attributes (so they'll be lazily reloaded on next access).
    #  But lazy-loading a relationship with a normal attribute access (post.author) would 
    # require an implicit synchronous-style DB query — which doesn't work well in async SQLAlchemy, 
    # since lazy loads aren't awaited automatically and will raise an error (MissingGreenlet / "greenlet_spawn has not been called") if you try
    await db.refresh(post, attribute_names=["author"]) 
    return post

# below is the patch endpoint, used for partial updates
# See that we pass PostUpdate as the input schema instead of PostCreate
@router.patch("/{post_id}", response_model=PostResponse)
async def update_post_partial(
    post_id: int,
    post_data: PostUpdate,
    current_user: CurrentUser,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    result = await db.execute(
        select(models.Post)
        .where(models.Post.id == post_id)
        )
    post = result.scalars().first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    if post.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail= "Not authorized to update this post"
        )
    
    update_data = post_data.model_dump(exclude_unset=True) # model.dump() converts a Pydantic model into a plain Python dictionary
    # exclude_unset is very important for our patch here
    # if exclude_unset was not set to True, Python would include every field in the model in the dictonary
    # now, since exclude_unset is set to True, only the fields that the caller actually set in the request are included in the resulting dictionary
    for field, value in update_data.items():
        setattr(post, field, value) # setattr() is a built-in Python function that lets you set an attribute on an object dynamically, using a string for the attribute name instead of writing it directly in code
        # It's the dynamic equivalent of writing object.attribute_name = value. The difference is that with setattr(), the attribute name can be a variable — a string computed at runtime — rather than something hardcoded

    await db.commit()
    await db.refresh(post, attribute_names=["author"])
    return post
  
@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int, current_user: CurrentUser, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(select(models.Post).where(models.Post.id == post_id))
    post = result.scalars().first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    
    if post.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail= "Not authorized to deleter this post"
        )

    await db.delete(post)
    await db.commit()