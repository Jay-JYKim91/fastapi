from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange


from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


my_posts = [{
    "title": "title of post 1", "content": "content of post 1", "id":  1
},
    {
    "title": "title of post 2", "content": "content of post 2", "id":  2
}]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for index, post in enumerate(my_posts):
        if post["id"] == id:
            return index


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get('/')
def root():
    return {"message": "Hello World"}
