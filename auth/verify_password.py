from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):

    '''

    Verify that the inputted-and-hashed password matches the saved password hash.

    From: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#check-the-password

    '''

    return pwd_context.verify(plain_password, hashed_password)
