from email.policy import HTTP
from typing import Optional
from fastapi import FastAPI, HTTPException, status, Response, Depends
from random import randrange
import psycopg
from utils import hash
from psycopg.rows import dict_row
import time
from sqlalchemy.orm import Session
from routers import posts, users, auth
import models
from database import engine

models.Base.metadata.create_all(engine)

app = FastAPI()

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

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)