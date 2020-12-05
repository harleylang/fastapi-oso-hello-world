from pydantic import BaseModel

class User(BaseModel):
    username: str
    role: str # user or fbi
    hash: str