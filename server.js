const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const usuarios = [{email: 'user@ej.com', password: bcrypt.hashSync('pass', 10), roles: ['ilimitado', 'consulta1', 'guardar', 'baseapuntes', 'baseclientes', 'calcosmica', 'ventanainfo', 'menuasistencia', 'comparativa2', 'vibrconjuncta']}]; // Mock DB

app.post('/login', (req, res) => {
  const {email, password} = req.body;
  const user = usuarios.find(u => u.email === email);
  if (user && bcrypt.compareSync(password, user.password)) {
    const token = jwt.sign({email, roles: user.roles}, 'secret_key', {expiresIn: '1h'});
    res.json({token, roles: user.roles});
  } else res.status(401).json({error: 'Credenciales Invalidas'});
});
