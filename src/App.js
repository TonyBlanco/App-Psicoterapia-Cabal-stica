import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Add react-router-dom package.json if not

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = () => {
    fetch('/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    })
    .then(r => r.json())
    .then(data => {
      if (data.token) {
        localStorage.setItem('jwt', data.token);
        localStorage.setItem('roles', JSON.stringify(data.roles)); // e.g., ['ilimitado', 'consulta1']
        navigate('/dashboard'); // Redirect to dashboard
      } else alert('Error Login: Verifique Credenciales');
    })
    .catch(e => alert('Desarmonía: Error Conexión'));
  };

  return (
    <div style={{ maxWidth: '400px', margin: '0 auto', padding: '20px', background: 'white', borderRadius: '8px', boxShadow: '0 2px 10px rgba(0,0,0,0.1)' }}>
      <h1 style={{ textAlign: 'center', color: '#8B008B' }}>Cábala Profesional</h1>
      <form onSubmit={e => { e.preventDefault(); handleLogin(); }}>
        <label style={{ display: 'block', marginBottom: '5px' }}>Correo Electrónico:</label>
        <input type="email" value={email} onChange={e => setEmail(e.target.value)} placeholder="usuario@ej.com" style={{ width: '100%', padding: '10px', marginBottom: '10px', border: '1px solid #ccc', borderRadius: '4px' }} required />
        <label style={{ display: 'block', marginBottom: '5px' }}>Contraseña:</label>
        <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="contraseña" style={{ width: '100%', padding: '10px', marginBottom: '10px', border: '1px solid #ccc', borderRadius: '4px' }} required />
        <button type="submit" style={{ width: '100%', padding: '10px', background: '#8B008B', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>Conectar</button>
      </form>
      <p style={{ textAlign: 'center', marginTop: '10px', fontSize: '14px' }}>
        <a href="#" style={{ color: '#8B008B' }}>¿Olvidaste la contraseña?</a> | <a href="#" style={{ color: '#8B008B' }}>No tienes cuenta? Crea una</a>
      </p>
      <p style={{ textAlign: 'center', fontSize: '12px', color: '#666' }}>Acceso ilimitado: Consulta 1 persona | Imprimir análisis | Guardar consulta | Base datos apuntes | Base datos clientes | Calculadora cósmica | Ventana info breve | Menú asistencia | Comparativa 2 personas | Cálculo vibración conjunta</p>
    </div>
  );
}

export default Login;
