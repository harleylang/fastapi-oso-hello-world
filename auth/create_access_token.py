from datetime import datetime, timedelta
from jose import JWTError, jwt
from auth.jwt_key_vars import jwt_key_vars

def create_access_token(username: str):

    ''' 

    Helper function for creating temporary bearer tokens.

    See: https://fastapi.tiangolo.com/tutorial/security/first-steps/

    '''
    
    expire = datetime.utcnow() + timedelta(minutes=5)

    jwt_data = {
        "username": username,
        "exp": expire
    }

    jwt_info = jwt_key_vars()

    encoded_jwt = jwt.encode(jwt_data, jwt_info['key'], algorithm=jwt_info['algo'])

    return encoded_jwt
