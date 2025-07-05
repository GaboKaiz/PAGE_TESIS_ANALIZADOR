import pdfplumber
import pytesseract
from PIL import Image
import io
import re
import os


def process_pdf(pdf_path):
    results = {
        "Marca temporal": "",
        "Dirección de correo electrónico": "",
        "Título de la tesis": "",
        "Link de la tesis": "",
        "Asesor": "",
        "Jurado 1": "",
        "Jurado 2": "",
        "Jurado 3": "",
        "Lugar": "",
        "Quienes (Sujetos de estudio)": "",
        "Variable dependiente": "",
        "Variable independiente": "",
        "Enfoque": "",
        "Nivel o alcance": "",
        "Diseño de investigación": "",
        "Problema general": "",
        "Problema específico 1": "",
        "Problema específico 2": "",
        "Problema específico 3": "",
        "Problema específico 4": "",
        "Objetivo general": "",
        "Objetivo específico 1": "",
        "Objetivo específico 2": "",
        "Objetivo específico 3": "",
        "Objetivo específico 4": "",
        "Hipótesis general": "",
        "Hipótesis específica 1": "",
        "Hipótesis específica 2": "",
        "Hipótesis específica 3": "",
        "Hipótesis específica 4": "",
        "Línea de investigación": "",
        "Descripción de la población": "",
        "Cantidad de la población": "",
        "Cantidad de la muestra": "",
        "Prueba estadística": "",
        "Fecha de publicación": "",
        "Tipo de observación": "",
        "Detalle de la observación": "",
        "Número de página de la observación": ""
    }
    observations = []

    # Extraer texto e imágenes del PDF
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Extraer texto
            page_text = page.extract_text() or ""
            text += page_text + "\n"
            # Extraer imágenes y procesar con OCR
            for img in page.images:
                try:
                    img_data = img['stream'].get_data()
                    image = Image.open(io.BytesIO(img_data))
                    ocr_text = pytesseract.image_to_string(image, lang='spa')
                    text += ocr_text + "\n"
                except Exception as e:
                    observations.append(f"Error al procesar imagen en página {page.page_number}: {str(e)}")

    # Extraer campos con expresiones regulares
    results["Título de la tesis"] = extract_field(text, r"(?i)(titulo|título):\s*(.+?)(?=\n|$)", "No identificado")
    results["Asesor"] = extract_field(text, r"(?i)(asesor|advisor):\s*(.+?)(?=\n|$)", "No identificado")
    results["Jurado 1"] = extract_field(text, r"(?i)(jurado 1|primer jurado):\s*(.+?)(?=\n|$)", "No identificado")
    results["Jurado 2"] = extract_field(text, r"(?i)(jurado 2|segundo jurado):\s*(.+?)(?=\n|$)", "No identificado")
    results["Jurado 3"] = extract_field(text, r"(?i)(jurado 3|tercer jurado):\s*(.+?)(?=\n|$)", "No identificado")
    results["Lugar"] = extract_field(text, r"(?i)(lugar|ubicación):\s*(.+?)(?=\n|$)", "Tingo María, Perú" if "Tingo María" in text else "No identificado")
    results["Quienes (Sujetos de estudio)"] = extract_field(text, r"(?i)(sujetos de estudio|población):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Variable dependiente"] = extract_field(text, r"(?i)(variable dependiente):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Variable independiente"] = extract_field(text, r"(?i)(variable independiente):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Enfoque"] = extract_field(text, r"(?i)(enfoque):\s*(.+?)(?=\n|$)", "No identificado")
    results["Nivel o alcance"] = extract_field(text, r"(?i)(nivel o alcance|alcance):\s*(.+?)(?=\n|$)", "No identificado")
    results["Diseño de investigación"] = extract_field(text, r"(?i)(diseño de investigación):\s*(.+?)(?=\n|$)", "No identificado")
    results["Problema general"] = extract_field(text, r"(?i)(problema general):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Problema específico 1"] = extract_field(text, r"(?i)(problema específico 1|problema especifico 1):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Problema específico 2"] = extract_field(text, r"(?i)(problema específico 2|problema especifico 2):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Problema específico 3"] = extract_field(text, r"(?i)(problema específico 3|problema especifico 3):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Problema específico 4"] = extract_field(text, r"(?i)(problema específico 4|problema especifico 4):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Objetivo general"] = extract_field(text, r"(?i)(objetivo general):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Objetivo específico 1"] = extract_field(text, r"(?i)(objetivo específico 1|objetivo especifico 1):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Objetivo específico 2"] = extract_field(text, r"(?i)(objetivo específico 2|objetivo especifico 2):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Objetivo específico 3"] = extract_field(text, r"(?i)(objetivo específico 3|objetivo especifico 3):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Objetivo específico 4"] = extract_field(text, r"(?i)(objetivo específico 4|objetivo especifico 4):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Hipótesis general"] = extract_field(text, r"(?i)(hipótesis general|hipotesis general):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Hipótesis específica 1"] = extract_field(text, r"(?i)(hipótesis específica 1|hipotesis especifica 1):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Hipótesis específica 2"] = extract_field(text, r"(?i)(hipótesis específica 2|hipotesis especifica 2):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Hipótesis específica 3"] = extract_field(text, r"(?i)(hipótesis específica 3|hipotesis especifica 3):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Hipótesis específica 4"] = extract_field(text, r"(?i)(hipótesis específica 4|hipotesis especifica 4):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Línea de investigación"] = extract_field(text, r"(?i)(línea de investigación|linea de investigacion):\s*(.+?)(?=\n|$)", "No identificado")
    results["Descripción de la población"] = extract_field(text, r"(?i)(descripción de la población|descripcion de la poblacion):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Cantidad de la población"] = extract_field(text, r"(?i)(cantidad de la población|cantidad de la poblacion):\s*(.+?)(?=\n|$)", "No identificado")
    results["Cantidad de la muestra"] = extract_field(text, r"(?i)(cantidad de la muestra|cantidad de la muestra):\s*(.+?)(?=\n|$)", "No identificado")
    results["Prueba estadística"] = extract_field(text, r"(?i)(prueba estadística|prueba estadistica):\s*(.+?)(?=\n|$)", "No identificado")
    results["Fecha de publicación"] = extract_field(text, r"(?i)(fecha de publicación|fecha de publicacion):\s*(.+?)(?=\n|$)", "No identificado")
    results["Tipo de observación"] = extract_field(text, r"(?i)(tipo de observación|tipo de observacion):\s*(.+?)(?=\n|$)", "No identificado")
    results["Detalle de la observación"] = extract_field(text, r"(?i)(detalle de la observación|detalle de la observacion):\s*(.+?)(?=\n\n|$)", "No identificado")
    results["Número de página de la observación"] = extract_field(text, r"(?i)(número de página de la observación|numero de pagina de la observacion):\s*(.+?)(?=\n|$)", "No identificado")

    # Generar observaciones
    if "retaso" in text.lower():
        observations.append("Error ortográfico: 'retaso' debería ser 'retraso'.")
    if "escaza" in text.lower():
        observations.append("Error ortográfico: 'escaza' debería ser 'escasa'.")
    if not results["Variable dependiente"]:
        observations.append("No se identificó la variable dependiente.")
    if not results["Variable independiente"]:
        observations.append("No se identificó la variable independiente.")
    if not results["Descripción de la población"]:
        observations.append("No se encontró una descripción clara de la población.")
    if not results["Prueba estadística"]:
        observations.append("No se especificó la prueba estadística utilizada.")

    return results, observations


