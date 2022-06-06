from typing import List

import fastapi
from db.db_setup import get_db
from fastapi import Depends, HTTPException
from pydantic_schemas.course import Course, CourseCreate
from sqlalchemy.orm import Session

from api.utils.courses_queries import create_course, get_courses

router = fastapi.APIRouter()


@router.get("/courses", response_model=List[Course])
async def read_courses(db: Session = Depends(get_db)):
    courses = get_courses(db=db)
    return courses


@router.post("/courses", response_model=Course)
async def create_new_course(
    course: CourseCreate, db: Session = Depends(get_db)
):
    return create_course(db=db, course=course)


@router.get("/courses/{id}")
async def read_course():
    return {"courses": []}


@router.patch("/courses/{id}")
async def update_course():
    return {"courses": []}


@router.delete("/courses/{id}")
async def delete_course():
    return {"courses": []}


@router.get("/courses/{id}/sections")
async def read_course_sections():
    return {"courses": []}
