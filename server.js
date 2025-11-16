const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors({origin: '*'}));
app.use(express.json());
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <title>Dashboard Cabalístico</title>
      <style>
        body { font-family: Arial; background: #f0f8ff; padding: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        .grid-cp { display: grid; grid-template-columns: repeat(10, 1fr); gap: 1px; background: #ddd; margin: 10px 0; }
        .cell-cp { padding: 5px; border: 1px solid #ccc; text-align: center; cursor: pointer; }
        .alta { background: red; color: white; }
      </style>
    </head>
    <body>
      <h1>¡Árbol Vivo! Dashboard Cabalístico Listo. TO=1 Mago Unidad</h1>
      <div id="root"></div>
      <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
      <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
      <script>
        const {useState} = React;
        function App() {
          const otd = {TO: 1, PT: 8, TD: 14};
          const cpData = {14: {freq: 4, decomp: 'P41 Servicio'}};
          const laminaCP = Array.from({length: 100}, (_, i) => ({
            num: i + 10,
            freq: cpData[i + 10]?.freq || 0,
            visual: '|'.repeat(cpData[i + 10]?.freq || 0),
            decomp: cpData[i + 10]?.decomp || 'N/A'
          }));
          const sumaOtd = otd.TO + otd.PT + otd.TD; // 23 → 5 corrobora TD=14 → 5
          return React.createElement('div', null,
            React.createElement('h2', null, 'Panel A: Senderos OTD'),
            React.createElement('table', null,
              React.createElement('thead', null,
                React.createElement('tr', null,
                  React.createElement('th', null, 'Sendero'),
                  React.createElement('th', null, 'Valor'),
                  React.createElement('th', null, 'Arcano'),
                  React.createElement('th', null, 'Función')
                )
              ),
              React.createElement('tbody', null,
                React.createElement('tr', null,
                  React.createElement('td', null, 'TO'),
                  React.createElement('td', null, otd.TO),
                  React.createElement('td', null, 'El Mago'),
                  React.createElement('td', null, 'Base Unidad Voluntad')
                ),
                React.createElement('tr', null,
                  React.createElement('td', null, 'PT'),
                  React.createElement('td', null, otd.PT),
                  React.createElement('td', null, 'La Justicia'),
                  React.createElement('td', null, 'Transición Fuerza Misión')
                ),
                React.createElement('tr', null,
                  React.createElement('td', null, 'TD'),
                  React.createElement('td', null, otd.TD),
                  React.createElement('td', null, 'La Templanza'),
                  React.createElement('td', null, 'Misión Servicio Armonía')
                )
              )
            ),
            React.createElement('p', null, `Suma OTD: ${sumaOtd} → ${sumaOtd % 9 || 9} (Corrobora TD=14 → 5)`),
            React.createElement('h2', null, 'Panel C: CP Lámina Repetidos 10-109'),
            React.createElement('div', {className: 'grid-cp'},
              laminaCP.map(cell => React.createElement('div', {
                key: cell.num,
                className: `cell-cp ${cell.freq >= 4 ? 'alta' : ''}`,
                onClick: () => alert(`CP ${cell.num}: Freq ${cell.freq} Visual ${cell.visual} Decomp ${cell.decomp}`)
              }, `${cell.num} ${cell.visual}`))
            )
          );
        }
        ReactDOM.render(React.createElement(App), document.getElementById('root'));
      </script>
    </body>
    </html>
  `);
});

app.listen(port, () => console.log(`Servicio Activo Puerto ${port}`));
