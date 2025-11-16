import React from 'react';

interface Props { vibracion: number; }

export const MiniMapPreview: React.FC<Props> = ({ vibracion }) => (
  <svg width="200" height="100" style={{ marginTop: '10px' }}>
    <circle cx="100" cy="50" r="40" fill={vibracion === 8 ? 'gold' : 'silver'} stroke="#8B008B" strokeWidth="2" />
    <text x="100" y="55" textAnchor="middle" fill="#8B008B">{`Sephira ${vibracion}`}</text>
  </svg>
);
