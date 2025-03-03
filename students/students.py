from fastapi import APIRouter, HTTPException
from bson import ObjectId
from .database import students_collection
from .models import Student, StudentUpdate

router = APIRouter()


@router.post('/student-create')
def create_student(student: Student):
    student_data = student.model_dump()
    try:
        result = students_collection.insert_one(student_data)
        student_data["_id"] = str(result.inserted_id)
        return student_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
