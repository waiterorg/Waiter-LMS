from typing import List, Optional

import fastapi
from db.db_setup import get_db
from fastapi import Depends, HTTPException
from pydantic import BaseModel
from pydantic_schemas.user import User, UserCreate
from sqlalchemy.orm import Session

from api.utils.users_query import create_user, get_user_by_email, get_users

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Email is already registered"
        )
    return create_user(db=db, user=user)


@router.get("/users/{id}")
async def get_user(id: int):
    return {}
