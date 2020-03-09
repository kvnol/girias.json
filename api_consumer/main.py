from fastapi import FastAPI
from tinydb import TinyDB, Query
import json

db = TinyDB('database.json')
table = db.table('slangs')
app = FastAPI()

@app.get("/")
def list(page: int = 0, search: str = None):
    if search:
        Slang = Query()
        data = table.search(Slang.name == search)[page*10:page*10 + 10]
    else: 
        data = db.all()[page*10:page*10 + 10]

    return {
        "data": data,
        "page": page
    }
