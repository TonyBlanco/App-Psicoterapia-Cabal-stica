const express = require('express');
const app = express();
app.get('/', (req, res) => res.send('¡Árbol Vivo! Dashboard Cabalístico Listo. TO=1 Mago Unidad.'));
app.listen(3000, () => console.log('Render Servicio Activo'));
