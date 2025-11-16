import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { usePythagorean } from '../hooks/usePythagorean';  // Hook de fases previas
import { pythagoreanConvert, validateHolistic } from '../utils/pythagorean';  // Incluye fecha reducción
import { MiniMapPreview } from './MiniMapPreview';  // Nuevo subcomponente para preview

const Dashboard: React.FC = () => {
  const [nombre, setNombre] = useState('');
  const [fecha, setFecha] = useState('01/08/1959');
  const navigate = useNavigate();
  const vibNombre = usePythagorean(nombre).vibracion || 0;
  const vibFecha = pythagoreanConvert(fecha.replace(/\//g, ''));  // DDMMAAAA → suma → reduc. 1-22
  const isAligned = validateHolistic(vibNombre, [vibFecha]);  // Corroboración simple

  const handleCalcular = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!nombre || nombre.length < 4) return alert('Nombre inválido: Use normas no hipocorísticas.');
    const vibFull = (vibNombre + vibFecha) % 22 || 22;  // Combinación holística
    if (!isAligned) return alert('Desarmonía Detectada: Ajuste fecha para afinidad Sephirot (>95%).');
    
    try {
      const response = await fetch(`/calculo?nombre=${encodeURIComponent(nombre)}&fecha=${encodeURIComponent(fecha)}`, {
        headers: { Authorization: `Bearer ${localStorage.getItem('jwt')}` }  // Si backend requiere
      });
      const data = await response.json();  // {vibracion: 8, sendero: 'Hod', tikun: '...'}
      if (data.vibracion) {
        navigate('/mapa', { state: { ...data, holistica: true } });
      }
    } catch (error) {
      console.error('Error Cálculo:', error);  // Fallback mock si backend no listo
      navigate('/mapa', { state: { vibracion: vibFull, sendero: `Sephira ${vibFull}` } });
    }
  };

  return (
    <div style={{ backgroundColor: '#f0f8ff', minHeight: '100vh', padding: '20px', fontFamily: 'Arial' }}>
      <header style={{ backgroundColor: '#8B008B', color: 'white', padding: '10px', textAlign: 'center' }}>
        <h1>🍇 Portal del Sendero del Alma</h1>
      </header>
      <main style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', flexDirection: 'column' }}>
        <div style={{ backgroundColor: 'white', padding: '30px', borderRadius: '8px', boxShadow: '0 4px 6px rgba(0,0,0,0.1)', maxWidth: '500px', width: '100%' }}>
          <h2 style={{ textAlign: 'center', color: '#8B008B' }}>Cálculo Cabalístico</h2>
          <form onSubmit={handleCalcular}>
            <label style={{ display: 'block', marginBottom: '5px' }}>Nombre (Normas No Hipocorísticas):</label>
            <input
              type="text"
              value={nombre}
              onChange={(e) => setNombre(e.target.value.toUpperCase().replace(/[^A-Z\s]/g, ''))}  // Limpieza Pitagórica
              placeholder="Ej: JUAN"
              style={{ width: '100%', padding: '12px', marginBottom: '15px', border: '1px solid #ccc', borderRadius: '4px' }}
              required
            />
            <label style={{ display: 'block', marginBottom: '5px' }}>Fecha (DD/MM/AAAA):</label>
            <input
              type="text"
              value={fecha}
              onChange={(e) => setFecha(e.target.value)}
              placeholder="01/08/1959"
              style={{ width: '100%', padding: '12px', marginBottom: '15px', border: '1px solid #ccc', borderRadius: '4px' }}
              required
            />
            <button type="submit" style={{ width: '100%', padding: '12px', backgroundColor: '#4CAF50', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>
              Calcular Sendero del Alma
            </button>
          </form>
          {vibNombre > 0 && (
            <div style={{ marginTop: '20px', padding: '10px', backgroundColor: isAligned ? '#d4edda' : '#f8d7da', borderRadius: '4px' }}>
              <p><strong>Vibración Nombre:</strong> {vibNombre} ({mapVibToSendero(vibNombre)})</p>
              <p><strong>Vibración Fecha:</strong> {vibFecha}</p>
              <p><strong>Alineación Holística:</strong> {isAligned ? 'Armonizada (95%+)' : 'Pendiente Ajuste'}</p>
              <MiniMapPreview vibracion={vibNombre} />  {/* Preview Sephira */}
            </div>
          )}
        </div>
      </main>
    </div>
  );
};

// Helper: Mapeo canónico (expande a 22 Senderos)
function mapVibToSendero(vib: number): string {
  const sephirot = ['Kether', 'Chokmah', 'Binah', 'Chesed', 'Geburah', 'Tiphareth', 'Netzach', 'Hod', 'Yesod', 'Malkuth'];
  return sephirot[vib - 1] || 'Equilibrio Divino';
}

export default Dashboard;
