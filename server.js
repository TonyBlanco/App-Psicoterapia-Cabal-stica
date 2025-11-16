const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors({origin: '*'}));
app.use(express.json());
const port = process.env.PORT || 3000;

// [Código gematriaPitagorica, gematriaHebrea, adbashHebreo de anterior, pegar aquí]

app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html lang="es">
    <head><title>Dashboard Cabalístico Tipheret Armonía</title><style>body{font-family:Arial;background:#f0f8ff;padding:20px;}table{border-collapse:collapse;width:100%;}th,td{border:1px solid #ccc;padding:8px;text-align:left;}.grid-cp{display:grid;grid-template-columns:repeat(10,1fr);gap:1px;background:#ddd;}.cell-cp{padding:5px;border:1px solid #ccc;text-align:center;cursor:pointer;}.alta{ background:red;color:white;}</style></head>
    <body>
    <h1>Dashboard Holístico Tipheret (6 Armonía Integra Pitagórica-Mística)</h1>
    <div id="root"></div>
    <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script>
    const {useState,useEffect}=React;
    function App() {
      const [data, setData] = useState({OTD:{}, CP:{}, gemPit:0, gemHeb:0, adbash:''});
      useEffect(() => {
        fetch('/calculo?nombre=Luis Antonio Blanco Fontela&fecha=01/08/1959')
          .then(r => r.json()).then(setData);
      }, []);
      const laminaCP = Array.from({length:100}, (_,i) => ({num:i+10, freq:data.CP[i+10]?.freq||0, visual:'|'.repeat(data.CP[i+10]?.freq||0)})); // Lámina 10-109
      return React.createElement('div', null,
        React.createElement('h2', null, 'Panel A: Senderos OTD'),
        React.createElement('table', null,
          React.createElement('thead', null, React.createElement('tr', null, React.createElement('th', null, 'Sendero'), React.createElement('th', null, 'Valor'), React.createElement('th', null, 'Arcano'), React.createElement('th', null, 'Función'))),
          React.createElement('tbody', null,
            React.createElement('tr', null, React.createElement('td', null, 'TO'), React.createElement('td', null, data.OTD.TO||'Cargando'), React.createElement('td', null, 'El Mago'), React.createElement('td', null, 'Base Unidad Voluntad')),
            React.createElement('tr', null, React.createElement('td', null, 'PT'), React.createElement('td', null, data.OTD.PT||''), React.createElement('td', null, 'La Justicia'), React.createElement('td', null, 'Transición Fuerza Misión')),
            React.createElement('tr', null, React.createElement('td', null, 'TD'), React.createElement('td', null, data.OTD.TD||''), React.createElement('td', null, 'La Templanza'), React.createElement('td', null, 'Misión Servicio Armonía'))
          )
        ),
        React.createElement('h2', null, 'Panel C: CP Lámina Repetidos 10-109'),
        React.createElement('div', {className:'grid-cp', style:{gridTemplateColumns:'repeat(10,1fr)'}},
          laminaCP.map(cell => React.createElement('div', {key:cell.num, className:`cell-cp ${cell.freq>=4 ? 'alta' : ''}`, onClick:() => alert(`CP ${cell.num}: Freq ${cell.freq} Visual ${cell.visual} Decomp P${(cell.num*2+1)}`)}, `${cell.num} ${cell.visual}`))
        ),
        React.createElement('p', null, `Gematria Pitagórica: ${data.gemPit} | Hebrea Ej Alef: ${data.gemHeb} | Adbash Ej: ${data.adbash}`),
        React.createElement('p', null, `Corroboración %9: ${((data.gemPit % 9 || 9) === (data.gemHeb % 9 || 9)) ? 'Armonía Holística' : 'Fallback Canónico'}`)
      );
    }
    ReactDOM.render(React.createElement(App), document.getElementById('root'));
    </script>
    </body>
    </html>
  `);
});

// [Endpoints /calculo con data OTD={TO:1,PT:8,TD:14}, CP={14:{freq:4}}, gemPit:269, etc. de anterior]

app.listen(port, () => console.log(`Servicio Activo Puerto ${port}`));
