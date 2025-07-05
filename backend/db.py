from pymongo import MongoClient
from datetime import datetime


def get_db():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["tesis_analizador"]
        return db
    except Exception as e:
        print(f"Error conectando a MongoDB: {e}")
        raise


def save_consulta(pdf_name, results, observations, user_id):
    try:
        db = get_db()
        consultas = db["consultas"]
        consultas.insert_one({
            "pdf_name": pdf_name,
            "results": results,
            "observations": observations,
            "user_id": user_id,
            "timestamp": datetime.now()
        })
    except Exception as e:
        print(f"Error guardando consulta: {e}")
        raise


def save_pregunta(pdf_name, pregunta, respuesta, user_id):
    try:
        db = get_db()
        preguntas = db["preguntas"]
        preguntas.insert_one({
            "pdf_name": pdf_name,
            "pregunta": pregunta,
            "respuesta": respuesta,
            "user_id": user_id,
            "timestamp": datetime.now()
        })
    except Exception as e:
        print(f"Error guardando pregunta: {e}")
        raise
