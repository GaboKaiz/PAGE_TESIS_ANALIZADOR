import React, { useState } from 'react';
import axios from 'axios';

function FileUpload({ setResults, setObservations, setPdfName }) {
    const [file, setFile] = useState(null);
    const [uploading, setUploading] = useState(false);
    const [error, setError] = useState('');

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
        setError('');
    };

    const handleUpload = async () => {
        if (!file) {
            setError('Por favor, selecciona un archivo PDF.');
            return;
        }
        setUploading(true);
        const formData = new FormData();
        formData.append('file', file);
        try {
            const response = await axios.post('http://localhost:5000/upload', formData);
            setResults(response.data.results);
            setObservations(response.data.observations);
            setPdfName(file.name);
        } catch (error) {
            setError('Error al subir el archivo. Verifica que el servidor esté corriendo.');
            console.error(error);
        }
        setUploading(false);
    };

    return (
        <div className="mb-6">
            <h2 className="text-2xl font-semibold text-secondary mb-4">Subir Tesis (PDF)</h2>
            <input
                type="file"
                accept=".pdf"
                onChange={handleFileChange}
                className="mb-4 p-2 border rounded w-full"
            />
            <button
                onClick={handleUpload}
                disabled={uploading}
                className="bg-primary text-white px-4 py-2 rounded hover:bg-blue-700 disabled:bg-gray-400"
            >
                {uploading ? 'Subiendo...' : 'Subir PDF'}
            </button>
            {error && <p className="text-red-500 mt-2">{error}</p>}
        </div>
    );
}

export default FileUpload;