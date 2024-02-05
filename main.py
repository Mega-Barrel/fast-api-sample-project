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
