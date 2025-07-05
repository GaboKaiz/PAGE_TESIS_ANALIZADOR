from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["tesis_analizador"]
    print("Colecciones:", db.list_collection_names())
except Exception as e:
    print("Error:", e)
