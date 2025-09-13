from fastapi import FastAPI, status

app = FastAPI(version="github-v0.1.1", title="Github API", description="Github API")


@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    """Represents a hello message to users."""
    return {"message": "Welcome to Github deployment with CI/CD pipeline"}


@app.get("/health", status_code=status.HTTP_200_OK)
async def healthcheck():
    """Return value can help us to be sure about service's healthy.
    If return value is 'OK', fastapi service is running successfully.
    """
    return {"status": "OK"}
