from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title : str
    content : str
    published : bool =True
    rating : Optional[int]=None

@app.get("/")
def root():
    return {"message":"Welcome to root!!!"}

@app.get("/posts")
def get_post():
    return {"message":"here are posts"}
    
@app.post("/posts")
def create_post(post:Post):
    print(post.published)
    print(post.rating)
    return {"message": post}