import React from 'react';
function App() {
  const otd = {TO: 1, PT: 8, TD: 14};
  const cpData = {14: {freq: 4, decomp: 'P41 Servicio'}};
  const laminaCP = Array.from({length: 100}, (_, i) => ({
    num: i + 10,
    freq: cpData[i + 10]?.freq || 0,
    visual: '|'.repeat(cpData[i + 10]?.freq || 0),
    decomp: cpData[i + 10]?.decomp || 'N/A'
  }));
  const sumaOtd = otd.TO + otd.PT + otd.TD;
  return (
    <div>
      <h2>Panel A: Senderos OTD</h2>
      <table>
        <thead><tr><th>Sendero</th><th>Valor</th><th>Arcano</th><th>Función</th></tr></thead>
        <tbody>
          <tr><td>TO</td><td>{otd.TO}</td><td>El Mago</td><td>Base Unidad Voluntad</td></tr>
          <tr><td>PT</td><td>{otd.PT}</td><td>La Justicia</td><td>Transición Fuerza Misión</td></tr>
          <tr><td>TD</td><td>{otd.TD}</td><td>La Templanza</td><td>Misión Servicio Armonía</td></tr>
        </tbody>
      </table>
      <p>Suma OTD: {sumaOtd} → {sumaOtd % 9 || 9} (Corrobora TD=14 → 5)</p>
      <h2>Panel C: CP Lámina Repetidos 10-109</h2>
      <div style={{display: 'grid', gridTemplateColumns: 'repeat(10, 1fr)', gap: '1px', background: '#ddd', margin: '10px 0'}}>
        {laminaCP.map(cell => (
          <div key={cell.num} style={{padding: '5px', border: '1px solid #ccc', textAlign: 'center', cursor: 'pointer', background: cell.freq >= 4 ? 'red' : 'white', color: cell.freq >= 4 ? 'white' : 'black'}}
            onClick={() => alert(`CP ${cell.num}: Freq ${cell.freq} Visual ${cell.visual} Decomp ${cell.decomp}`)}
          >
            {cell.num} {cell.visual}
          </div>
        ))}
      </div>
    </div>
  );
}
export default App;
