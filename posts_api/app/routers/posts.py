import models
import schemas
from fastapi import FastAPI, HTTPException, status, Response, Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(
    prefix = "/posts", tags = ['Posts']
)

@router.get("/", response_model = list[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    #cursor.execute("""SELECT * FROM posts """)
    #posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.CreatePost, db: Session = Depends(get_db)):
    #cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
    #posts = cursor.fetchone()
    #conn.commit()
    posts = models.Post(**post.model_dump())
    db.add(posts)
    db.commit()
    db.refresh(posts)

    return posts
    

@router.get("/{id}", response_model = schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):

    #cursor.execute("""SELECT * FROM posts WHERE id = %s """, (id,))
    #unp = cursor.fetchone()

    #if not unp:
    #    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    get_post = db.query(models.Post).filter(models.Post.id == id).first()

    if not get_post:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return get_post
    

@router.put("/{id}", response_model = schemas.Post)
def update_post(id: int, up_post: schemas.UpdatePost, db: Session = Depends(get_db)):

    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, id))
    
    # updated_post = cursor.fetchone()
    # conn.commit()

    posts = db.query(models.Post).filter(models.Post.id == id)

    updated_post = posts.first()
    
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    posts.update(up_post.model_dump(), synchronize_session=False)

    db.commit()
    
    return posts.first()

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):

    # cursor.execute("""DELETE FROM posts WHERE id = %s""", (id,))
    # post = cursor.fetchone()
    # conn.commit()

    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    post.delete(synchronize_session=False)

    db.commit()
    
    return {"data": "successfully deleted"}