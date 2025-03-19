from fastapi import FastAPI

app = FastAPI()

"""
@app.get("/") # path, tambien se puede utilizar con otros metodos como: post, update, delete, option, head, etc
async def root():
    return {"message": "Hello World"}"
"""

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}