import React, { useState } from 'react';
import axios from 'axios';
import ResultsTable from './components/ResultsTable';
import QueryForm from './components/QueryForm';

function App() {
  const [results, setResults] = useState(null);
  const [observations, setObservations] = useState([]);
  const [pdfName, setPdfName] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:5000/upload', formData);
      setResults(response.data.results);
      setObservations(response.data.observations);
      setPdfName(response.data.pdf_name);
      setError('');
    } catch (err) {
      setError('Error al procesar el PDF. Verifica que el servidor esté corriendo.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-background flex flex-col items-center">
      <div className="w-full max-w-4xl px-4 py-8">
        {/* Overlay de cargando */}
        {loading && (
          <div className="fixed inset-0 bg-gray-900 bg-opacity-50 flex items-center justify-center z-50">
            <div className="bg-white p-6 rounded-lg shadow-lg flex items-center space-x-4">
              <svg
                className="animate-spin h-6 w-6 text-primary"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                ></circle>
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                ></path>
              </svg>
              <p className="text-lg text-secondary">Cargando...</p>
            </div>
          </div>
        )}

        {/* Sección de subida de archivo */}
        <div className="mb-8 bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-2xl font-semibold text-primary mb-6">Subir PDF</h2>
          <div className="flex justify-center">
            <label className="bg-primary text-white px-8 py-3 rounded-lg cursor-pointer hover:bg-blue-700 transition duration-200">
              Seleccionar PDF
              <input
                type="file"
                accept="application/pdf"
                onChange={handleFileUpload}
                className="hidden"
              />
            </label>
          </div>
          {error && <p className="text-error mt-4 text-center">{error}</p>}
        </div>

        {/* Resultados */}
        {results && <ResultsTable results={results} observations={observations} />}

        {/* Formulario de preguntas */}
        {pdfName && <QueryForm pdfName={pdfName} />}
      </div>
    </div>
  );
}

export default App;