from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.comment import Comment, CommentCreate
from app.crud import comment as crud_comment

router = APIRouter(prefix="/comment", tags=["comment"])

@router.get("/", response_model=List[Comment])
def read_comments(user_id: int = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_comment.get_comments(db, user_id=user_id, skip=skip, limit=limit)

@router.post("/", response_model=Comment)
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    # FIXME: Check if user exists before creating comment?
    return crud_comment.create_comment(db=db, comment=comment)
