from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.db import engine
from app.models.source import Source
from app.schemas.source import SourceCreate, SourceRead

router = APIRouter()

@router.post("/sources", response_model=SourceRead)
def create_source(source: SourceCreate):
    with Session(engine) as session:
        data = source.dict()
        data["url"] = str(source.url)
        db_source = Source(**data)
        session.add(db_source)
        session.commit()
        session.refresh(db_source)
        return db_source


@router.get("/sources", response_model=list[SourceRead])
def list_sources():
    with Session(engine) as session:
        statement = select(Source)
        results = session.exec(statement).all()
        return results

@router.get("/sources/{id}", response_model=SourceRead)
def get_source(id: int):
    with Session(engine) as session:
        source = session.get(Source, id)
        if not source:
            raise HTTPException(status_code=404, detail="Source not found")
        return source
