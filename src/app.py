from fastapi import FastAPI
from contextlib import asynccontextmanager


from fastapi.middleware.cors import CORSMiddleware
from src.features.todo.router import router as todo_router
from src.database import create_tables, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(todo_router)
