import json
from tinydb import TinyDB, Query

db = TinyDB('./database.json')

"""
    Initialize JSON migration to database
"""
with open('../girias.json') as json_file:
    data = json.load(json_file)
    for slang in data["slang"]:
        if isinstance(slang["name"], list):
            print(slang["name"][0])
        else:
            print(slang["name"])
