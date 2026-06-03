from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.auth import get_current_user
from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.schemas.user import User
from app.crud import task as crud_task

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/", response_model=List[Task])
def read_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud_task.get_tasks(db, user_id=current_user.id)

@router.post("/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud_task.create_task(db=db, task=task, user_id=current_user.id)

@router.patch("/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    updated_task = crud_task.update_task(db=db, task_id=task_id, task=task, user_id=current_user.id)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    success = crud_task.delete_task(db=db, task_id=task_id, user_id=current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
