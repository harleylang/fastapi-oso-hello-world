import json

def put_data_in_class(data, obj):

    '''

    A helper function for converting a dictionary into a class.

    '''

    if type(data) is str:

        # from: https://stackoverflow.com/a/15882054/14198287
        return json.loads(data, object_hook=lambda d: obj(**d))

    elif type(data) is dict:

        return obj(**data) 

    else:

        raise TypeError('put_data_in_class did not receive data of type string or dict.')
