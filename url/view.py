from fastapi import APIRouter

url_api = APIRouter()


@url_api.get("/{mapping_str}")
def get_url(mapping_str: str):
    return {"mapping_str": mapping_str, "url": "TODO"}  # TODO


@url_api.post("/{url}")
def post_url(url: str):
    return {"mapping_str": "TODO", "url": url}  # TODO


@url_api.put("/{mapping_str}")
def put_url(mapping_str: str, url: str):
    return {"mapping_str": mapping_str, "url": url}  # TODO


@url_api.delete("/{mapping_str}")
def delete_url(mapping_str: str, url: str):
    return {"mapping_str": mapping_str, "url": url}  # TODO
