# Article Scraper API

## 📌 Features

- ✅ Create and manage news sources (`/sources`)
- ✅ Trigger scraping from source websites using Selenium (`/sources/{id}/scrape`)
- ✅ Store scraped articles (`/articles`)
- ✅ Read/delete stored articles
- ✅ Auto timestamps for creation and scraping
- ✅ Swagger UI (`/docs`) and ReDoc (`/redoc`) documentation

---

## 🚀 Technologies Used

| Component   | Tech Stack                |
|-------------|---------------------------|
| Backend     | FastAPI                   |
| Database    | SQLModel + SQLite         |
| Scraper     | Selenium (headless Chrome)|
| Validation  | Pydantic                  |
| Server      | Uvicorn                   |
| ORM         | SQLAlchemy via SQLModel   |

## 🏗️ Project Structure

```
 ├── app/
 │ ├── api/
 │ ├── models/
 ├── services/
 │ └── main.py
 ├── tests/
 ├── requirements.txt
 ├── README.md
 └── pyproject.toml (if using Poetry)
```

---


### 🧪 Running the App

```bash
uvicorn app.main:app --reload
```

Visit:

- Swagger UI: http://localhost:8000/docs

- ReDoc: http://localhost:8000/redoc

### 📡 API Endpoints

📁 Sources

- `POST /sources` – Add a new source

- `GET /sources` – List all sources

- `GET /sources/{id}` – View specific source

- `POST /sources/{id}/scrape` – Scrape articles from source

📰 Articles

- `GET /articles` – List all articles

- `GET /articles/{id}` – View specific article

- `DELETE /articles/{id}` – Delete article

---

## 📊 Example Usage

### Add Source

#### `POST` /sources

``` json
{
  "name": "Quotes to Scrape",
  "url": "https://quotes.toscrape.com/"
}
```

`Status:` 200 OK

`Response:`
``` json
{
    "id": 1,
    "name": "Quotes to Scrape",
    "url": "https://quotes.toscrape.com/",
    "created_at": "2025-06-03T18:21:34.819095"
}
```

### Scrape Source

#### `POST` /sources/1/scrape

`Status:` 200 OK

`Response:`
``` json
{
    "message": "Scraping completed"
}
```
### Get Articles

#### `GET` /articles

`Status:` 200 OK

`Response:`
``` json
{
        "id": 1,
        "title": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
        "content": "Albert Einstein",
        "url": "https://quotes.toscrape.com/",
        "source_id": 2,
        "created_at": "2025-06-03T18:29:53.720042"
    },
    ...
        {
        "id": 10,
        "title": "“A day without sunshine is like, you know, night.”",
        "content": "Steve Martin",
        "url": "https://quotes.toscrape.com/",
        "source_id": 2,
        "created_at": "2025-06-03T18:29:54.052309"
    }
}
```

---

### 🐞 Known Issues

- Some websites may block headless scraping.
- Dynamic pages may require specific selectors.

---

### 👨‍💻 Author

- Igor Malkovskiy
- Email: 433garik433@gmail.com
- GitHub: Garikmal
