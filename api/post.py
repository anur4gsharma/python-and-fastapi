from typing import Optional
from fastapi import FastAPI, HTTPException, status, Response
from pydantic import BaseModel
from random import randrange
import psycopg
from psycopg.rows import dict_row
import time

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

while True :
    try:
        conn = psycopg.connect(host = 'aws-0-ap-northeast-1.pooler.supabase.com', dbname = 'postgres', user = 'postgres.ibnsowjvyitjcvgoyvgw', password = 'Hnsa@2007Anu', row_factory = dict_row)
        cursor = conn.cursor()
        print("Database Connection Successful!")
        break

    except Exception as error:
        print("Connection Failed")
        print("Error : ", error)
        time.sleep(2)

my_posts: dict[int, dict] = {
    1: {"id": 1, "title": "title of post 1", "content": "content of post 1"},
    2: {"id": 2, "title": "foods", "content": "best food to try"}
}

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()
    return posts

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_id = randrange(0, 1000000)
    post_dict['id'] = post_id
    

    my_posts[post_id] = post_dict
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):

    if id not in my_posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return {"data": my_posts[id]}

@app.put("/posts/{id}")
def update_post(id: int, post: Post):

    if id not in my_posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    updated_post = post.model_dump()
    updated_post["id"] = id
    my_posts[id] = updated_post
    
    return {"data": my_posts[id]}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):

    if id not in my_posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    del my_posts[id]
    return