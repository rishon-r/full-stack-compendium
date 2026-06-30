from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# The config file defines what settings our application needs
# However, the actual values for these settings are loaded from the .env file
# In the .env file, environment variables are defined with the same name as fields in the setting class (this is however case insensitive)
# Everything in the .env file will also be in plain text but Pydantic will handle these type conversions implicitly
# Remember to add the .env file to .gitignore and never commit the environment variables to source control as this results in a major security risk


class Settings(BaseSettings): # Settings class inherits from BaseSettings which comes from pydantic_settings
  model_config = SettingsConfigDict(
    env_file = ".env", # Model config tells it to automatically load values from a .env file. The .env file is for storing sensitive configuration info
    env_file_encoding="utf-8"
  )

  secret_key: SecretStr # SecretStr is a special type that won't leak the string value when we print it out or write it in logs
  # We usually generate a secret key in the terminal before adding it to our environment variables
  # Terminal command to generate secret key: python -c "import secrets; print(secrets.token_hex(32))"
  algorithm: str = "HS256" # HS256 is the standard algorithm for JSON Web Tokens
  access_token_expires_minutes: int = 30 # In 30 minutes the access token will expire

  max_upload_size_butes: int = 5 * 1024 * 1024 # 5MB is the maximum upload size

settings = Settings() # This loads everything from the .env file when the model is imported