import React, { useState } from 'react';
import axios from 'axios';

function FileUpload({ setResults, setObservations, setPdfName, setError, setLoading }) {
    const [file, setFile] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
        setError('');
    };

    const handleUpload = async () => {
        if (!file) {
            setError('Por favor, selecciona un archivo PDF.');
            return;
        }
        setLoading(true);
        const formData = new FormData();
        formData.append('file', file);
        try {
            const response = await axios.post('http://localhost:5000/upload', formData);
            setResults(response.data.results);
            setObservations(response.data.observations);
            setPdfName(response.data.pdf_name);
            setError('');
        } catch (error) {
            setError('Error al subir el archivo. Verifica que el servidor esté corriendo.');
            console.error(error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="mb-8 bg-white p-8 rounded-lg shadow-lg transition-all duration-300 hover:shadow-xl">
            <h2 className="text-2xl font-semibold text-primary mb-6">Subir Tesis (PDF)</h2>
            <div className="flex flex-col items-center space-y-4">
                <label className="bg-primary text-white px-8 py-3 rounded-lg cursor-pointer hover:bg-blue-700 transition duration-200">
                    Seleccionar PDF
                    <input
                        type="file"
                        accept=".pdf"
                        onChange={handleFileChange}
                        className="hidden"
                    />
                </label>
                {file && <p className="text-secondary">{file.name}</p>}
                <button
                    onClick={handleUpload}
                    disabled={!file}
                    className="bg-accent text-white px-6 py-3 rounded-lg hover:bg-yellow-500 transition duration-200 disabled:bg-gray-400"
                >
                    Analizar PDF
                </button>
            </div>
        </div>
    );
}

export default FileUpload;