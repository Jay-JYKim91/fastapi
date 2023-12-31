from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{
    "title": "title of post 1", "content": "content of post 1", "id":  1
},
    {
    "title": "title of post 2", "content": "content of post 2", "id":  2
}]


@app.get('/')
def root():
    return {"message": "Hello World"}


@app.get('/posts')
def get_posts():
    return {"data": my_posts}


@app.post('/posts')
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000000)
    my_posts.append(post_dict)
    return {
        "data": post_dict
    }


@app.get('/posts/{id}')
def get_post(id):
    print(id)
    return {"post_detail": f"Here is post {id}"}
