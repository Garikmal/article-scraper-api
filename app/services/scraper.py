from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from app.models.article import Article
from datetime import datetime
from sqlmodel import Session
import time

def scrape_site(source, session: Session):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(source.url)
        time.sleep(2)

        quotes = driver.find_elements(By.CLASS_NAME, "quote")

        for quote in quotes:
            title = quote.find_element(By.CLASS_NAME, "text").text
            content = quote.find_element(By.CLASS_NAME, "author").text
            article = Article(
                title=title,
                content=content,
                url=source.url,
                source_id=source.id,
                created_at=datetime.utcnow()
            )
            session.add(article)

        session.commit()

    finally:
        driver.quit()
