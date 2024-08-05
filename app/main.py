from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .schema import schemas
from .models import models
from . import  crud, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todos/", response_model=schemas.ToDoItem)
def create_todo_item(todo_item: schemas.ToDoItemCreate, db: Session = Depends(get_db)):
    return crud.create_todo_item(db=db, todo_item=todo_item)

@app.get("/todos/", response_model=list[schemas.ToDoItem])
def read_todo_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_todo_items(db=db, skip=skip, limit=limit)

@app.get("/todos/{item_id}", response_model=schemas.ToDoItem)
def read_todo_item(item_id: int, db: Session = Depends(get_db)):
    db_todo_item = crud.get_todo_item(db=db, item_id=item_id)
    if db_todo_item is None:
        raise HTTPException(status_code=404, detail="ToDo item not found")
    return db_todo_item

@app.put("/todos/{item_id}", response_model=schemas.ToDoItem)
def update_todo_item(item_id: int, todo_item: schemas.ToDoItemUpdate, db: Session = Depends(get_db)):
    db_todo_item = crud.update_todo_item(db=db, item_id=item_id, todo_item=todo_item)
    if db_todo_item is None:
        raise HTTPException(status_code=404, detail="ToDo item not found")
    return db_todo_item

@app.delete("/todos/{item_id}", response_model=schemas.ToDoItem)
def delete_todo_item(item_id: int, db: Session = Depends(get_db)):
    if not crud.delete_todo_item(db=db, item_id=item_id):
        raise HTTPException(status_code=404, detail="ToDo item not found")
    return {"detail": "ToDo item deleted"}
 