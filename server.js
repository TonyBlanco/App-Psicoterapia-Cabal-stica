const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors({origin: '*'}));
app.use(express.json());
const port = process.env.PORT || 3000;

// Tabla Pitagórica Dos Cifras (Normas Senderos)
const pitagoricaTabla = {A:1, B:2, C:11, D:4, E:5, F:6, G:7, H:8, I:9, J:10, K:11, L:12, M:13, N:14, O:15, P:16, Q:17, R:18, S:19, SS:42, T:20, U:21, V:22, W:23, X:24, Y:25, Z:26, CH:8, Ñ:14};

function sanitizeNormas(nombre) {
  return nombre.replace(/pepe|fran|paco|conchi/gi, 'José').replace(/maría de /i, ''); // Regla 4/7
}

function gematriaPitagorica(nombre) {
  const clean = sanitizeNormas(nombre).toUpperCase().replace(/ /g, '');
  let sum = 0;
  for (let i = 0; i < clean.length; i++) {
    let key = clean[i];
    if (clean[i] === 'S' && clean[i+1] === 'S') { key = 'SS'; i++; } // SS=42
    sum += pitagoricaTabla[key] || 0;
  }
  return sum; // Intacto dos cifras
}

// Alefato Hebreo Simple (npm hebrew-numerals o custom)
const alefato = {א:1, ב:2, ג:3, ד:4, ה:5, ו:6, ז:7, ח:8, ט:9, י:10, כ:20, ל:30, מ:40, נ:50, ס:60, ע:70, פ:80, צ:90, ק:100, ר:200, ש:300, ת:400};

function gematriaHebrea(texto) {
  return texto.split('').reduce((sum, l) => sum + (alefato[l] || 0), 0);
}

// Desencriptación Mística Simple
function adbashHebreo(palabra) {
  const keys = Object.keys(alefato);
  const reverse = keys.slice().reverse();
  return palabra.split('').map(l => reverse[keys.indexOf(l)] || l).join('');
}

app.get('/', (req, res) => res.send('¡Árbol Vivo! Dashboard Cabalístico Listo. TO=1 Mago Unidad.'));

app.get('/calculo', (req, res) => {
  const {nombre, fecha} = req.query;
  const gemPit = gematriaPitagorica(nombre || 'Luis Antonio Blanco Fontela');
  const scf = fecha ? fecha.replace(/\//g,'').split('').reduce((s,d) => s + +d, 0) : 33; // Hoy SCF=18
  const pin = gemPit + scf;
  const to = 1, pt = 8, td = 14; // Canónico Luis
  const gemHebEj = gematriaHebrea('אלף'); // Ej "Alef"=1
  const adbashEj = adbashHebreo('אלף'); // Sustitución
  res.json({gemPit, scf, pin, TO:to, PT:pt, TD:td, gemHebreaEj:gemHebEj, adbashEj});
});

app.listen(port, () => console.log(`Servicio Activo Puerto ${port}`));
