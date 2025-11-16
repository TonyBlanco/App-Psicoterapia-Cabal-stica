import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    fetch('/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    })
    .then(r => r.json())
    .then(data => {
      if (data.token) {
        localStorage.setItem('jwt', data.token);
        localStorage.setItem('roles', JSON.stringify(data.roles));
        navigate('/dashboard');
      } else alert('Error Login: Verifique Credenciales');
    })
    .catch(e => alert('Desarmonía: Error Conexión'));
  };

  return (
    <div style={{ backgroundColor: '#f0f0f0', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Header Morado */}
      <header style={{ backgroundColor: '#8B008B', color: 'white', padding: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div style={{ display: 'flex', alignItems: 'center' }}>
          <span style={{ fontSize: '24px', marginRight: '10px' }}>🍇</span> {/* Logo uva emoji */}
          <h1>Cábala</h1>
          <span style={{ fontSize: '14px', marginLeft: '10px' }}>Profesional</span>
        </div>
        <nav>
          <a href="#" style={{ color: 'white', margin: '0 10px', textDecoration: 'none' }}>Calcular Cábala</a> |
          <a href="#" style={{ color: 'white', margin: '0 10px', textDecoration: 'none' }}>Bases de Datos</a> |
          <a href="#" style={{ color: 'white', margin: '0 10px', textDecoration: 'none' }}>Calculadora Cósmica</a>
        </nav>
      </header>
      {/* Login Card Blanco */}
      <main style={{ flex: 1, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <div style={{ backgroundColor: 'white', padding: '30px', borderRadius: '8px', boxShadow: '0 4px 6px rgba(0,0,0,0.1)', maxWidth: '400px', width: '100%' }}>
          <h2 style={{ textAlign: 'center', color: '#8B008B', marginBottom: '20px' }}>Login Usuario</h2>
          <form onSubmit={handleLogin}>
            <label style={{ display: 'block', marginBottom: '5px', color: '#666' }}>Correo Electrónico:</label>
            <input type="email" value={email} onChange={e => setEmail(e.target.value)} placeholder="usuario@ej.com" style={{ width: '100%', padding: '12px', marginBottom: '15px', border: '1px solid #ccc', borderRadius: '4px' }} required />
            <label style={{ display: 'block', marginBottom: '5px', color: '#666' }}>Contraseña:</label>
            <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="contraseña" style={{ width: '100%', padding: '12px', marginBottom: '15px', border: '1px solid #ccc', borderRadius: '4px' }} required />
            <button type="submit" style={{ width: '100%', padding: '12px', backgroundColor: '#4CAF50', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', fontSize: '16px' }}>Conectar</button>
          </form>
          <p style={{ textAlign: 'center', marginTop: '15px', fontSize: '14px' }}>
            <a href="#" style={{ color: '#8B008B' }}>¿Olvidaste la contraseña?</a> | <a href="#" style={{ color: '#8B008B' }}>No tienes cuenta? Crea una</a>
          </p>
          <ul style={{ marginTop: '20px', fontSize: '12px', color: '#666', listStyleType: 'none', padding: 0 }}>
            <li>✓ Acceso ilimitado</li>
            <li>✓ Consulta 1 persona</li>
            <li>✓ Imprimir análisis</li>
            <li>✓ Acceso guardar consulta</li>
            <li>✓ Acceso a base de datos apuntes</li>
            <li>✓ Acceso base de datos clientes</li>
            <li>✓ Acceso a la calculadora cósmica</li>
            <li>✓ Acceso ventana emergente de información breve</li>
            <li>✓ Acceso menú emergente de asistencia a la consulta</li>
            <li>✓ Acceso comparativa de dos personas</li>
            <li>✓ Acceso cálculo vibración conjunta</li>
          </ul>
        </div>
      </main>
    </div>
  );
}

export default Login;
