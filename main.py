from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="DevOps Blog")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

user_profile = {
    "name": "Qodirjon",
    "role": "Junior DevOps Engineer",
    "bio": "Linux sistemalari, Docker va CI/CD bilan ishlaydigan mutaxassis.",
    "github": "https://github.com/itsqodirjon",
    "portfolio_url": "https://qodirjon.vercel.app"
}

posts_db = [
    {
        "id": 1,
        "title": "Linux Serverlarda Nginx Reverse Proxy Sozlash",
        "date": "2026-07-30",
        "category": "Linux",
        "summary": "Nginx orqali backend ilovalarni yo'naltirish va SSL sertifikat o'rnatish bo'yicha amaliy qo'llanma."
    },
    {
        "id": 2,
        "title": "Docker va Docker Compose Bilan FastAPI Loyihasini Konteynerlash",
        "date": "2026-07-29",
        "category": "Docker",
        "summary": "Python backend ilovalarini Docker environment ichida xavfsiz ko'tarish usullari."
    }
]

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "profile": user_profile,
        "posts": posts_db
    })
