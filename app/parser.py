import requests
from bs4 import BeautifulSoup

URL = "https://askona.ru/matrasy"

def parse_products():

    r = requests.get(URL)
    soup = BeautifulSoup(r.text,"html.parser")

    products = []

    cards = soup.select(".product-card")

    for c in cards:

        try:
            name = c.select_one(".product-title").text.strip()
            price = c.select_one(".price").text.strip()
        except:
            continue

        products.append({
            "name": name,
            "price": price,
            "height": 20,
            "firmness": "medium",
            "max_weight": 120,
            "size": "160x200",
            "category": "mattress"
        })

    return products
