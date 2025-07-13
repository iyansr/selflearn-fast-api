from sqlalchemy import  String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base
from uuid import uuid4, UUID

class Todo(Base):
    __tablename__ = "todos"
    
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    title: Mapped[str] = mapped_column(String, index=True, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)

    