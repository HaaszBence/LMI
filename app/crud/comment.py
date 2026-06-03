from sqlalchemy.orm import Session, joinedload
from app.models.comments import CommentsTable
from app.schemas.comment import CommentCreate

def get_comments(db: Session, user_id: int|None = None, skip: int|None = None, limit: int|None = None):
    query = db.query(CommentsTable).options(joinedload(CommentsTable.author))
    if user_id is not None:
        query = query.filter(CommentsTable.user_id == user_id)
    if limit is not None:
        query = query.limit(limit)
    if skip is not None:
        query = query.offset(skip)
    return query.all()

def create_comment(db: Session, comment: CommentCreate):
    db_comment = CommentsTable(content=comment.content, user_id=comment.user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
