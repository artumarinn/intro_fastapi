from fastapi import FastAPI

app = FastAPI()

"""
@app.get("/") # path, tambien se puede utilizar con otros metodos como: post, update, delete, option, head, etc
async def root():
    return {"message": "Hello World"}"
"""

# Parametros de ruta - Path Parameters
"""
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
"""
# Parametros de ruta con tipos - Path Parameters with types

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id} 

# Orden de las rutas

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

