from typing import List

import fastapi
from db.db_setup import get_db
from fastapi import Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic_schemas.course import Course, CourseCreate
from sqlalchemy.orm import Session

from api.utils.courses_queries import (
    create_course,
    delete_course,
    get_course,
    get_courses,
    update_course,
)

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


@router.get("/courses/{course_id}", response_model=Course)
async def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course


@router.patch("/courses/{course_id}", response_model=Course)
async def update_specified_course(
    course_id: int, course: CourseCreate, db: Session = Depends(get_db)
):
    return update_course(db=db, course_id=course_id, course=course)


@router.delete("/courses/{course_id}", status_code=204)
async def remove_course(course_id: int, db: Session = Depends(get_db)):
    return delete_course(db=db, course_id=course_id)


@router.get("/courses/{id}/sections")
async def read_course_sections():
    return {"courses": []}
