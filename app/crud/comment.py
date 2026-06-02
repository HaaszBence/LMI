from sqlalchemy.orm import Session
from app.models.comments import CommentsTable
from app.schemas.comment import CommentCreate

def get_comments(db: Session, user_id: int = None, skip: int = 0, limit: int = 100):
    query = db.query(CommentsTable)
    if user_id is not None:
        query = query.filter(CommentsTable.user_id == user_id)
    return query.offset(skip).limit(limit).all()

def create_comment(db: Session, comment: CommentCreate):
    db_comment = CommentsTable(content=comment.content, user_id=comment.user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
