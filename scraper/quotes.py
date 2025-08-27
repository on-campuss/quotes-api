import requests
from bs4 import BeautifulSoup

def fetch_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("span", class_="text")
    return [quote.text for quote in quotes]