import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App';  // Apunta a App.tsx (CRA resuelve .tsx auto)

const container = document.getElementById('root');
if (!container) {
  throw new Error('Desarmonía Kether: #root ausente — Verifique index.html');
}
const root = createRoot(container);
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
