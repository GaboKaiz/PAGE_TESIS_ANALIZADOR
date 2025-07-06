import React, { useState } from 'react';
import axios from 'axios';

function QueryForm({ pdfName }) {
    const [pregunta, setPregunta] = useState('');
    const [respuesta, setRespuesta] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = async () => {
        if (!pregunta) {
            setError('Por favor, escribe una pregunta.');
            return;
        }
        setLoading(true);
        setError('');
        setRespuesta('');
        try {
            const response = await axios.post('http://localhost:5000/query', {
                pdf_name: pdfName,
                pregunta,
            }, {
                headers: { 'Content-Type': 'application/json' }
            });
            setRespuesta(response.data.respuesta);
            setPregunta('');
        } catch (error) {
            setError('Error al procesar la pregunta. Verifica que el servidor esté corriendo y el PDF exista.');
            console.error('Error en QueryForm:', error.response || error.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="mb-8 bg-white p-8 rounded-lg shadow-lg">
            <h2 className="text-2xl font-semibold text-primary mb-6">Preguntar sobre el PDF</h2>
            <textarea
                value={pregunta}
                onChange={(e) => setPregunta(e.target.value)}
                placeholder="Escribe tu pregunta (ej. ¿Quién es el estudiante que lo realizó? ¿Quiénes son los jurados?)"
                className={`w-full p-4 border border-gray-200 rounded-lg mb-6 resize-y focus:outline-none focus:ring-2 focus:ring-primary ${loading ? 'bg-gray-100 cursor-not-allowed' : ''
                    }`}
                disabled={loading}
            />
            <button
                onClick={handleSubmit}
                disabled={loading}
                className={`px-6 py-3 rounded-lg text-white font-semibold transition duration-200 ${loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-primary hover:bg-blue-700'
                    }`}
            >
                {loading ? 'Cargando...' : 'Enviar Pregunta'}
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