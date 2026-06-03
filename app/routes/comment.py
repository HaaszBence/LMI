from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.comment import Comment, CommentCreate
from app.schemas.user import User as UserSchema
from app.crud import comment as crud_comment
from app.auth import get_current_user

router = APIRouter(prefix="/comment", tags=["comment"])

@router.get("/", response_model=List[Comment])
def read_comments(user_id: int = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_comment.get_comments(db, user_id=user_id, skip=skip, limit=limit)

@router.post("/", response_model=Comment)
def create_comment(
    comment: CommentCreate, 
    db: Session = Depends(get_db),
    current_user: UserSchema = Depends(get_current_user)
):
    # Override user_id from the authenticated user
    comment.user_id = current_user.id
    return crud_comment.create_comment(db=db, comment=comment)
