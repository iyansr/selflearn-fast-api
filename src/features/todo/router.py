
from fastapi import APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from src.features.todo.service import get_todos, get_todo, update_todo, delete_todo
from src.database import get_db
from src.features.todo.schema import AddTodo, UpdateTodo
from src.features.todo.service import create_todo

router = APIRouter(
    tags=["Todo"],
    prefix="/todos",
)

@router.get("/")
async def get_todos_handler(db: AsyncSession = Depends(get_db)):
    return await get_todos(db)

@router.get("/{id}")
async def get_todo_handler(id: UUID, db: AsyncSession = Depends(get_db)):
    return await get_todo(id, db)

@router.post("/")
async def create_todo_handler(todo: AddTodo, db: AsyncSession = Depends(get_db)):
    return await create_todo(todo, db)


@router.put("/{id}")
async def update_todo_handler(id: UUID, todo: UpdateTodo, db: AsyncSession = Depends(get_db)):
    return await update_todo(id, todo, db)

@router.delete("/{id}")
async def delete_todo_handler(id: UUID, db: AsyncSession = Depends(get_db)):
    return await delete_todo(id, db)