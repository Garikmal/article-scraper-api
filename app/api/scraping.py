from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.db import get_session
from app.models.source import Source
from app.services.scraper import scrape_site

router = APIRouter()

@router.post("/sources/{source_id}/scrape")
def scrape_source(source_id: int, session: Session = Depends(get_session)):
    source = session.exec(select(Source).where(Source.id == source_id)).first()
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    scrape_site(source, session)
    return {"message": "Scraping completed"}
