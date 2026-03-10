from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from parser import parse_products
from filters import filter_products

app = FastAPI()

app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/api/products")
def products():

    return parse_products()

@app.get("/api/filter")
def filter_api(
    weight:int=None,
    height:int=None,
    price:int=None
):

    data = parse_products()

    result = filter_products(data, weight, height, price)

    return result
