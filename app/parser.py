import requests
from bs4 import BeautifulSoup

BASE = "https://askona.ru"

CATEGORIES = [
    "/matrasy",
    "/krovati",
    "/podushki",
]

def parse_category(path):

    url = BASE + path

    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")

    items = []

    cards = soup.select(".product-card")

    for c in cards:

        try:
            name = c.select_one(".product-title").text.strip()
            price = c.select_one(".price").text.strip()
            link = BASE + c.select_one("a")["href"]
            image = c.select_one("img")["src"]
        except:
            continue

        items.append({
            "name": name,
            "price": price,
            "link": link,
            "image": image,
            "height": 20,
            "firmness": "medium",
            "max_weight": 120,
            "size": "160x200",
            "category": path.replace("/","")
        })

    return items


def parse_all():

    products = []

    for c in CATEGORIES:

        products += parse_category(c)

    return products
