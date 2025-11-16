import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './components/Login';  // Auto-resuelve .tsx
import Dashboard from './components/Dashboard';
// ... Otros imports

interface AppState { jwt?: string; }  // Tipado holístico para auth

const App: React.FC = () => {
  const isAuthenticated = !!localStorage.getItem('jwt');
  return (
    <Router>
      <Routes>
        <Route path="/login" element={!isAuthenticated ? <Login /> : <Navigate to="/dashboard" />} />
        <Route path="/dashboard" element={isAuthenticated ? <Dashboard /> : <Navigate to="/login" />} />
        {/* ... Otras rutas */}
        <Route path="/" element={<Navigate to="/login" />} />
        <Route path="*" element={<div>Desarmonía: Ruta No Resuelta (Vib. 32)</div>} />
      </Routes>
    </Router>
  );
};

export default App;
