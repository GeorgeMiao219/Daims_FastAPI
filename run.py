if __name__ == "__main__":
    from uvicorn import run
    run("app:app", host="0.0.0.0", port=8000, log_level="info", reload=True)