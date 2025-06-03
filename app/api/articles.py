from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.db import engine
from app.models.article import Article
from app.schemas.article import ArticleRead, ArticleCreate

router = APIRouter()

@router.get("/articles", response_model=list[ArticleRead])
def list_articles():
    with Session(engine) as session:
        statement = select(Article)
        results = session.exec(statement).all()
        return results

@router.get("/articles/{id}", response_model=ArticleRead)
def get_article(id: int):
    with Session(engine) as session:
        article = session.get(Article, id)
        if not article:
            raise HTTPException(status_code=404, detail="Article not found")
        return article

@router.delete("/articles/{id}")
def delete_article(id: int):
    with Session(engine) as session:
        article = session.get(Article, id)
        if not article:
            raise HTTPException(status_code=404, detail="Article not found")
        session.delete(article)
        session.commit()
        return {"Article deleted": id}
