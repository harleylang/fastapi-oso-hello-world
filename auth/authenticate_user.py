from auth.verify_password import verify_password
from database.get_user import get_user
from sometypes.User import User
from utils.put_data_in_class import put_data_in_class

def authenticate_user(username: str, password: str):

    '''

    Verify that the provided user/password combo are legit.

    From: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#get-the-username-and-password

    '''

    user_json = get_user(username)

    if user_json is None:
    
        return False

    user = put_data_in_class(user_json, User)

    if not verify_password(password, user.hash):
    
        return False
    
    return user
