from typing import Optional
from fastapi import FastAPI, HTTPException, status, Response, Depends
from pydantic import BaseModel
from random import randrange
import psycopg
from psycopg.rows import dict_row
import time
import models
from database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(engine)

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

@app.get("/sqlalchemy")
def test_post(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()
    return posts

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
    posts = cursor.fetchone()
    conn.commit()
    posts
    return {"data": posts}
    

@app.get("/posts/{id}")
def get_post(id: int):

    cursor.execute("""SELECT * FROM posts WHERE id = %s """, (id,))
    unp = cursor.fetchone()

    if not unp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    return unp

@app.put("/posts/{id}")
def update_post(id: int, post: Post):

    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, id))
    
    updated_post = cursor.fetchone()
    conn.commit()
    
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    return {"data": updated_post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):

    cursor.execute("""DELETE FROM posts WHERE id = %s""", (id,))
    post = cursor.fetchone()
    conn.commit()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    return post