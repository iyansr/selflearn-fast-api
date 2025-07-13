from fastapi import HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from src.features.todo.models import Todo
from src.database import get_db
from src.features.todo.schema import AddTodo, TodoResponse, UpdateTodo

async def get_todos(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Todo))
    all_todos = result.scalars().all()
    return all_todos

async def get_todo(id: UUID, db: AsyncSession = Depends(get_db)) -> TodoResponse:
    result = await db.execute(select(Todo).filter(Todo.id == id))
    todo = result.scalar_one_or_none()
    
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

async def create_todo(todo: AddTodo, db: AsyncSession = Depends(get_db)):
    new_todo = Todo(title=todo.title, description=todo.description)
    db.add(new_todo)
    await db.commit()
    await db.refresh(new_todo)
    return new_todo

async def update_todo(id: UUID, todo: UpdateTodo, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Todo).filter(Todo.id == id))
    old_todo = result.scalar_one_or_none()
    
    if old_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    if todo.title is not None:
        old_todo.title = todo.title
    if todo.description is not None:
        old_todo.description = todo.description
    if todo.completed is not None:
        old_todo.completed = todo.completed
    
    await db.commit()
    await db.refresh(old_todo)
    return old_todo

async def delete_todo(id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Todo).filter(Todo.id == id))
    todo = result.scalar_one_or_none()
    
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    await db.delete(todo)
    await db.commit()
    return {"message": "Todo deleted successfully"}