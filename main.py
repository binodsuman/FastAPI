from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/")
async def root():
    #return 'Demo starting here '
    return {"message": "Hello World from FastAPI!"}

@app.get("/home")
async def root():
    return 'This is home page '
    # return {"message": "Hello World from FastAPI!"}

# Path Parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Query Parameters
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# http://localhost:8000/items/?skip=20&limit=100


# Post Request Body
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# Post Request Body
@app.post("/items/")
async def create_item(item: Item):
    item.name = item.name + " - modified"
    item.description = item.description + " - modified" if item.description else "No description provided"
    item.price = item.price * 1.1  # Example modification: increase price by 10%
    if item.tax:
        item.tax = item.tax * 1.05
    return {"item": item}


@app.get("/items2/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
# q isoptional here, if not provided it will return all items

# Form input 
from fastapi import Form


import sys
print(f"Python version: {sys.version}")

from typing import Annotated
from fastapi import FastAPI, Form



@app.get("/login/")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()]
):
    return {"username": username, "password": password}