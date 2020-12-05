from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from oso import Oso
from typing import Optional

from auth.authenticate_user import authenticate_user
from auth.create_access_token import create_access_token
from auth.get_current_user import get_current_user

from database.get_messages import get_messages
from database.get_user import get_user

from sometypes.Message import Message
from sometypes.Token import Token
from sometypes.User import User

from utils.put_data_in_class import put_data_in_class

# setup

app = FastAPI()
oso = Oso()

# load policies

oso.register_class(Message)
oso.register_class(User)
oso.load_file('auth.polar')

# routes

@app.get("/") 
def root(name: Optional[str] = None):
    '''
        An example "Hello world" FastAPI route. To test:
        (1) In your preferred browser, go to 'localhost:1337/docs' 
        (2) Click 'GET /'.
        (3) In the dropdown card, click the 'Try it out' to the top right.
        (4) Click the large blue 'Execute' button that appears.
        (5) The json result appears under the 'Responses' header.
    '''
    return { "Hello": "World" }

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    '''
        Create temporary bearer tokens on login.

        To generate a token:
        - (1) Run `sudo bash spin.sh`
        - (2) In your preferred browser, go to 'localhost:1337/docs'
        - (3) Click the 'Authorize' button.
        - (4) Enter any of the following test user/pass pairs:

        Example user/password pairs for testing FastAPI authentication:
        - "johndoe"     /   "secret"
        - "waldo"       /   "secret"
        - "agentk"      /   "mib"
        - "agentj"      /   "mib"

        To see the effect of authentication on api routes, try:
        - (1) Executing an API call on 'localhost:1337/docs' without being loggedin,
            - Notice that the '/messages*' call, for example, is replying with "Not authenticated"
        - (2) Next, executing an API call on 'localhost:1337:docs' WITH different logins
            - Notice that the '/messages*' call, for example, is replying with all data
    '''
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(user.username)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/profile_without_authorization")
def messages_without_authorization(account: str, user: User = Depends(get_current_user)):
    '''
    Returns a user profile.

    This route requires authentication but NOT authorization.
    '''
    account_json = get_user(account)
    return { "data": account_json }

@app.get("/profile_with_authorization")
def messages_with_authorization(account: str, user: User = Depends(get_current_user)):
    '''
    Returns a user profile.

    This route requires authentication AND authorization.

    Notice how you can only access the profile of the user who is currently logged in.
    '''
    account_json = get_user(account)
    account = put_data_in_class(account_json, User)
    if oso.is_allowed(user, "read", account):
        return { "data" : account_json }
    else:
        return HTTPException(status_code=404, detail="invalid_role")

@app.get("/messages_without_authorization")
def messages_without_authorization(user: User = Depends(get_current_user)):
    '''
    Returns a user's messages.

    This route requires authentication but NOT authorization.
    '''
    messages = []
    all_messages = get_messages()
    for m in all_messages:
        message = all_messages[m]
        messages.append(message)
    return { "data": messages }

@app.get("/messages_with_authorization")
def messages_with_authorization(user: User = Depends(get_current_user)):
    '''
    Returns a user's messages.

    This route requires authentication AND authorization.

    Notice how if you are johndoe or waldo, you do not see the message from agentj.
    '''
    messages = []
    all_messages = get_messages()
    for m in all_messages:
        message = all_messages[m]
        message = put_data_in_class(message, Message)
        if oso.is_allowed(user, "read", message):
            messages.append(message)
    return { "data": messages }
