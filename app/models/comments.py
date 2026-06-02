from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from app.database import Base

class CommentsTable(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String(200), nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    
    author = relationship("UsersTable", back_populates="comments")


    def __repr__(self) -> str:
        return f"Comment(id={self.id}, content='{self.content}', user_id={self.user_id})"
