"""
amazon.com/create-user
GET - GET AN INFORMATION
POST - CREATE SOMETHING NEW
PUT - UPDATE
DELETE - DELETE SOMETHING
"""
### Installation and Creating your first API
### Path Parameters

from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1 : {
        "name" : "john",
        "age" : 17,
        "class" : "year 12"
    }
}

class Student(BaseModel):
    name : str
    age : int
    year : str

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None


@app.get("/")
def index():
    return {"name":"First Data"}

# uvicorn main:app --reload

@app.get("/get-student/{student_id}")
def get_student(
        student_id : int = Path(
        description = "The ID of the student you want to view",
        gt = 0,
        lt=3)
):
    return students[student_id]

# google.com/get-student/1
# gt = greater than, lt = less than, ge = greater or equal, le = less or eqaul
# google.com/results?search=Python

### Query Paramters
### Combining Path and Query Parameters

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id : int, name : Optional[str]=None, test:int):
    for student_id in students:
        if students[student_id]["name"] == name :
            return students[student_id]
    return {"Data" : "Not found"}

### Request Body and The Post Method
@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students :
        return {"Error": "Student exists"}

    students[student_id] = student
    return students[student_id]

### Put Method
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):

    if student_id not in students:
        return {"Error" : "Student does not exist"}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    # students[student_id] = student
    return students[student_id]

#### Delete Method

@app.delete("/delete-student/{student_id}")
def delete_student(student_id : int):
    if student_id not in students:
        return {"Error" : "Student does not exist"}

    del students[student_id]
    return {"Message" : "Student deleted sucessfully"}