from sqlalchemy.orm import Session
from app.models.users import UsersTable
from app.schemas.user import UserCreate
from app.auth import get_password_hash

def get_user(db: Session, user_id: int):
    return db.query(UsersTable).filter(UsersTable.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(UsersTable).filter(UsersTable.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    # TODO: Add sorting options (asc/desc)
    return db.query(UsersTable).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = UsersTable(
        name=user.name, 
        email=user.email, 
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
