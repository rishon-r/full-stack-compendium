from datetime import UTC, datetime, timedelta
import jwt
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
from config import settings

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


