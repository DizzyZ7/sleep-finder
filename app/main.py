from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from parser import parse_all
from filters import apply_filters

app = FastAPI()

app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/api/products")
def products():

    return parse_all()


@app.get("/api/filter")
def filter_products(
    price:int=None,
    height:int=None,
    weight:int=None
):

    data = parse_all()

    return apply_filters(data,price,height,weight)
