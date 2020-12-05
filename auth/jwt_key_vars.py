def jwt_key_vars():

    '''

    This is for the sake of example.

    Don't store secrets like this!

    '''

    # to get a string like this run:
    # openssl rand -hex 32

    return { 
        "key": "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7",
        "algo": "HS256"
    } 
