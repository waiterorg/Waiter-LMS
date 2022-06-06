from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from pydantic_schemas.course import Course
from api.utils.courses import get_courses

router = fastapi.APIRouter()


@router.get("/courses", response_model=List[Course])
async def read_courses(db: Session = Depends(get_db)):
    courses = get_courses(db=db)
    return courses


@router.post("/courses")
async def create_course_api():
    return {"courses": []}


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
