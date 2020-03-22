from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
import config as cf
from database import DB
from utils import Singleton

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


@Singleton
class AuthController:  # TODO
    def __init__(self):
        self.db = DB.get_instance(cf.username, cf.password)

    def get_current_user(self, token: str):
        pass