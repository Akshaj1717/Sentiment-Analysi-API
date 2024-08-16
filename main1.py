from fastapi import FastAPI
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI()
analyzer = SentimentIntensityAnalyzer()

@app.get("/")
def read_root():
    return {"message":"Welcome to the Sentiment Analysis API!"}

@app.post("/analyze/")
def analyze_sentiment(text: str):
    scores = analyzer.polarity_scores(text)
    sentiment = "positve" if scores['compound'] > 0 else "negative" if scores['compound'] < 0 else "neutral"
    return {"text": text, "sentiment": sentiment, "scores": scores}