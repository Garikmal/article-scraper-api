from sqlmodel import SQLModel, Field
from datetime import datetime

class Article(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    content: str
    url: str
    source_id: int = Field(foreign_key="source.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

