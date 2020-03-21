from fastapi import FastAPI

from url import url_api
from dns import dns_api

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "FastAPI"}


app.include_router(url_api, tags=["URL"])
app.include_router(dns_api, tags=["DNS"], prefix="/DNS")
