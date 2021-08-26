from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from leia import SentimentIntensityAnalyzer

app = FastAPI()

def get_polarity_score(text):
    analyzer = SentimentIntensityAnalyzer()
    polarity_score = analyzer.polarity_scores(text)['compound']
    return polarity_score


templates = Jinja2Templates(directory="templates")

@app.get("/index", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/sentiment-score", response_class=HTMLResponse)
def sentiment_score(request: Request, phrase: str = Form(...)):
    return templates.TemplateResponse("response.html", {"request": request, 
                                                        "phrase": phrase,
                                                        "sentiment_score": get_polarity_score(phrase)})
