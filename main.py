"""FastAPI"""
from fastapi import FastAPI #pylint: disable=E0401

app = FastAPI()

todos = []

@app.get("/")
async def root():
    """
    Root method: init
    """
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Method to return specific item_id data
    """
    return {"item_id": item_id}

@app.post("/items/{item_id}")
async def post_item(item_id: int):
    """
    Method to post items
    """
    todos.append(item_id)
    return {"message": f"item: {item_id} added to list"}

@app.post("/items/")    
async def get_item():
    """
    Method to post items
    """
    return {"items": todos}
