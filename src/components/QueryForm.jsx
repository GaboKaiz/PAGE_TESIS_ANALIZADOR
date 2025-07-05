import React, { useState } from 'react';
import axios from 'axios';

function QueryForm({ pdfName }) {
    const [pregunta, setPregunta] = useState('');
    const [respuesta, setRespuesta] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async () => {
        if (!pregunta) {
            setError('Por favor, escribe una pregunta.');
            return;
        }
        try {
            const response = await axios.post('http://localhost:5000/query', {
                pdf_name: pdfName,
                pregunta,
            }, {
                headers: { 'Content-Type': 'application/json' }
            });
            setRespuesta(response.data.respuesta);
            setError('');
            setPregunta('');
        } catch (error) {
            setError('Error al procesar la pregunta. Verifica que el servidor esté corriendo y el PDF exista.');
            console.error('Error en QueryForm:', error.response || error.message);
        }
    };

    return (
        <div className="mb-8 bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-2xl font-semibold text-primary mb-6">Preguntar sobre el PDF</h2>
            <textarea
                value={pregunta}
                onChange={(e) => setPregunta(e.target.value)}
                placeholder="Escribe tu pregunta (ej. ¿Quién es el estudiante que lo realizó? ¿Quiénes son los jurados?)"
                className="w-full p-4 border border-gray-200 rounded-lg mb-6 resize-y focus:outline-none focus:ring-2 focus:ring-primary"
            />
            <button
                onClick={handleSubmit}
                className="bg-primary text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition duration-200"
            >
                Enviar Pregunta
            </button>
            {respuesta && (
                <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                    <p className="text-secondary"><strong>Respuesta:</strong> {respuesta}</p>
                </div>
            )}
            {error && <p className="text-error mt-4 text-center">{error}</p>}
        </div>
    );
}

export default QueryForm;