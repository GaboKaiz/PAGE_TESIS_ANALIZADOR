import React from 'react';

function ResultsTable({ results, observations, pdfName }) {
    const handleExit = () => {
        window.location.reload();
    };

    return (
        <div className="mb-8 bg-white p-8 rounded-lg shadow-lg">
            <h2 className="text-2xl font-semibold text-primary mb-6">Resultados del Análisis</h2>
            <div className="overflow-x-auto">
                <table className="w-full border-collapse border border-gray-200 text-sm">
                    <thead>
                        <tr className="bg-primary text-white">
                            <th className="border border-gray-200 p-4 text-left font-medium">Campo</th>
                            <th className="border border-gray-200 p-4 text-left font-medium">Valor</th>
                        </tr>
                    </thead>
                    <tbody>
                        {Object.entries(results).map(([key, value]) => (
                            <tr key={key} className="hover:bg-gray-50 transition duration-200">
                                <td className="border border-gray-200 p-4 font-medium text-secondary">{key}</td>
                                <td className="border border-gray-200 p-4 text-secondary break-words">{value}</td>
                            </tr>
                        ))}
                        <tr className="bg-gray-100">
                            <td className="border border-gray-200 p-4 font-medium text-secondary">Observaciones</td>
                            <td className="border border-gray-200 p-4 text-secondary">
                                {observations.length > 0 ? (
                                    <ul className="list-disc pl-5 space-y-2">
                                        {observations.map((obs, index) => (
                                            <li key={index} className="mb-1">{obs}</li>
                                        ))}
                                    </ul>
                                ) : "No se encontraron observaciones."}
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div className="mt-6 flex justify-center space-x-4">
                <a
                    href={`http://localhost:5000/download_excel/${pdfName}`}
                    className="bg-accent text-white px-6 py-3 rounded-lg hover:bg-yellow-500 transition duration-200"
                >
                    Descargar Excel
                </a>
                <button
                    onClick={handleExit}
                    className="bg-error text-white px-6 py-3 rounded-lg hover:bg-red-700 transition duration-200"
                >
                    SALIR
                </button>
            </div>
        </div>
    );
}

export default ResultsTable;