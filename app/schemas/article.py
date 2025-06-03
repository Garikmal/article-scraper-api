from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel
class ArticleRead(BaseModel):
    id: int
    title: str
    content: str
    url: str
    source_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class ArticleCreate(SQLModel):
    title: str
    content: str
    url: str
    source_id: Optional[int] = None
    created_at: Optional[datetime] = None
