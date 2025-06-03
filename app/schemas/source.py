from pydantic import BaseModel, HttpUrl
from datetime import datetime

class SourceCreate(BaseModel):
    name: str
    url: HttpUrl

class SourceRead(BaseModel):
    id: int
    name: str
    url: HttpUrl
    created_at: datetime
