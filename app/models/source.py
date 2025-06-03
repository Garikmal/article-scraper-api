from sqlmodel import SQLModel, Field
from datetime import datetime

class Source(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    url: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
