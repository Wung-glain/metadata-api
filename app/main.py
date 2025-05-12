from fastapi import FastAPI

from app.api.v1.routes import metadata

app = FastAPI()
app.include_router(metadata.router)
