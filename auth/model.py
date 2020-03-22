from pydantic import BaseModel


class User(BaseModel):
    uid: int
    username: str
    email: str
    hashed_password: str
    disabled: bool = False

