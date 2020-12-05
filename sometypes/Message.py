from pydantic import BaseModel

class Message(BaseModel):
    sent_from: str
    sent_to: str
    msg: str