from typing import Union # Especifica que una variable o parametro puede tomar diferentes tipos de datos

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # se crea una instancia 

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# Definir rutas

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

