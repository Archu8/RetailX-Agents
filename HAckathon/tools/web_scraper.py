import requests
from bs4 import BeautifulSoup

def fetch_competitor_prices(url):
    print(f"[WebScraper] Fetching data from {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    prices = []
    for item in soup.select(".product"):
        name = item.select_one(".name").text
        price = item.select_one(".price").text
        prices.append((name, price))
    return prices
