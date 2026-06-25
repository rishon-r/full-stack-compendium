from datetime import UTC, datetime, timedelta
import jwt
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
from config import settings
from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import models
from database import get_db

password_hash  = PasswordHash.recommended() # Creates a password hash with argon2 using the recommended settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/token") # OAuth2passwordBearer extracts the token from the authorization header
# When a client sends the token in authorization header, the schema extracts it for us
# This also enables the authorize button for us in our docs which makes testing authentication a lot easier

def hash_password(password:str) -> str:
  # Takes in a plaintext password and returns the hash
  return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
  # Takes a plain password and a hashed password and returns True if they match (otherwise returns False)

  return password_hash.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str: # Function takes a data dictionary and optional expire time in time_delat format
    """Create a JWT access token."""
    # dictionary.copy() creates a shallow copy of a dictionary — a new dictionary object with the same key-value pairs as the original
    # Changes to copied (adding/removing/changing top-level keys) won't affect original, and vice versa
    to_encode = data.copy()

    if expires_delta: # Checks if expires_delta was actually provided (not None and not falsy, e.g. not timedelta(0))
        expire = datetime.now(UTC) + expires_delta # If it was provided, calculate the expiration time as the current UTC time plus that custom delta
    else:
        expire = datetime.now(UTC) + timedelta( # Otherwise, fall back to a default expiration time, pulled from app settings (e.g. settings.access_token_expire_minutes might be 30
            minutes=settings.access_token_expire_minutes, 
        )
    to_encode.update({"exp": expire}) # Adds an "exp" key to the copied dictionary, set to the calculated expiration datetime. "exp" is a standard JWT claim name that libraries use to know when a token expires

    encoded_jwt = jwt.encode( 
        to_encode, # This is the payload: your data + expiration. "Payload" refers to the actual data being carried/transmitted by something, as opposed to the overhead, headers, or metadata wrapped around it
        settings.secret_key.get_secret_value(), # the secret key used to sign the token, retrieved from a settings object (the .get_secret_value() suggests it's wrapped in something like Pydantic's SecretStr to avoid accidentally logging/printing the raw secret).
        algorithm=settings.algorithm, # the signing algorithm to use
    ) # Encode the dictionary into a signed JWT string
    return encoded_jwt

def verify_access_token(token: str) -> str | None:
    """Verify a JWT access token and return the subject (user id) if valid."""
    try:
        payload = jwt.decode(
            token, # the JWT string to decode/verify
            settings.secret_key.get_secret_value(), # the same secret key used in create_access_token to sign the token. It's needed here to recompute the signature and check it matches (as we covered earlier).
            algorithms=[settings.algorithm], # explicitly tells the library which algorithm(s) are acceptable
            options={"require": ["exp", "sub"]}, # tells the library that the payload must contain exp (expiration) and sub (subject/user ID) claims. 
            # If either is missing, the library treats the token as invalid — even if the signature itself is technically valid. 
            # This guards against malformed tokens that might have a valid signature but are missing critical fields your app depends on.
        )

    # If everything checks out — valid signature, correct algorithm, not expired, has both required claims — jwt.decode()
    # returns the decoded payload as a dictionary (e.g. {"sub": "user123", "exp": 1719263400}
    except jwt.InvalidTokenError:
        return None # If anything goes wrong — bad signature, expired, missing required claims, malformed token — the function simply returns None
    else:
        # The else clause on a try/except runs only if the try block succeeded without raising an exception. 
        # Since jwt.decode() succeeded, payload is a valid dictionary, and the function extracts and returns the "sub" claim 
        # — the user ID that was embedded when the token was created.
        return payload.get("sub")



