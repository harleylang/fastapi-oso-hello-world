import json

def get_messages():

    '''

    This is a helper function that returns 'messages'.

    The 'messages' objects are pulled from the data-messages.json file in the root directory.

    If you wish to test this with your active database, be sure to:
    - (1) Replace 'data-messages.json' calls below with calls to your own database, and
    - (2) Update the 'Content.py' file in '/sometypes' according to your data structure.

    '''

    with open('data-messages.json') as json_file:
        data = json.load(json_file)

    return data 

