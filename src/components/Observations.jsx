import React from 'react';

function Observations({ observations }) {
    return (
        <div className="mb-6">
            <h2 className="text-2xl font-semibold text-secondary mb-4">Observaciones</h2>
            <ul className="list-disc pl-6">
                {observations.map((obs, index) => (
                    <li key={index} className="text-gray-700">{obs}</li>
                ))}
            </ul>
        </div>
    );
}

export default Observations;