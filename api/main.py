from fastapi import FastAPI
from tinydb import TinyDB, Query
import json

db = TinyDB('database.json')
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
