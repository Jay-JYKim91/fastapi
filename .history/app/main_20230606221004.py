from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth
from pydantic import BaseSettings


class Settings(BaseSettings):
    database_password: str
    database_username: str
    secret_key: str


settings = Settings()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get('/')
def root():
    return {"message": "Hello World"}