# When you inject oauth2_scheme into a route using Depends(), FastAPI automatically looks at the incoming request's HTTP headers. 
# It searches specifically for a header named Authorization and expects the value to follow the standard Bearer format: Authorization: Bearer <your_jwt_token_here>
# It strips away the word "Bearer " and extracts just the raw token string, passing it directly into your route function.
async def get_current_user(
    # token: extracted automatically by FastAPI via the oauth2_scheme dependency.
    # oauth2_scheme reads the "Authorization: Bearer <token>" header from the
    # incoming request and pulls out just the token string (the part after "Bearer ").
    # If the header is missing entirely, oauth2_scheme itself will raise a 401
    # before this function even runs.
    token: Annotated[str, Depends(oauth2_scheme)],

    # db: an active database session, injected by the get_db dependency.
    # FastAPI calls get_db(), which yields an AsyncSession, opens it for this
    # request, and will automatically close it after the request finishes
    # (success or failure) since get_db is a generator-based dependency.
    db: Annotated[AsyncSession, Depends(get_db)],

# Return type hint: this function either returns a fully-loaded User model
# instance, or raises an HTTPException (so it never actually returns None).
) -> models.User:

    # Decode and verify the JWT using our earlier verify_access_token function.
    # That function checks the signature, expiration, and required claims,
    # then returns the "sub" claim (the user ID as a string) if everything
    # checks out, or None if the token is invalid/expired/tampered with/missing claims.
    user_id = verify_access_token(token)

    # If verify_access_token returned None, the token failed validation in some way
    # (bad signature, expired, missing claims, etc.) — we don't know or care which,
    # we just treat it as "not authenticated."
    if user_id is None:
        raise HTTPException(
            # 401 Unauthorized: client did not provide valid credentials.
            status_code=status.HTTP_401_UNAUTHORIZED,
            # Generic message — deliberately vague, same security principle as
            # the login endpoint: don't give attackers clues about *why* it failed.
            detail="Invalid or expired token",
            # Tells the client which auth scheme to use when retrying
            # (part of the OAuth2/HTTP spec convention).
            headers={"WWW-Authenticate": "Bearer"},
        )

    # The "sub" claim was stored as a string when the token was created
    # (recall: data={"sub": str(user.id)} in create_access_token).
    # We need it back as an int to match the User model's id column type,
    # so we attempt to convert it here.
    try:
        user_id_int = int(user_id)
    # If user_id isn't a valid string representation of an integer
    # (e.g. it's None, or some unexpected non-numeric string),
    # int() will raise either TypeError or ValueError.
    except (TypeError, ValueError):
        raise HTTPException(
            # Treat a malformed "sub" claim the same as an invalid token overall —
            # again, same generic message, same status code, for consistency
            # and to avoid leaking implementation details.
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Query the database for a user whose id matches the one decoded from the token.
    # select(models.User) is SQLAlchemy's way of building a SELECT * FROM users query.
    # .where(models.User.id == user_id_int) adds a WHERE id = <user_id_int> clause.
    # await db.execute(...) actually runs the query asynchronously against the DB.
    result = await db.execute(
        select(models.User).where(models.User.id == user_id_int),
    )

    # .scalars() extracts the actual User objects from the raw result rows.
    # .first() grabs the first match, or None if no user has that id
    # (e.g. the user was deleted after the token was issued, but the token
    # itself is still technically valid/unexpired).
    user = result.scalars().first()

    # If no matching user was found in the database, reject the request —
    # a syntactically valid, correctly-signed token doesn't help if the
    # underlying user no longer exists.
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            # Slightly more specific message here, since at this point we know
            # the token itself was valid — it's specifically the user lookup
            # that failed. (Some teams might choose to keep this generic too,
            # depending on how strict they want to be about information leakage.)
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Everything checked out: valid signature, not expired, well-formed user id,
    # and a matching user exists in the database. Return the actual User model
    # instance — this becomes the value injected wherever this function is used
    # as a dependency (e.g. current_user: Annotated[models.User, Depends(get_current_user)]
    # in a protected route).
    return user

# This line creates a reusable type alias — it doesn't run any logic itself,
# it just gives a name to a commonly-used Annotated type so you don't have to repeat it everywhere
# Without the alias, every protected route would need to repeat the full, somewhat verbose type hint
CurrentUser = Annotated[models.User, Depends(get_current_user)]