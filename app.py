import logging
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

from url import url_api
from dns import dns_api
from database import DB
import config as cf

app = FastAPI()

logger = logging.getLogger("daims")
logger.setLevel(cf.logging_level)

try:
    db = DB.get_instance(cf.username, cf.password)
    logger.debug("Initializing Database service")
except Exception:
    logger.warning("Error while initializing Database service")


@app.get("/")
def home():
    return {"Hello": "FastAPI"}


app.include_router(url_api, tags=["URL"])
app.include_router(dns_api, tags=["DNS"], prefix="/DNS")
