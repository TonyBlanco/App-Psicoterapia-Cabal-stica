const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors({origin: '*'}));
app.use(express.json());
const port = process.env.PORT || 3000;

// Tabla Pitagórica Dos Cifras (Normas Senderos)
const pitagoricaTabla = {A:1, B:2, C:11, D:4, E:5, F:6, G:7, H:8, I:9, J:10, K:11, L:12, M:13, N:14, O:15, P:16, Q:17, R:18, S:19, SS:42, T:20, U:21, V:22, W:23, X:24, Y:25, Z:26, CH:8, Ñ:14};

function sanitizeNormas(nombre) {
  return nombre.replace(/pepe|fran|paco|conchi|diminutivo|hipocoristico/gi, 'José').replace(/maría de /i, ''); // Regla 4 exclusión
}

function gematriaPitagorica(nombre) {
  const clean = sanitizeNormas(nombre).toUpperCase().replace(/ /g, '');
  let sum = 0, i = 0;
  while (i < clean.length) {
    let key = clean[i];
    if (clean[i] === 'S' && i+1 < clean.length && clean[i+1] === 'S') { key = 'SS'; i += 2; } else i++;
    sum += pitagoricaTabla[key] || 0;
  }
  return sum; // Intacto dos cifras
}

app.get('/', (req, res) => res.send('¡Árbol Vivo! Backend Cabalístico Listo. Prueba /calculo?nombre=Luis&fecha=01/08/1959'));

app.get('/calculo', (req, res) => {
  const {nombre,fecha}=req.query;
  const gemPit=gematriaPitagorica(nombre || 'Luis Antonio Blanco Fontela');
  const scf=fecha ? fecha.replace(/\//g,'').split('').reduce((s,d)=>s+(+d),0) : 33;
  const otd={TO:1,PT:8,TD:14}; // Canónico, futuro algoritmoSendero(gemPit)
  const cp={14:{freq:scf>30?5:4,decomp:'P41 Servicio'}}; // Ej dinámico SCF
  res.json({OTD:otd,CP:cp,gemPit,scf});
});

app.listen(port, () => console.log(`Servicio Activo Puerto ${port}`));
