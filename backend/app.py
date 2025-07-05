from flask import Flask, request, jsonify
from flask_cors import CORS
from pdf_processor import process_pdf, process_query
from db import save_consulta, save_pregunta
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/upload", methods=["POST"])
def upload_pdf():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    if file and file.filename.endswith(".pdf"):
        pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(pdf_path)
        results, observations = process_pdf(pdf_path)
        save_consulta(file.filename, results, observations, "user_id_placeholder")
        return jsonify({"results": results, "observations": observations, "pdf_name": file.filename})
    return jsonify({"error": "Invalid file format"}), 400


@app.route("/query", methods=["POST"])
def query_pdf():
    try:
        data = request.get_json()
        pdf_name = data.get("pdf_name")
        pregunta = data.get("pregunta")
        if not pdf_name or not pregunta:
            return jsonify({"error": "Faltan pdf_name o pregunta"}), 400
        respuesta = process_query(pdf_name, pregunta)
        save_pregunta(pdf_name, pregunta, respuesta, "user_id_placeholder")
        return jsonify({"respuesta": respuesta})
    except Exception as e:
        print(f"Error en /query: {e}")
        return jsonify({"error": f"Error procesando la pregunta: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
