from random import randrange
from typing import Optional
from fastapi import Body, FastAPI, Response ,status , HTTPException
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
        
def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i
        
@app.get("/")
def root():
    return {"message":"root dir"}

@app.get("/posts")
def get_post():
    return {"data":my_posts}
    
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post:Post):
    post_dict = post.dict()
    post_dict["id"]=randrange(0,10000000)
    my_posts.append(post_dict)
    return {"message": my_posts}


@app.get("/posts/latest")
def latest():
    post=my_posts[len(my_posts)-1]
    return {"message":post}

@app.get("/posts/{id}")
def get_post(id:int, response:Response):
    post = find_Post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found")
    return {"message":find_Post(id)}

@app.delete("/posts/{id}")
def delete_post(id:int):
    index=find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} doesnt exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int,post:Post):
    index=find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} doesnt exist")
    post_dict = post.dict()
    post_dict["id"]=id
    my_posts[index]=post_dict
    return {"message":post_dict}