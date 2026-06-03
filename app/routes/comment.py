from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.comment import Comment, CommentCreate
from app.crud import comment as crud_comment
from app.crud import user as crud_user

router = APIRouter(prefix="/comment", tags=["comment"])

@router.get("/", response_model=List[Comment])
def read_comments(user_id: int = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_comment.get_comments(db, user_id=user_id, skip=skip, limit=limit)

@router.post("/", response_model=Comment)
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user_id=comment.user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found. Cannot post comment.")
    return crud_comment.create_comment(db=db, comment=comment)
