from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from vader import SentimentScore
from mangum import Mangum


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/sentiment-form", response_class=HTMLResponse)
def sentiment_form(request: Request):
    return templates.TemplateResponse("sentiment/form.html", {"request": request})


@app.post("/sentiment-score", response_class=HTMLResponse)
def sentiment_score(request: Request, phrase: str = Form(...)):
    return templates.TemplateResponse("sentiment/response.html", {"request": request, 
                                                                  "phrase": phrase,
                                                                  "sentiment_score": SentimentScore.get(phrase)})


handler = Mangum(app=app)
