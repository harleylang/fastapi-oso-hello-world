from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from auth.jwt_key_vars import jwt_key_vars
from database.get_user import get_user
from sometypes.TokenData import TokenData
from sometypes.User import User
from utils.put_data_in_class import put_data_in_class

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):

    '''

    This function decrypts a user's bearer token and returns the
    user who originally requested the token.

    To read more about the design of this auth arcitecture, see the FastAPI security chapter:
    https://fastapi.tiangolo.com/tutorial/security/

    '''

    # 0) setup exception

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid_token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # 1) decode jwt

    jwt_info = jwt_key_vars()

    try:
        payload = jwt.decode(token, jwt_info['key'], algorithms=[jwt_info['algo']])
        username: str = payload.get("username")
        if username is None:
            raise exception
        token_data = TokenData(username=username)
    except JWTError:
        raise exception

    # 2) get user information from db

    user_json = get_user(username) 

    if user_json is None: # user does not exist
        raise exception

    user = put_data_in_class(user_json, User)

    return user