def extract_field(text, pattern, default):
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(2).strip()[:500] if match else default


def process_query(pdf_name, pregunta):
    try:
        text = ""
        with pdfplumber.open(f"uploads/{pdf_name}") as pdf:
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                text += page_text + "\n"
                for img in page.images:
                    img_data = img['stream'].get_data()
                    image = Image.open(io.BytesIO(img_data))
                    ocr_text = pytesseract.image_to_string(image, lang='spa')
                    text += ocr_text + "\n"

        # Buscar respuesta según la pregunta
        if "estudiante" in pregunta.lower() or "autor" in pregunta.lower():
            match = re.search(r"(?i)(autor|estudiante|alumno):\s*(.+?)(?=\n|$)", text)
            return f"El estudiante que realizó la tesis es: {match.group(2) if match else 'No identificado'}"
        elif "asesor" in pregunta.lower():
            match = re.search(r"(?i)(asesor|advisor):\s*(.+?)(?=\n|$)", text)
            return f"El asesor de la tesis es: {match.group(2) if match else 'No identificado'}"
        elif "jurado" in pregunta.lower():
            jurors = []
            for i in range(1, 4):
                match = re.search(rf"(?i)(jurado {i}|{'primer' if i==1 else 'segundo' if i==2 else 'tercer'} jurado):\s*(.+?)(?=\n|$)", text)
                jurors.append(match.group(2) if match else "No identificado")
            return f"Los jurados son: Jurado 1: {jurors[0]}, Jurado 2: {jurors[1]}, Jurado 3: {jurors[2]}"
        else:
            # Búsqueda general en el texto
            sentences = text.split('\n')
            for sentence in sentences:
                if pregunta.lower() in sentence.lower():
                    return sentence[:500]
            return f"No se encontró información relevante para la pregunta '{pregunta}'"
    except Exception as e:
        return f"Error al procesar la pregunta: {str(e)}"
