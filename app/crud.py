from sqlalchemy.orm import Session
from .schema import schemas
from .models import models

def get_todo_item(db: Session, item_id: int):
    return db.query(models.ToDoItem).filter(models.ToDoItem.id == item_id).first()

def get_todo_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ToDoItem).offset(skip).limit(limit).all()

def create_todo_item(db: Session, todo_item: schemas.ToDoItemCreate):
    db_todo_item = models.ToDoItem(**todo_item.dict())
    db.add(db_todo_item)
    db.commit()
    db.refresh(db_todo_item)
    return db_todo_item

def update_todo_item(db: Session, item_id: int, todo_item: schemas.ToDoItemUpdate):
    db_todo_item = db.query(models.ToDoItem).filter(models.ToDoItem.id == item_id).first()
    if db_todo_item:
        db_todo_item.title = todo_item.title
        db_todo_item.description = todo_item.description
        db_todo_item.completed = todo_item.completed
        db.commit()
        db.refresh(db_todo_item)
        return db_todo_item
    return None

def delete_todo_item(db: Session, item_id: int):
    db_todo_item = db.query(models.ToDoItem).filter(models.ToDoItem.id == item_id).first()
    if db_todo_item:
        db.delete(db_todo_item)
        db.commit()
        return True
    return False
