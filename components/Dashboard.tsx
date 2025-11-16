import React, { useState } from 'react';
import { usePythagorean } from '../hooks/usePythagorean';  // De fases previas
import NumerologyInput from './NumerologyInput';  // Subcomponente para inputs

const Dashboard: React.FC = () => {
  const [input, setInput] = useState('');  // Nombre
  const [fecha, setFecha] = useState('01/08/1959');
  const { vibracion, sendero } = usePythagorean(input + fecha.replace(/\//g, ''));  // Concat para reducción

  const handleCalcular = async () => {
    const vibFull = pythagoreanConvert(input + fecha.replace(/\//g, ''));
    const response = await fetch(`/calculo?nombre=${encodeURIComponent(input)}&fecha=${encodeURIComponent(fecha)}`);
    const data = await response.json();
    if (validateHolistic(vibFull, [data.sendero || 1])) {  // Corrobora
      // Actualiza estado o navega a /mapa con data
    } else {
      alert('Revelación Pendiente: Ajuste input para alineación Sephirot.');
    }
  };

  return (
    <div style={{ padding: '20px', backgroundColor: '#f0f8ff' }}>  // Estilo del HTML
      <h1>Dashboard Cabalístico</h1>
      <NumerologyInput value={input} onChange={setInput} placeholder="Nombre (No Hipocorísticos)" />
      <input type="text" value={fecha} onChange={e => setFecha(e.target.value)} placeholder="DD/MM/AAAA" style={{ /* ... */ }} />
      <button onClick={handleCalcular}>Calcular Sendero del Alma</button>
      {vibracion && <p>Vibración: {vibracion} - Sendero: {sendero} (Alineado: {validateHolistic(vibracion) ? 'Sí' : 'No'})</p>}
      <a href="/mapa">Explorar Mapa Interactivo</a>
    </div>
  );
};

export default Dashboard;
