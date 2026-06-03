from sqlalchemy.orm import Session
from app.models.tasks import TasksTable
from app.schemas.task import TaskCreate, TaskUpdate

def get_tasks(db: Session, user_id: int):
    return db.query(TasksTable).filter(TasksTable.owner_id == user_id).all()

def create_task(db: Session, task: TaskCreate, user_id: int):
    db_task = TasksTable(**task.model_dump(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task: TaskUpdate, user_id: int):
    db_task = db.query(TasksTable).filter(TasksTable.id == task_id, TasksTable.owner_id == user_id).first()
    if not db_task:
        return None
    
    update_data = task.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)
    
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int, user_id: int):
    db_task = db.query(TasksTable).filter(TasksTable.id == task_id, TasksTable.owner_id == user_id).first()
    if not db_task:
        return False
    db.delete(db_task)
    db.commit()
    return True
