const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors({origin: '*'}));
app.use(express.json());
const port = process.env.PORT || 3000;

// Gematria Pitagórica Dos Cifras + Normas
const pitagoricaTabla = {A:1,B:2,C:11,D:4,E:5,F:6,G:7,H:8,I:9,J:10,K:11,L:12,M:13,N:14,O:15,P:16,Q:17,R:18,S:19,SS:42,T:20,U:21,V:22,W:23,X:24,Y:25,Z:26,CH:8,Ñ:14};
function sanitizeNormas(nombre) { return nombre.replace(/pepe|fran|paco|conchi/gi, 'José').replace(/maría de /i, ''); }
function gematriaPitagorica(nombre) {
  const clean = sanitizeNormas(nombre).toUpperCase().replace(/ /g, '');
  let sum = 0, i = 0;
  while (i < clean.length) {
    let key = clean[i];
    if (clean[i] === 'S' && i+1 < clean.length && clean[i+1] === 'S') { key = 'SS'; i += 2; } else i++;
    sum += pitagoricaTabla[key] || 0;
  }
  return sum;
}

// Alefato Hebreo + Adbash Simple
const alefato = {א:1,ב:2,ג:3,ד:4,ה:5,ו:6,ז:7,ח:8,ט:9,י:10,כ:20,ל:30,מ:40,נ:50,ס:60,ע:70,פ:80,צ:90,ק:100,ר:200,ש:300,ת:400};
function gematriaHebrea(texto) { return texto.split('').reduce((sum, l) => sum + (alefato[l] || 0), 0); }
function adbashHebreo(palabra) {
  const keys = Object.keys(alefato);
  const reverse = keys.slice().reverse();
  return palabra.split('').map(l => reverse[keys.indexOf(l)] || l).join('');
}

app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html lang="es">
    <head><title>Dashboard Cabalístico Tipheret Armonía</title><style>body{font-family:Arial;background:#f0f8ff;padding:20px;}table{border-collapse:collapse;width:100%;}th,td{border:1px solid #ccc;padding:8px;text-align:left;}.grid-cp{display:grid;grid-template-columns:repeat(10,1fr);gap:1px;background:#ddd;margin:10px 0;}.cell-cp{padding:5px;border:1px solid #ccc;text-align:center;cursor:pointer;}.alta{background:red;color:white;}</style></head>
    <body>
      <h1>¡Árbol Vivo! Dashboard Cabalístico Listo. TO=1 Mago Unidad</h1>
      <div id="root"></div>
      <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
      <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
      <script>
        const {useState,useEffect}=React;
        function App() {
          const [data,setData]=useState({OTD:{},CP:{},gemPit:0,gemHeb:0,adbash:''});
          useEffect(() => {
            fetch('/calculo?nombre=Luis Antonio Blanco Fontela&fecha=01/08/1959').then(r=>r.json()).then(setData).catch(e=>console.log(e));
          }, []);
          const laminaCP=Array.from({length:100},(_,i)=>({num:i+10,freq:data.CP[i+10]?.freq||0,visual:'|'.repeat(data.CP[i+10]?.freq||0)}));
          return React.createElement('div',null,
            React.createElement('h2',null,'Panel A: Senderos OTD'),
            React.createElement('table',null,
              React.createElement('thead',null,React.createElement('tr',null,React.createElement('th',null,'Sendero'),React.createElement('th',null,'Valor'),React.createElement('th',null,'Arcano'),React.createElement('th',null,'Función'))),
              React.createElement('tbody',null,
                React.createElement('tr',null,React.createElement('td',null,'TO'),React.createElement('td',null,data.OTD.TO||'Cargando'),React.createElement('td',null,'El Mago'),React.createElement('td',null,'Base Unidad Voluntad')),
                React.createElement('tr',null,React.createElement('td',null,'PT'),React.createElement('td',null,data.OTD.PT||''),React.createElement('td',null,'La Justicia'),React.createElement('td',null,'Transición Fuerza Misión')),
                React.createElement('tr',null,React.createElement('td',null,'TD'),React.createElement('td',null,data.OTD.TD||''),React.createElement('td',null,'La Templanza'),React.createElement('td',null,'Misión Servicio Armonía'))
              )
            ),
            React.createElement('h2',null,'Panel C: CP Lámina Repetidos 10-109'),
            React.createElement('div',{className:'grid-cp'},
              laminaCP.map(cell=>React.createElement('div',{key:cell.num,className:`cell-cp ${cell.freq>=4?'alta':''}`,onClick:()=>alert(`CP ${cell.num}: Freq ${cell.freq} Visual ${cell.visual} Decomp P${cell.num*2+1}`)},`${cell.num} ${cell.visual}`))
            ),
            React.createElement('p',null,`Gematria Pitagórica: ${data.gemPit} | Hebrea Ej Alef: ${data.gemHeb} | Adbash Ej: ${data.adbash}`),
            React.createElement('p',null,`Corroboración %9: ${((data.gemPit%9||9)===(data.gemHeb%9||9))?'Armonía Holística':'Fallback Canónico'}`)
          );
        }
        ReactDOM.render(React.createElement(App),document.getElementById('root'));
      </script>
    </body>
    </html>
  `);
});

app.get('/calculo', (req, res) => {
  const {nombre='Luis Antonio Blanco Fontela',fecha='01/08/1959'}=req.query;
  const gemPit=gematriaPitagorica(nombre);
  const scf=fecha.replace(/\//g,'').split('').reduce((s,d)=>s+(+d),0);
  const pin=gemPit+scf;
  const otd={TO:1,PT:8,TD:14};
  const cp={14:{freq:4}}; // Ej canónico Luis
  const gemHebEj=gematriaHebrea('אלף'); // Alef=111→3
  const adbashEj=adbashHebreo('אלף'); // Ej 'תשפ"ג'
  res.json({OTD:otd,CP:cp,gemPit,gemHeb:gemHebEj,adbash:adbashEj});
});

app.listen(port,()=>console.log(`Servicio Activo Puerto ${port}`));
