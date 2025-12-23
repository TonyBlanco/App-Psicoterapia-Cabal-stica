"""
Generador de Reportes PDF con Visualizaciones
Crea reportes profesionales de análisis cabalístico
"""

import matplotlib
matplotlib.use('Agg')  # Backend sin GUI
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle
from datetime import datetime
from typing import Dict, List
import os

# Importar módulos propios
from cabala_calculator import CabalaCalculator
from interpretaciones import InterpretacionesCabalisticas
from sephirot import ArbolDeLaVida, CalculadorAnioPersonal


class GeneradorReportePDF:
    """Genera reportes PDF con análisis cabalístico completo"""
    
    def __init__(self):
        self.calculator = CabalaCalculator()
        self.interpretaciones = InterpretacionesCabalisticas()
        self.arbol = ArbolDeLaVida()
        
    def generar_reporte_completo(self, nombre: str, fecha: str, 
                                output_file: str = "reporte_cabalistico.pdf") -> str:
        """
        Genera un reporte PDF completo con todas las visualizaciones
        
        Args:
            nombre: Nombre completo de la persona
            fecha: Fecha de nacimiento DD/MM/AAAA
            output_file: Nombre del archivo de salida
            
        Returns:
            Ruta del archivo generado
        """
        # Calcular análisis completo
        analisis = self.calculator.calcular_sendero_alma(nombre, fecha)
        
        # Crear figura con múltiples páginas
        from matplotlib.backends.backend_pdf import PdfPages
        
        with PdfPages(output_file) as pdf:
            # Página 1: Portada
            self._crear_portada(pdf, nombre, fecha)
            
            # Página 2: Árbol de la Vida con sendero iluminado
            self._crear_pagina_arbol(pdf, analisis)
            
            # Página 3: Análisis numerológico detallado
            self._crear_pagina_analisis(pdf, analisis)
            
            # Página 4: Interpretación del Sendero del Alma
            self._crear_pagina_interpretacion(pdf, analisis)
            
            # Página 5: Gráficos de vibraciones
            self._crear_pagina_graficos(pdf, analisis)
            
            # Página 6: Año personal y predicciones
            self._crear_pagina_anio_personal(pdf, analisis)
            
            # Metadata
            d = pdf.infodict()
            d['Title'] = f'Análisis Cabalístico - {nombre}'
            d['Author'] = 'Sistema de Astrología Cabalística'
            d['Subject'] = 'Análisis Numerológico y Cabalístico'
            d['Keywords'] = 'Cábala, Numerología, Árbol de la Vida'
            d['CreationDate'] = datetime.now()
        
        return output_file
    
    def _crear_portada(self, pdf, nombre: str, fecha: str):
        """Crea la página de portada"""
        fig = plt.figure(figsize=(8.5, 11))
        ax = fig.add_subplot(111)
        ax.axis('off')
        
        # Fondo degradado
        gradient = ax.imshow([[0, 0], [1, 1]], extent=[0, 1, 0, 1], 
                            aspect='auto', cmap='twilight', alpha=0.3)
        
        # Título principal
        ax.text(0.5, 0.75, 'ANÁLISIS CABALÍSTICO', 
               ha='center', va='center', fontsize=28, fontweight='bold',
               color='#4B0082')
        
        ax.text(0.5, 0.68, 'Sendero del Alma', 
               ha='center', va='center', fontsize=18, 
               color='#8B008B', style='italic')
        
        # Símbolo del Árbol de la Vida simplificado
        self._dibujar_simbolo_arbol_simple(ax, 0.5, 0.45, 0.15)
        
        # Información personal
        ax.text(0.5, 0.25, nombre.upper(), 
               ha='center', va='center', fontsize=20, fontweight='bold',
               color='#2F4F4F')
        
        ax.text(0.5, 0.20, f'Fecha de Nacimiento: {fecha}', 
               ha='center', va='center', fontsize=14,
               color='#696969')
        
        # Fecha del reporte
        fecha_reporte = datetime.now().strftime('%d de %B de %Y')
        ax.text(0.5, 0.08, f'Reporte generado: {fecha_reporte}', 
               ha='center', va='center', fontsize=10,
               color='#A9A9A9', style='italic')
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
    
    def _dibujar_simbolo_arbol_simple(self, ax, cx, cy, size):
        """Dibuja un símbolo simplificado del Árbol de la Vida"""
        # Círculo central (Tiphareth)
        circle = Circle((cx, cy), size * 0.15, color='gold', alpha=0.7, zorder=3)
        ax.add_patch(circle)
        
        # Círculos superiores
        circle1 = Circle((cx, cy + size * 0.5), size * 0.1, color='white', 
                        edgecolor='purple', linewidth=2, alpha=0.8, zorder=3)
        ax.add_patch(circle1)
        
        circle2 = Circle((cx - size * 0.3, cy + size * 0.25), size * 0.1, 
                        color='gray', alpha=0.7, zorder=3)
        ax.add_patch(circle2)
        
        circle3 = Circle((cx + size * 0.3, cy + size * 0.25), size * 0.1, 
                        color='black', alpha=0.7, zorder=3)
        ax.add_patch(circle3)
        
        # Círculos inferiores
        circle4 = Circle((cx, cy - size * 0.5), size * 0.1, 
                        color='brown', alpha=0.7, zorder=3)
        ax.add_patch(circle4)
        
        # Líneas conectoras
        ax.plot([cx, cx], [cy + size * 0.5, cy], 'purple', linewidth=1.5, alpha=0.5, zorder=1)
        ax.plot([cx, cx - size * 0.3], [cy, cy + size * 0.25], 'purple', 
               linewidth=1.5, alpha=0.5, zorder=1)
        ax.plot([cx, cx + size * 0.3], [cy, cy + size * 0.25], 'purple', 
               linewidth=1.5, alpha=0.5, zorder=1)
        ax.plot([cx, cx], [cy, cy - size * 0.5], 'purple', linewidth=1.5, alpha=0.5, zorder=1)
    
    def _crear_pagina_arbol(self, pdf, analisis: Dict):
        """Crea la página con el Árbol de la Vida"""
        fig = plt.figure(figsize=(8.5, 11))
        ax = fig.add_subplot(111)
        ax.axis('off')
        
        # Título
        ax.text(0.5, 0.95, 'ÁRBOL DE LA VIDA CABALÍSTICO', 
               ha='center', va='top', fontsize=18, fontweight='bold',
               transform=ax.transAxes, color='#4B0082')
        
        ax.text(0.5, 0.91, f'Tu Sendero: {analisis["sendero_alma"]}', 
               ha='center', va='top', fontsize=14,
               transform=ax.transAxes, color='#8B008B')
        
        # Dibujar el Árbol de la Vida
        self._dibujar_arbol_vida(ax, analisis['sendero_alma'])
        
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
    
    def _dibujar_arbol_vida(self, ax, sendero_activo: int):
        """Dibuja el Árbol de la Vida completo con las 10 Sephirot"""
        # Obtener coordenadas
        coords = self.arbol.generar_coordenadas_arbol(600, 700)
        conexiones = self.arbol.obtener_conexiones()
        
        # Configurar límites
        ax.set_xlim(0, 800)
        ax.set_ylim(0, 800)
        ax.invert_yaxis()  # Invertir Y para que Kether esté arriba
        
        # Dibujar conexiones (senderos)
        for desde, hasta in conexiones:
            x1, y1 = coords[desde]['x'], coords[desde]['y']
            x2, y2 = coords[hasta]['x'], coords[hasta]['y']
            ax.plot([x1, x2], [y1, y2], 'gray', linewidth=1.5, alpha=0.4, zorder=1)
        
        # Dibujar Sephirot
        for num, coord in coords.items():
            sephira = self.arbol.obtener_sephira(num)
            
            # Determinar si esta Sephira está en el camino del sendero activo
            camino = self.arbol.calcular_camino_espiritual(sendero_activo)
            es_activa = any(s['nombre'] == sephira['nombre'] for s in camino)
            
            # Color y tamaño
            color = coord['color']
            size = 800 if es_activa else 500
            alpha = 0.9 if es_activa else 0.6
            edge_width = 3 if es_activa else 2
            
            # Círculo de la Sephira
            circle = Circle((coord['x'], coord['y']), 40, 
                          color=color, alpha=alpha, 
                          edgecolor='black', linewidth=edge_width, zorder=3)
            ax.add_patch(circle)
            
            # Número
            ax.text(coord['x'], coord['y'] - 5, str(num), 
                   ha='center', va='center', fontsize=14, 
                   fontweight='bold', color='white', zorder=4)
            
            # Nombre
            ax.text(coord['x'], coord['y'] + 60, coord['nombre'], 
                   ha='center', va='top', fontsize=10, 
                   fontweight='bold' if es_activa else 'normal',
                   color='black', zorder=4)
        
        # Leyenda de pilares
        ax.text(100, 750, 'Pilar de la\nMisericordia', ha='center', fontsize=9, 
               style='italic', color='#0000FF')
        ax.text(400, 750, 'Pilar del\nEquilibrio', ha='center', fontsize=9, 
               style='italic', color='#FFD700')
        ax.text(700, 750, 'Pilar de la\nSeveridad', ha='center', fontsize=9, 
               style='italic', color='#FF0000')
    
    def _crear_pagina_analisis(self, pdf, analisis: Dict):
        """Crea la página con análisis numerológico detallado"""
        fig = plt.figure(figsize=(8.5, 11))
        ax = fig.add_subplot(111)
        ax.axis('off')
        
        # Título
        ax.text(0.5, 0.95, 'ANÁLISIS NUMEROLÓGICO', 
               ha='center', va='top', fontsize=18, fontweight='bold',
               transform=ax.transAxes, color='#4B0082')
        
        y_pos = 0.88
        line_height = 0.04
        
        # Análisis del nombre
        vib_nombre = analisis['vibracion_nombre']
        ax.text(0.1, y_pos, 'VIBRACIÓN DEL NOMBRE', fontsize=14, 
               fontweight='bold', transform=ax.transAxes, color='#8B008B')
        y_pos -= line_height
        
        ax.text(0.1, y_pos, f"Nombre: {vib_nombre['nombre']}", 
               fontsize=11, transform=ax.transAxes)
        y_pos -= line_height
        
        ax.text(0.1, y_pos, f"Proceso: {vib_nombre['proceso'][:80]}...", 
               fontsize=9, transform=ax.transAxes, style='italic', color='#696969')
        y_pos -= line_height
        
        ax.text(0.1, y_pos, f"Suma Total: {vib_nombre['suma_total']}", 
               fontsize=11, transform=ax.transAxes)
        y_pos -= line_height
        
        ax.text(0.1, y_pos, f"Vibración Final: {vib_nombre['vibracion']}", 
               fontsize=12, fontweight='bold', transform=ax.transAxes, color='#FF6347')
        y_pos -= line_height * 2
        
        # Análisis de la fecha
        vib_fecha = analisis['vibracion_fecha']
        ax.text(0.1, y_pos, 'VIBRACIÓN DE LA FECHA', fontsize=14, 
               fontweight='bold', transform=ax.transAxes, color='#8B008B')
        y_pos -= line_height
        
        ax.text(0.1, y_pos, f"Fecha: {vib_fecha['fecha']}", 
               fontsize=11, transform=ax.transAxes)
        y_pos -= line_height
        
        ax.text(0.1, y_pos, 
               f"Día: {vib_fecha['dia']} → {vib_fecha['vibracion_dia']}  |  " +
               f"Mes: {vib_fecha['mes']} → {vib_fecha['vibracion_mes']}  |  " +
               f"Año: {vib_fecha['anio']} → {vib_fecha['vibracion_anio']}", 
               fontsize=10, transform=ax.transAxes)
        y_pos -= line_height
        
        ax.text(0.1, y_pos, f"Suma Total: {vib_fecha['suma_total']}", 
               fontsize=11, transform=ax.transAxes)
        y_pos -= line_height
        
        ax.text(0.1, y_pos, f"Vibración Final: {vib_fecha['vibracion']}", 
               fontsize=12, fontweight='bold', transform=ax.transAxes, color='#FF6347')
        y_pos -= line_height * 2
        
        # Sendero del Alma
        ax.text(0.1, y_pos, 'SENDERO DEL ALMA', fontsize=14, 
               fontweight='bold', transform=ax.transAxes, color='#8B008B')
        y_pos -= line_height
        
        ax.text(0.1, y_pos, f"Número del Sendero: {analisis['sendero_alma']}", 
               fontsize=13, fontweight='bold', transform=ax.transAxes, color='#4B0082')
        y_pos -= line_height
        
        ax.text(0.1, y_pos, f"Número de Expresión: {analisis['numero_expresion']}", 
               fontsize=11, transform=ax.transAxes)
        y_pos -= line_height
        
        ax.text(0.1, y_pos, f"Número de Destino: {analisis['numero_destino']}", 
               fontsize=11, transform=ax.transAxes)
        y_pos -= line_height
        
        ax.text(0.1, y_pos, f"Tikun (Corrección Kármica): {analisis['tikun']}", 
               fontsize=11, transform=ax.transAxes)
        y_pos -= line_height * 2
        
        # Alineación
        alineacion = analisis['alineacion']
        ax.text(0.1, y_pos, 'ALINEACIÓN HOLÍSTICA', fontsize=14, 
               fontweight='bold', transform=ax.transAxes, color='#8B008B')
        y_pos -= line_height
        
        ax.text(0.1, y_pos, f"Estado: {alineacion['estado']}", 
               fontsize=11, transform=ax.transAxes)
        y_pos -= line_height
        
        ax.text(0.1, y_pos, f"Porcentaje de Alineación: {alineacion['porcentaje']}%", 
               fontsize=11, fontweight='bold', transform=ax.transAxes, 
               color='#228B22' if alineacion['porcentaje'] >= 85 else '#FF8C00')
        
        # Barra de alineación
        rect_bg = FancyBboxPatch((0.1, y_pos - 0.05), 0.8, 0.03, 
                                boxstyle="round,pad=0.005", 
                                edgecolor='gray', facecolor='lightgray',
                                transform=ax.transAxes, zorder=2)
        ax.add_patch(rect_bg)
        
        rect_fill = FancyBboxPatch((0.1, y_pos - 0.05), 
                                  0.8 * (alineacion['porcentaje'] / 100), 0.03, 
                                  boxstyle="round,pad=0.005", 
                                  facecolor='#228B22' if alineacion['porcentaje'] >= 85 else '#FF8C00',
                                  transform=ax.transAxes, zorder=3)
        ax.add_patch(rect_fill)
        
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
    
    def _crear_pagina_interpretacion(self, pdf, analisis: Dict):
        """Crea la página con interpretación del sendero"""
        fig = plt.figure(figsize=(8.5, 11))
        ax = fig.add_subplot(111)
        ax.axis('off')
        
        sendero = analisis['sendero_alma']
        interp = self.interpretaciones.obtener_interpretacion(sendero)
        
        # Título
        ax.text(0.5, 0.95, f'SENDERO {sendero}: {interp["nombre"]}', 
               ha='center', va='top', fontsize=16, fontweight='bold',
               transform=ax.transAxes, color='#4B0082')
        
        y_pos = 0.88
        line_height = 0.035
        
        # Información básica
        secciones = [
            ('Arquetipo', interp['arquetipo']),
            ('Elemento', interp['elemento']),
            ('Planeta', interp['planeta']),
            ('Significado', interp['significado']),
        ]
        
        for titulo, contenido in secciones:
            ax.text(0.1, y_pos, f"{titulo}:", fontsize=11, fontweight='bold',
                   transform=ax.transAxes, color='#8B008B')
            y_pos -= line_height
            ax.text(0.15, y_pos, contenido, fontsize=10,
                   transform=ax.transAxes, wrap=True)
            y_pos -= line_height * 1.5
        
        # Luz y Sombra
        ax.text(0.1, y_pos, 'Aspectos de Luz:', fontsize=11, fontweight='bold',
               transform=ax.transAxes, color='#228B22')
        y_pos -= line_height
        luz_lines = self._wrap_text(interp['luz'], 70)
        for line in luz_lines:
            ax.text(0.15, y_pos, line, fontsize=9, transform=ax.transAxes)
            y_pos -= line_height * 0.8
        y_pos -= line_height * 0.5
        
        ax.text(0.1, y_pos, 'Aspectos de Sombra:', fontsize=11, fontweight='bold',
               transform=ax.transAxes, color='#8B0000')
        y_pos -= line_height
        sombra_lines = self._wrap_text(interp['sombra'], 70)
        for line in sombra_lines:
            ax.text(0.15, y_pos, line, fontsize=9, transform=ax.transAxes)
            y_pos -= line_height * 0.8
        y_pos -= line_height * 0.5
        
        # Lección y Consejo
        ax.text(0.1, y_pos, 'Lección Kármica:', fontsize=11, fontweight='bold',
               transform=ax.transAxes, color='#4B0082')
        y_pos -= line_height
        leccion_lines = self._wrap_text(interp['leccion'], 70)
        for line in leccion_lines:
            ax.text(0.15, y_pos, line, fontsize=9, transform=ax.transAxes)
            y_pos -= line_height * 0.8
        y_pos -= line_height * 0.5
        
        ax.text(0.1, y_pos, 'Consejo Espiritual:', fontsize=11, fontweight='bold',
               transform=ax.transAxes, color='#FF8C00')
        y_pos -= line_height
        consejo_lines = self._wrap_text(interp['consejo'], 70)
        for line in consejo_lines:
            ax.text(0.15, y_pos, line, fontsize=9, transform=ax.transAxes, style='italic')
            y_pos -= line_height * 0.8
        y_pos -= line_height * 0.5
        
        # Áreas de vida
        ax.text(0.1, y_pos, 'Profesión Ideal:', fontsize=11, fontweight='bold',
               transform=ax.transAxes, color='#8B008B')
        y_pos -= line_height
        prof_lines = self._wrap_text(interp['profesion'], 70)
        for line in prof_lines:
            ax.text(0.15, y_pos, line, fontsize=9, transform=ax.transAxes)
            y_pos -= line_height * 0.8
        
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
    
    def _crear_pagina_graficos(self, pdf, analisis: Dict):
        """Crea página con gráficos de vibraciones"""
        fig = plt.figure(figsize=(8.5, 11))
        
        # Título
        fig.suptitle('GRÁFICOS DE VIBRACIONES', fontsize=18, fontweight='bold', 
                    color='#4B0082', y=0.98)
        
        # Gráfico 1: Comparación de vibraciones
        ax1 = plt.subplot(3, 1, 1)
        categorias = ['Nombre', 'Fecha', 'Sendero del Alma']
        valores = [
            analisis['vibracion_nombre']['vibracion'],
            analisis['vibracion_fecha']['vibracion'],
            analisis['sendero_alma']
        ]
        colores = ['#FF6347', '#4169E1', '#FFD700']
        
        bars = ax1.bar(categorias, valores, color=colores, alpha=0.7, edgecolor='black')
        ax1.set_ylabel('Vibración', fontsize=11, fontweight='bold')
        ax1.set_title('Comparación de Vibraciones', fontsize=12, fontweight='bold')
        ax1.set_ylim(0, max(valores) + 5)
        ax1.grid(axis='y', alpha=0.3)
        
        # Añadir valores en las barras
        for bar, val in zip(bars, valores):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{val}', ha='center', va='bottom', fontweight='bold')
        
        # Gráfico 2: Alineación
        ax2 = plt.subplot(3, 1, 2)
        alineacion = analisis['alineacion']['porcentaje']
        
        # Gauge chart simplificado
        theta = (alineacion / 100) * 180  # 0-180 grados
        colors_gauge = ['#FF0000', '#FF8C00', '#FFD700', '#9ACD32', '#228B22']
        
        for i, color in enumerate(colors_gauge):
            start = i * 36
            end = (i + 1) * 36
            ax2.barh(0, 36, left=start, height=0.3, color=color, alpha=0.7)
        
        # Indicador
        ax2.plot([alineacion * 1.8, alineacion * 1.8], [-0.2, 0.5], 
                'k-', linewidth=3, marker='v', markersize=10)
        
        ax2.set_xlim(0, 180)
        ax2.set_ylim(-0.3, 0.6)
        ax2.set_title(f'Alineación Holística: {alineacion}%', 
                     fontsize=12, fontweight='bold')
        ax2.axis('off')
        
        ax2.text(0, -0.25, '0%', ha='center', fontsize=9)
        ax2.text(90, -0.25, '50%', ha='center', fontsize=9)
        ax2.text(180, -0.25, '100%', ha='center', fontsize=9)
        
        # Gráfico 3: Distribución de energías
        ax3 = plt.subplot(3, 1, 3)
        
        expresion = analisis['numero_expresion']
        destino = analisis['numero_destino']
        tikun = analisis['tikun']
        
        labels = ['Expresión\n(Quién Eres)', 'Destino\n(Tu Camino)', 'Tikun\n(Tu Lección)']
        sizes = [expresion, destino, max(tikun, 1)]  # Evitar 0
        colors_pie = ['#FF6347', '#4169E1', '#9370DB']
        explode = (0.1, 0.1, 0.1)
        
        ax3.pie(sizes, explode=explode, labels=labels, colors=colors_pie,
               autopct='%1.0f', startangle=90, textprops={'fontsize': 10})
        ax3.set_title('Distribución de Energías Numerológicas', 
                     fontsize=12, fontweight='bold')
        
        plt.tight_layout()
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
    
    def _crear_pagina_anio_personal(self, pdf, analisis: Dict):
        """Crea página con año personal y predicciones"""
        fig = plt.figure(figsize=(8.5, 11))
        ax = fig.add_subplot(111)
        ax.axis('off')
        
        # Calcular año personal
        vib_fecha = analisis['vibracion_fecha']
        anio_actual = datetime.now().year
        calc_anio = CalculadorAnioPersonal()
        anio_personal = calc_anio.calcular_anio_personal(
            vib_fecha['dia'], vib_fecha['mes'], anio_actual
        )
        
        # Calcular edad y ciclos
        fecha_nac = vib_fecha['fecha_obj']
        edad = anio_actual - fecha_nac.year
        ciclos = calc_anio.obtener_ciclos_vida(edad)
        
        # Título
        ax.text(0.5, 0.95, f'AÑO PERSONAL {anio_actual}', 
               ha='center', va='top', fontsize=18, fontweight='bold',
               transform=ax.transAxes, color='#4B0082')
        
        y_pos = 0.88
        line_height = 0.04
        
        # Año personal
        ax.text(0.1, y_pos, f'Tu Año Personal: {anio_personal}', 
               fontsize=14, fontweight='bold', transform=ax.transAxes, color='#8B008B')
        y_pos -= line_height * 1.5
        
        consejo_anual = self.interpretaciones.obtener_consejo_anual(anio_personal)
        consejo_lines = self._wrap_text(consejo_anual, 70)
        for line in consejo_lines:
            ax.text(0.1, y_pos, line, fontsize=11, transform=ax.transAxes)
            y_pos -= line_height
        y_pos -= line_height
        
        # Ciclos de vida
        ax.text(0.1, y_pos, 'CICLOS DE VIDA', fontsize=14, fontweight='bold',
               transform=ax.transAxes, color='#8B008B')
        y_pos -= line_height
        
        ax.text(0.1, y_pos, f"Edad actual: {edad} años", 
               fontsize=11, transform=ax.transAxes)
        y_pos -= line_height
        
        ax.text(0.1, y_pos, f"Ciclo actual: {ciclos['ciclo']}", 
               fontsize=11, transform=ax.transAxes)
        y_pos -= line_height
        
        ax.text(0.1, y_pos, f"Año {ciclos['anio_en_ciclo']} del ciclo de 9 años", 
               fontsize=11, transform=ax.transAxes)
        y_pos -= line_height * 2
        
        # Interpretación del ciclo
        ax.text(0.1, y_pos, 'Interpretación del Ciclo:', fontsize=12, fontweight='bold',
               transform=ax.transAxes, color='#4B0082')
        y_pos -= line_height
        
        interp_ciclo = self._obtener_interpretacion_ciclo(ciclos['anio_en_ciclo'])
        interp_lines = self._wrap_text(interp_ciclo, 70)
        for line in interp_lines:
            ax.text(0.1, y_pos, line, fontsize=10, transform=ax.transAxes)
            y_pos -= line_height * 0.9
        y_pos -= line_height
        
        # Recomendaciones
        ax.text(0.1, y_pos, 'RECOMENDACIONES PARA ESTE AÑO', fontsize=14, 
               fontweight='bold', transform=ax.transAxes, color='#8B008B')
        y_pos -= line_height
        
        recomendaciones = self._obtener_recomendaciones_anio(anio_personal)
        for i, rec in enumerate(recomendaciones, 1):
            ax.text(0.1, y_pos, f"{i}.", fontsize=11, fontweight='bold',
                   transform=ax.transAxes)
            rec_lines = self._wrap_text(rec, 65)
            for j, line in enumerate(rec_lines):
                x_offset = 0.15 if j > 0 else 0.13
                ax.text(x_offset, y_pos, line, fontsize=10, transform=ax.transAxes)
                y_pos -= line_height * 0.85
            y_pos -= line_height * 0.3
        
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
    
    def _wrap_text(self, text: str, width: int) -> List[str]:
        """Divide texto en líneas de ancho específico"""
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + 1 <= width:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def _obtener_interpretacion_ciclo(self, anio_ciclo: int) -> str:
        """Obtiene interpretación del año dentro del ciclo de 9 años"""
        interpretaciones = {
            1: "Año de nuevos comienzos y siembra. Es momento de iniciar proyectos y tomar iniciativas.",
            2: "Año de gestación y paciencia. Los proyectos iniciados necesitan tiempo para desarrollarse.",
            3: "Año de expansión y creatividad. Momento de expresar y comunicar tus ideas.",
            4: "Año de consolidación y trabajo. Construye bases sólidas para el futuro.",
            5: "Año de cambios y libertad. Momento de adaptarse y explorar nuevas posibilidades.",
            6: "Año de responsabilidad y amor. Enfócate en relaciones y armonía.",
            7: "Año de introspección y sabiduría. Tiempo para estudiar y conectar con tu interior.",
            8: "Año de cosecha y logros. Momento de materializar y obtener resultados.",
            9: "Año de culminación y cierre. Completa ciclos y prepárate para lo nuevo."
        }
        return interpretaciones.get(anio_ciclo, "Año de integración y balance.")
    
    def _obtener_recomendaciones_anio(self, anio_personal: int) -> List[str]:
        """Obtiene recomendaciones específicas para el año personal"""
        recomendaciones = {
            1: [
                "Inicia ese proyecto que has estado postergando",
                "Toma decisiones con confianza y liderazgo",
                "Cultiva tu independencia y originalidad"
            ],
            2: [
                "Practica la paciencia y la diplomacia",
                "Fortalece tus relaciones y colaboraciones",
                "Desarrolla tu intuición y sensibilidad"
            ],
            3: [
                "Expresa tu creatividad en todas sus formas",
                "Socializa y comunica tus ideas",
                "Disfruta y mantén una actitud optimista"
            ],
            4: [
                "Organiza tu vida y establece rutinas",
                "Trabaja con disciplina en tus metas",
                "Construye bases sólidas para el futuro"
            ],
            5: [
                "Abraza los cambios con flexibilidad",
                "Viaja y experimenta cosas nuevas",
                "Libera lo que ya no te sirve"
            ],
            6: [
                "Cuida tus relaciones familiares y de pareja",
                "Asume responsabilidades con amor",
                "Crea armonía en tu hogar y entorno"
            ],
            7: [
                "Dedica tiempo a la meditación y estudio",
                "Busca respuestas en tu interior",
                "Perfecciona tus habilidades y conocimientos"
            ],
            8: [
                "Enfócate en tus metas materiales y profesionales",
                "Ejerce liderazgo con integridad",
                "Cosecha los frutos de tu trabajo"
            ],
            9: [
                "Completa proyectos pendientes",
                "Suelta el pasado con gratitud",
                "Prepárate para un nuevo ciclo de 9 años"
            ]
        }
        return recomendaciones.get(anio_personal, [
            "Mantén el equilibrio en todas las áreas",
            "Confía en el proceso de la vida",
            "Actúa con consciencia y amor"
        ])
    
    def generar_reporte_compatibilidad(self, persona1: Dict, persona2: Dict,
                                      output_file: str = "compatibilidad.pdf") -> str:
        """Genera reporte de compatibilidad entre dos personas"""
        from matplotlib.backends.backend_pdf import PdfPages
        
        # Calcular compatibilidad
        compatibilidad = self.calculator.calcular_compatibilidad(persona1, persona2)
        
        with PdfPages(output_file) as pdf:
            fig = plt.figure(figsize=(8.5, 11))
            ax = fig.add_subplot(111)
            ax.axis('off')
            
            # Título
            ax.text(0.5, 0.95, 'ANÁLISIS DE COMPATIBILIDAD', 
                   ha='center', va='top', fontsize=18, fontweight='bold',
                   transform=ax.transAxes, color='#4B0082')
            
            y_pos = 0.88
            line_height = 0.04
            
            # Nombres
            ax.text(0.5, y_pos, f"{persona1['nombre']} & {persona2['nombre']}", 
                   ha='center', fontsize=14, fontweight='bold',
                   transform=ax.transAxes, color='#8B008B')
            y_pos -= line_height * 2
            
            # Compatibilidad total
            comp_total = compatibilidad['compatibilidad_total']
            color_comp = '#228B22' if comp_total >= 70 else '#FF8C00' if comp_total >= 50 else '#8B0000'
            
            ax.text(0.5, y_pos, f"Compatibilidad Total: {comp_total}%", 
                   ha='center', fontsize=16, fontweight='bold',
                   transform=ax.transAxes, color=color_comp)
            y_pos -= line_height
            
            ax.text(0.5, y_pos, f"Nivel: {compatibilidad['nivel']}", 
                   ha='center', fontsize=13,
                   transform=ax.transAxes, color=color_comp)
            y_pos -= line_height * 2
            
            # Detalles
            detalles = [
                ('Sendero del Alma', f"{compatibilidad['sendero1']} - {compatibilidad['sendero2']}", 
                 f"{compatibilidad['compatibilidad_sendero']}%"),
                ('Expresión', f"{persona1['numero_expresion']} - {persona2['numero_expresion']}", 
                 f"{compatibilidad['compatibilidad_expresion']}%"),
                ('Destino', f"{persona1['numero_destino']} - {persona2['numero_destino']}", 
                 f"{compatibilidad['compatibilidad_destino']}%"),
            ]
            
            for titulo, valores, porcentaje in detalles:
                ax.text(0.1, y_pos, f"{titulo}:", fontsize=12, fontweight='bold',
                       transform=ax.transAxes)
                ax.text(0.4, y_pos, valores, fontsize=11, transform=ax.transAxes)
                ax.text(0.7, y_pos, porcentaje, fontsize=11, fontweight='bold',
                       transform=ax.transAxes, color=color_comp)
                y_pos -= line_height * 1.5
            
            # Interpretación
            y_pos -= line_height
            ax.text(0.1, y_pos, 'INTERPRETACIÓN:', fontsize=13, fontweight='bold',
                   transform=ax.transAxes, color='#4B0082')
            y_pos -= line_height
            
            texto_comp = self.interpretaciones.obtener_compatibilidad_texto(
                compatibilidad['nivel'], comp_total
            )
            comp_lines = self._wrap_text(texto_comp, 70)
            for line in comp_lines:
                ax.text(0.1, y_pos, line, fontsize=11, transform=ax.transAxes)
                y_pos -= line_height
            
            pdf.savefig(fig, bbox_inches='tight')
            plt.close()
        
        return output_file
