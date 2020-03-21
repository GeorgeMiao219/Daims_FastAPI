from fastapi import APIRouter

dns_api = APIRouter()


@dns_api.get("/{prefix}")
async def get_dns(prefix: str):
    return {"prefix": prefix, "url": "TODO"}  # TODO


@dns_api.post("/{prefix}")
async def post_dns(prefix: str, url: str):
    return {"prefix": prefix, "url": url}


@dns_api.put("/{prefix}")
async def get_dns(prefix: str, url: str):
    return {"prefix": prefix, "url": url}  # TODO


@dns_api.delete("/{prefix}")
async def get_dns(prefix: str):
    return {"prefix": prefix, "url": "TODO"}  # TODO
