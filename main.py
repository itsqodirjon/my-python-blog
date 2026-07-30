from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

posts_db = {
    1: {
        "title": "Linux Serverlarda Nginx Sozlash",
        "date": "2026-07-30",
        "category": "Linux",
        "content": "Nginx — bu yuqori unumdorlikka ega Web Server va Reverse Proxy hisoblanadi."
    }
}

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "posts": posts_db.values()
    })
