from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body

app = FastAPI()

class Student(BaseModel):
    name: str
    interests: str
    degree: str
    age: int
    about: Optional[str] = None
    student: bool = True

students = []

@app.get("/")
def home():
    return {"message": "this is home"}

@app.get("/about")
def about():
    return {"about": "this is our students"}

@app.get("/students")
def get_students():
    return students
    

@app.post("/students/posts")
def post_student(student: Student):
    students.append(student)
    print("After:", students)
    return student