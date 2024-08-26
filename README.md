# 🌟 ToDo API

## 📖 Overview
Welcome to the **ToDo API** project! This API, built with **FastAPI**, **SQLAlchemy**, and **Pydantic**, allows users to manage ToDo items efficiently. You can create, read, update, and delete tasks through a simple interface.

---

## 🛠️ Requirements
To run this project, ensure you have **Python** installed. Follow the steps below to set up your environment:

### Step 1: Create a Virtual Environment
```bash
python -m venv venv
```

### Step 2: Activate the Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt 
```

## ⚙️ Setup
Before starting the API, configure your database connection. Modify the `database.py` file to connect to your desired database (e.g., SQLite, PostgreSQL).

### Example of `database.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # Update with your database URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

## 📡 API Endpoints

### Create a ToDo Item
- **Method:** POST
- **Endpoint:** `/todos/`
- **Request Body:** `ToDoItemCreate`
- **Response:** `ToDoItem`
- **Description:** Creates a new ToDo item.

### Read All ToDo Items
- **Method:** GET
- **Endpoint:** `/todos/`
- **Query Parameters:**
  - `skip`: Number of items to skip (default: 0)
  - `limit`: Number of items to return (default: 10)
- **Response:** `List[ToDoItem]`
- **Description:** Retrieves a list of ToDo items.

### Read a Single ToDo Item
- **Method:** GET
- **Endpoint:** `/todos/{item_id}`
- **Response:** `ToDoItem`
- **Description:** Retrieves a specific ToDo item by ID.

### Update a ToDo Item
- **Method:** PUT
- **Endpoint:** `/todos/{item_id}`
- **Request Body:** `ToDoItemUpdate`
- **Response:** `ToDoItem`
- **Description:** Updates an existing ToDo item.

### Delete a ToDo Item
- **Method:** DELETE
- **Endpoint:** `/todos/{item_id}`
- **Response:** `{"detail": "ToDo item deleted"}`
- **Description:** Deletes a specific ToDo item by ID.

## 📝 Example Requests

### Create ToDo Item
```bash
curl -X POST "http://127.0.0.1:8000/todos/" -H "Content-Type: application/json" -d '{"title": "Sample Task", "description": "This is a sample task"}'
```
### Get All ToDo Items

```bash
curl -X GET "http://127.0.0.1:8000/todos/"
```
### Get ToDo Item by ID
```bash 
curl -X GET "http://127.0.0.1:8000/todos/1"
```

### Update ToDo Item

```bash 
curl -X PUT "http://127.0.0.1:8000/todos/1" -H "Content-Type: application/json" -d '{"title": "Updated Task", "completed": true}'
```

### Delete ToDo Item

```bash 
curl -X DELETE "http://127.0.0.1:8000/todos/1"
```

## 🚀 Running the Application
To run the FastAPI application, use Uvicorn:

```bash 
uvicorn main:app --reload
```
## 🎉 Conclusion 
This ToDo API serves as a foundational structure for managing tasks. It can be easily extended with additional features such as user authentication and task categorization. We hope you enjoy using this API!