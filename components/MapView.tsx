import * as d3 from 'd3';
import { useEffect, useRef } from 'react';

const MapView: React.FC<{ vibracion?: number }> = ({ vibracion }) => {
  const svgRef = useRef<SVGSVGElement>(null);

  useEffect(() => {
    if (svgRef.current) {
      const svg = d3.select(svgRef.current);
      // Carga diagram.json: nodos = [{id: 'fundamentos', label: 'Psicoterapia...', x:0, y:0}, ...]
      // Edges del diagrama original
      // Ilumina nodo si matches vibracion (e.g., fill: vibracion === 8 ? '#FFD700' : 'gray')
      svg.append('circle').attr('cx', 100).attr('cy', 100).attr('r', 50).style('fill', vibracion ? 'gold' : 'silver');
      // Expande: zoom, drag para interactividad
    }
  }, [vibracion]);

  return <svg ref={svgRef} width="100%" height="600px" viewBox="0 0 800 600" />;
};

export default MapView;
