A brief tutorial for integrating `oso` logic into a `FastAPI` application.

# Python Installation Requirements

```
sudo pip3 install oso FastAPI passlib[bcrypt] python-jose[cryptography]
```

# Explore

Before getting started, read the following documentation:
* [oso Quickstart Guide](https://docs.osohq.com/getting-started/quickstart.html)
* [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
* [FastAPI Security Chapter](https://fastapi.tiangolo.com/tutorial/security/)

Comments are left throughout `main.py` to guide you through the application's logic.

This application is written with the assumption that it is being passed query params and/or data through the response body.

Policies are defined in `auth.polar`

Authentication logic is modelled from the FastAPI Security Chapter (see link above) is abstracted to the '/auth' folder.

To test the various API calls are their results, open your terminal and perform the following commands: 

```

# change directory
cd /path/to/this/directory

# spin up FastAPI
bash spin.sh

# In your browser, navigate to: 127.0.0.1:1337/docs
# Through the FastAPI swagger UI, you can test the various example API calls for their results.
# Next, read each route defined in main.py to explore oso + FastAPI functionality.
# When a route header label is clicked through the FastAPI swagger UI, the comments from main.py will be displayed for each corresponding route. 

```


