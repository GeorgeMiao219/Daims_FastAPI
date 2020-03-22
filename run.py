if __name__ == "__main__":
    from uvicorn import run
    from config import uvicorn_logging_level as log_level
    run("app:app", host="127.0.0.1", port=8000, log_level=log_level, reload=True)
