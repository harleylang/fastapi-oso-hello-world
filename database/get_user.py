import json

def get_user(username: str):

    '''

    This is a helper function that returns 'user' data.

    The 'user' objects are pulled from the data-users.json file in the root directory.

    If you wish to test this with your active database, be sure to:
    - (1) Replace 'data-users.json' calls below with calls to your own database, and
    - (2) Update the 'User.py' file in '/sometypes' according to your data structure.

    '''

    with open('data-users.json') as json_file: # get mock db entries
        data = json.load(json_file)

    try: # use generator to identify and return user obj
        user = next(data[obj] for obj in data if data[obj]['username'] == username)
        return user
    except StopIteration:
        return None # parent functions should raise exception if there is no user 
