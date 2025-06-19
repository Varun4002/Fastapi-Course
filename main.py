from random import randrange
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title : str
    content : str
    published : bool =True
    rating : Optional[int]=None


my_posts = [{"title":"title of post 1","content":"content of post 1","id":1},
            {"title":"i love pizza","content":"hey i love pizza","id":2}]

def find_Post(id):
    for p in my_posts:
        if p["id"]==id:
            return p

@app.get("/")
def root():
    return {"message":"root dir"}

@app.get("/posts")
def get_post():
    return {"data":my_posts}
    
@app.post("/posts")
def create_post(post:Post):
    post_dict = post.dict()
    post_dict["id"]=randrange(0,10000000)
    my_posts.append(post_dict)
    return {"message": my_posts}

@app.get("/posts/{id}")
def get_post(id:int):
    print(find_Post(id))
    return {"message":find_Post(id)}

