from datetime import datetime, timedelta
from jose import JWTError, jwt

from passlib.context import CryptContext
SECRET_KEY = "itmysecuritykey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 135


