import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

interface LoginProps {}  // Tipado futuro para props

const Login: React.FC<LoginProps> = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      });
      const data = await response.json();
      if (data.token) {
        localStorage.setItem('jwt', data.token);
        localStorage.setItem('roles', JSON.stringify(data.roles || []));
        // Holística Inicial: Cálculo vibración email para "bendición de acceso"
        const vibEmail = pythagoreanConvert(email);  // Importa de utils
        if (validateHolistic(vibEmail, [1])) {  // Corrobora vs. Kether (inicio)
          navigate('/dashboard');
        } else {
          alert('Desarmonía Inicial: Vibración no alineada. Intente con intención pura.');
        }
      } else {
        alert('Error Login: Verifique Credenciales');
      }
    } catch (error) {
      alert('Desarmonía: Error Conexión');
    }
  };

  return (
    // Preserva JSX actual: Header morado con 🍇, form blanco, lista features
    <div style={{ backgroundColor: '#f0f0f0', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Header y Main idénticos al actual */}
      <header style={{ backgroundColor: '#8B008B', /* ... resto igual */ }}>
        {/* ... JSX header actual ... */}
      </header>
      <main style={{ /* ... */ }}>
        <div style={{ /* card blanca */ }}>
          <h2 /* ... */>Login Usuario</h2>
          <form onSubmit={handleLogin}>
            {/* Inputs email/password iguales, con required */}
            <button type="submit" /* verde */>Conectar</button>
          </form>
          {/* Links y ul features iguales */}
        </div>
      </main>
    </div>
  );
};

export default Login;
