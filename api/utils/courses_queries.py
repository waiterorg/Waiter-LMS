from db.models.course import Course
from fastapi import HTTPException, status
from pydantic_schemas.course import CourseCreate
from sqlalchemy.orm import Session


def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


def get_courses(db: Session):
    return db.query(Course).all()


def get_user_courses(db: Session, user_id: int):
    courses = db.query(Course).filter(Course.user_id == user_id).all()
    return courses


def create_course(db: Session, course: CourseCreate):
    db_course = Course(
        title=course.title,
        description=course.description,
        user_id=course.user_id,
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def update_course(db: Session, course_id: int, course: CourseCreate):
    db_course = get_course(db, course_id)
    if not db_course:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail="Course not found"
        )
    update_data = course.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_course, key, value)

    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def delete_course(db: Session, course_id: int):
    db_course = get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail="Course not found"
        )
    db.delete(db_course)
    db.commit()
    return db_course
