from logging import getLogger
from fastapi import APIRouter, HTTPException, Depends
from .controller import URLController
from auth import oauth2_scheme

url_api = APIRouter()
uc = URLController.get_instance()
logger = getLogger("daims")


@url_api.get("/{mapping_str}")
def get_url(mapping_str: str):
    result = uc.get(mapping_str)
    if result["url"]:
        result["mapping_str"] = mapping_str
        return result
    else:
        raise HTTPException(status_code=404, detail=f"{mapping_str} not found")


@url_api.post("/{url}")
def post_url(url: str, token: str = Depends(oauth2_scheme)):
    result = uc.post(url)
    if result[0]:
        return {"rid": result[0], "mapping_str": result[1], "url": result[2]}
    else:
        raise HTTPException(500, detail=f"Failed to post {url} due to {result[1]}")


@url_api.put("/{mapping_str}")
def put_url(mapping_str: str, url: str, token: str = Depends(oauth2_scheme)):
    try:
        uc.put(mapping_str)
        return {"mapping_str": mapping_str, "url": url}  # TODO
    except Exception:
        raise HTTPException(500, detail=f"Failed to update {mapping_str}")


@url_api.delete("/{mapping_str}")
def delete_url(mapping_str: str, token: str = Depends(oauth2_scheme)):
    try:
        return {"mapping_str": mapping_str, "is_successful": uc.delete(mapping_str)}
    except Exception as e:
        raise HTTPException(500, detail=f"Failed to delete {mapping_str} due to {e}")
