from typing import List, Optional

import fastapi
from db.db_setup import get_db
from fastapi import Depends, HTTPException
from pydantic import BaseModel
from pydantic_schemas.user import User, UserCreate
from sqlalchemy.orm import Session

from api.utils.users_query import get_users

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users")
async def create_user(user: User):
    return "Success"


@router.get("/users/{id}")
async def get_user(id: int):
    return {}
