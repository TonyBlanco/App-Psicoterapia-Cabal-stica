"""
Módulo de Cálculos Numerológicos Cabalísticos
Sistema Pitagórico adaptado a la Cábala Hebrea
"""

from datetime import datetime
from typing import Tuple, Dict

class CabalaCalculator:
    """Calculadora de numerología cabalística"""
    
    # Tabla Pitagórica para conversión de letras
    PYTHAGOREAN_TABLE = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
        'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8,
        'Ñ': 5  # Letra española
    }
    
    # Números maestros que no se reducen
    MASTER_NUMBERS = [11, 22]
    
    def __init__(self):
        pass
    
    def calcular_vibracion_nombre(self, nombre: str) -> Dict:
        """
        Calcula la vibración numerológica de un nombre
        
        Args:
            nombre: Nombre completo en mayúsculas
            
        Returns:
            Dict con vibración, proceso de cálculo y detalles
        """
        nombre_limpio = ''.join(c for c in nombre.upper() if c.isalpha() or c.isspace())
        
        valores = []
        proceso = []
        
        for letra in nombre_limpio:
            if letra in self.PYTHAGOREAN_TABLE:
                valor = self.PYTHAGOREAN_TABLE[letra]
                valores.append(valor)
                proceso.append(f"{letra}={valor}")
        
        suma_total = sum(valores)
        vibracion_reducida = self._reducir_numero(suma_total)
        
        return {
            'nombre': nombre,
            'nombre_limpio': nombre_limpio,
            'valores': valores,
            'proceso': ' + '.join(proceso),
            'suma_total': suma_total,
            'vibracion': vibracion_reducida,
            'es_maestro': vibracion_reducida in self.MASTER_NUMBERS
        }
    
    def calcular_vibracion_fecha(self, fecha: str) -> Dict:
        """
        Calcula la vibración de una fecha de nacimiento
        
        Args:
            fecha: Fecha en formato DD/MM/AAAA
            
        Returns:
            Dict con vibración y detalles del cálculo
        """
        try:
            # Parsear fecha
            if '/' in fecha:
                dia, mes, anio = map(int, fecha.split('/'))
            elif '-' in fecha:
                anio, mes, dia = map(int, fecha.split('-'))
            else:
                raise ValueError("Formato de fecha inválido")
            
            # Validar fecha
            fecha_obj = datetime(anio, mes, dia)
            
            # Calcular vibraciones individuales
            vib_dia = self._reducir_numero(dia)
            vib_mes = self._reducir_numero(mes)
            vib_anio = self._reducir_numero(anio)
            
            # Suma total
            suma_total = dia + mes + anio
            vibracion_total = self._reducir_numero(suma_total)
            
            return {
                'fecha': fecha,
                'fecha_obj': fecha_obj,
                'dia': dia,
                'mes': mes,
                'anio': anio,
                'vibracion_dia': vib_dia,
                'vibracion_mes': vib_mes,
                'vibracion_anio': vib_anio,
                'suma_total': suma_total,
                'vibracion': vibracion_total,
                'es_maestro': vibracion_total in self.MASTER_NUMBERS
            }
        except Exception as e:
            raise ValueError(f"Error al procesar fecha: {str(e)}")
    
    def calcular_sendero_alma(self, nombre: str, fecha: str) -> Dict:
        """
        Calcula el Sendero del Alma (combinación holística)
        
        Args:
            nombre: Nombre completo
            fecha: Fecha de nacimiento DD/MM/AAAA
            
        Returns:
            Dict con análisis completo del sendero del alma
        """
        vib_nombre = self.calcular_vibracion_nombre(nombre)
        vib_fecha = self.calcular_vibracion_fecha(fecha)
        
        # Sendero del Alma: combinación de ambas vibraciones
        sendero = (vib_nombre['vibracion'] + vib_fecha['vibracion'])
        sendero_reducido = self._reducir_numero_22(sendero)  # Reducir a 1-22
        
        # Número de Expresión (solo nombre)
        expresion = vib_nombre['vibracion']
        
        # Número de Destino (solo fecha)
        destino = vib_fecha['vibracion']
        
        # Tikun (corrección kármica): diferencia entre expresión y destino
        tikun = abs(expresion - destino)
        
        return {
            'nombre': nombre,
            'fecha': fecha,
            'vibracion_nombre': vib_nombre,
            'vibracion_fecha': vib_fecha,
            'sendero_alma': sendero_reducido,
            'numero_expresion': expresion,
            'numero_destino': destino,
            'tikun': tikun,
            'alineacion': self._calcular_alineacion(expresion, destino)
        }
    
    def calcular_compatibilidad(self, persona1: Dict, persona2: Dict) -> Dict:
        """
        Calcula la compatibilidad entre dos personas
        
        Args:
            persona1: Datos del sendero del alma de persona 1
            persona2: Datos del sendero del alma de persona 2
            
        Returns:
            Dict con análisis de compatibilidad
        """
        sendero1 = persona1['sendero_alma']
        sendero2 = persona2['sendero_alma']
        
        # Diferencia entre senderos
        diferencia = abs(sendero1 - sendero2)
        
        # Compatibilidad basada en diferencia
        if diferencia == 0:
            compatibilidad = 100
            nivel = "Perfecta"
        elif diferencia <= 2:
            compatibilidad = 90
            nivel = "Excelente"
        elif diferencia <= 4:
            compatibilidad = 75
            nivel = "Muy Buena"
        elif diferencia <= 6:
            compatibilidad = 60
            nivel = "Buena"
        elif diferencia <= 9:
            compatibilidad = 45
            nivel = "Regular"
        else:
            compatibilidad = 30
            nivel = "Desafiante"
        
        # Compatibilidad de expresión
        expr_diff = abs(persona1['numero_expresion'] - persona2['numero_expresion'])
        compatibilidad_expresion = max(0, 100 - (expr_diff * 10))
        
        # Compatibilidad de destino
        dest_diff = abs(persona1['numero_destino'] - persona2['numero_destino'])
        compatibilidad_destino = max(0, 100 - (dest_diff * 10))
        
        # Promedio ponderado
        compatibilidad_total = (compatibilidad * 0.5 + 
                               compatibilidad_expresion * 0.25 + 
                               compatibilidad_destino * 0.25)
        
        return {
            'persona1': persona1['nombre'],
            'persona2': persona2['nombre'],
            'sendero1': sendero1,
            'sendero2': sendero2,
            'diferencia_senderos': diferencia,
            'compatibilidad_sendero': compatibilidad,
            'compatibilidad_expresion': compatibilidad_expresion,
            'compatibilidad_destino': compatibilidad_destino,
            'compatibilidad_total': round(compatibilidad_total, 1),
            'nivel': nivel,
            'armonia': compatibilidad_total >= 70
        }
    
    def _reducir_numero(self, numero: int) -> int:
        """
        Reduce un número a un solo dígito (1-9) o número maestro (11, 22)
        """
        while numero > 9 and numero not in self.MASTER_NUMBERS:
            numero = sum(int(d) for d in str(numero))
        return numero
    
    def _reducir_numero_22(self, numero: int) -> int:
        """
        Reduce un número al rango 1-22 (para senderos cabalísticos)
        """
        while numero > 22:
            numero = sum(int(d) for d in str(numero))
            if numero > 22:
                numero = numero % 22
                if numero == 0:
                    numero = 22
        return numero
    
    def _calcular_alineacion(self, expresion: int, destino: int) -> Dict:
        """
        Calcula el nivel de alineación entre expresión y destino
        """
        diferencia = abs(expresion - destino)
        
        if diferencia == 0:
            porcentaje = 100
            estado = "Perfectamente Alineado"
        elif diferencia == 1:
            porcentaje = 95
            estado = "Altamente Armonizado"
        elif diferencia == 2:
            porcentaje = 85
            estado = "Bien Alineado"
        elif diferencia <= 4:
            porcentaje = 70
            estado = "Alineación Moderada"
        else:
            porcentaje = 50
            estado = "Requiere Trabajo Interior"
        
        return {
            'porcentaje': porcentaje,
            'estado': estado,
            'diferencia': diferencia
        }


# Funciones de utilidad
def validar_nombre(nombre: str) -> bool:
    """Valida que el nombre tenga al menos 2 caracteres alfabéticos"""
    nombre_limpio = ''.join(c for c in nombre if c.isalpha())
    return len(nombre_limpio) >= 2


def validar_fecha(fecha: str) -> bool:
    """Valida formato de fecha DD/MM/AAAA o AAAA-MM-DD"""
    try:
        if '/' in fecha:
            dia, mes, anio = map(int, fecha.split('/'))
        elif '-' in fecha:
            anio, mes, dia = map(int, fecha.split('-'))
        else:
            return False
        
        datetime(anio, mes, dia)
        return True
    except:
        return False
