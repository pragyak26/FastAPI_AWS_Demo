from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="My First API")


class Task(BaseModel):
    title: str
    completed: bool = False


@app.get("/")
def home():
    return {"message": "FastAPI is working!"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/tasks")
def create_task(task: Task):
    return {"message": "Task created", "task": task}