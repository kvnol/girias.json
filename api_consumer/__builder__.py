import json
from tinydb import TinyDB, Query

db = TinyDB('./database.json')
table = db.table('slangs')

"""
    Initialize JSON migration to database
"""
def run():
    with open('../girias.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for slang in data["slang"]:
            for nSlang in normalize(slang):
                print(nSlang)
                table.insert(nSlang)

"""
    Normalize slang to database insert
"""
def normalize(data):
    if isinstance(data["name"], list):
        for name in data["name"]:
            yield {
                **data,
                "name": name
            }

    yield data

if __name__ == "__main__":
    run()