from fastapi import FastAPI
from scraper.quotes import fetch_quotes

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/quotes")
async def get_quotes():
    return {"quotes": fetch_quotes()}

@app.get("/quotes/{id}")
def get_quotes_by_id(id: int):
    quotes = fetch_quotes()
    return {"quote": quotes[id]}


