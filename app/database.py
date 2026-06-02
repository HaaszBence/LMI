import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Use /app/data for Docker, or local root for development
DATABASE_DIR = "/app/data" if os.path.exists("/app/data") else "."
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_DIR}/sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
