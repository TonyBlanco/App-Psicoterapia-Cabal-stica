"""
Árbol de la Vida Cabalístico - Sephirot y Senderos
Representación de las 10 Sephirot y 22 Senderos
"""

import math
from typing import List, Tuple, Dict

class ArbolDeLaVida:
    """Representación del Árbol de la Vida cabalístico"""
    
    # Las 10 Sephirot con sus atributos
    SEPHIROT = {
        1: {
            'nombre': 'Kether',
            'significado': 'Corona',
            'atributo': 'Voluntad Divina',
            'mundo': 'Atziluth (Emanación)',
            'color': '#FFFFFF',
            'posicion': (400, 50),  # x, y para visualización
            'descripcion': 'La Corona Suprema, fuente de toda creación'
        },
        2: {
            'nombre': 'Chokmah',
            'significado': 'Sabiduría',
            'atributo': 'Sabiduría Primordial',
            'mundo': 'Atziluth (Emanación)',
            'color': '#808080',
            'posicion': (250, 150),
            'descripcion': 'Sabiduría divina, principio masculino activo'
        },
        3: {
            'nombre': 'Binah',
            'significado': 'Entendimiento',
            'atributo': 'Comprensión',
            'mundo': 'Atziluth (Emanación)',
            'color': '#000000',
            'posicion': (550, 150),
            'descripcion': 'Entendimiento divino, principio femenino receptivo'
        },
        4: {
            'nombre': 'Chesed',
            'significado': 'Misericordia',
            'atributo': 'Amor y Bondad',
            'mundo': 'Briah (Creación)',
            'color': '#0000FF',
            'posicion': (250, 280),
            'descripcion': 'Misericordia, amor incondicional, expansión'
        },
        5: {
            'nombre': 'Geburah',
            'significado': 'Severidad',
            'atributo': 'Fuerza y Justicia',
            'mundo': 'Briah (Creación)',
            'color': '#FF0000',
            'posicion': (550, 280),
            'descripcion': 'Severidad, justicia, disciplina, contracción'
        },
        6: {
            'nombre': 'Tiphareth',
            'significado': 'Belleza',
            'atributo': 'Armonía y Balance',
            'mundo': 'Briah (Creación)',
            'color': '#FFD700',
            'posicion': (400, 350),
            'descripcion': 'Belleza, armonía, centro del Árbol, el Yo Superior'
        },
        7: {
            'nombre': 'Netzach',
            'significado': 'Victoria',
            'atributo': 'Eternidad',
            'mundo': 'Yetzirah (Formación)',
            'color': '#00FF00',
            'posicion': (250, 480),
            'descripcion': 'Victoria, emociones, instintos, naturaleza'
        },
        8: {
            'nombre': 'Hod',
            'significado': 'Gloria',
            'atributo': 'Esplendor',
            'mundo': 'Yetzirah (Formación)',
            'color': '#FFA500',
            'posicion': (550, 480),
            'descripcion': 'Gloria, intelecto, comunicación, magia'
        },
        9: {
            'nombre': 'Yesod',
            'significado': 'Fundamento',
            'atributo': 'Fundación',
            'mundo': 'Yetzirah (Formación)',
            'color': '#9400D3',
            'posicion': (400, 580),
            'descripcion': 'Fundamento, subconsciente, mundo astral'
        },
        10: {
            'nombre': 'Malkuth',
            'significado': 'Reino',
            'atributo': 'Reino Material',
            'mundo': 'Assiah (Acción)',
            'color': '#8B4513',
            'posicion': (400, 700),
            'descripcion': 'Reino, mundo físico, manifestación material'
        }
    }
    
    # Los 22 Senderos que conectan las Sephirot
    SENDEROS = [
        {'numero': 1, 'desde': 1, 'hasta': 2, 'letra': 'Aleph', 'tarot': 'El Loco'},
        {'numero': 2, 'desde': 1, 'hasta': 3, 'letra': 'Beth', 'tarot': 'El Mago'},
        {'numero': 3, 'desde': 1, 'hasta': 6, 'letra': 'Gimel', 'tarot': 'La Sacerdotisa'},
        {'numero': 4, 'desde': 2, 'hasta': 3, 'letra': 'Daleth', 'tarot': 'La Emperatriz'},
        {'numero': 5, 'desde': 2, 'hasta': 6, 'letra': 'Heh', 'tarot': 'El Emperador'},
        {'numero': 6, 'desde': 2, 'hasta': 4, 'letra': 'Vav', 'tarot': 'El Hierofante'},
        {'numero': 7, 'desde': 3, 'hasta': 6, 'letra': 'Zayin', 'tarot': 'Los Enamorados'},
        {'numero': 8, 'desde': 3, 'hasta': 5, 'letra': 'Chet', 'tarot': 'El Carro'},
        {'numero': 9, 'desde': 4, 'hasta': 5, 'letra': 'Teth', 'tarot': 'La Fuerza'},
        {'numero': 10, 'desde': 4, 'hasta': 6, 'letra': 'Yod', 'tarot': 'El Ermitaño'},
        {'numero': 11, 'desde': 4, 'hasta': 7, 'letra': 'Kaph', 'tarot': 'La Rueda'},
        {'numero': 12, 'desde': 5, 'hasta': 6, 'letra': 'Lamed', 'tarot': 'La Justicia'},
        {'numero': 13, 'desde': 5, 'hasta': 8, 'letra': 'Mem', 'tarot': 'El Colgado'},
        {'numero': 14, 'desde': 6, 'hasta': 7, 'letra': 'Nun', 'tarot': 'La Muerte'},
        {'numero': 15, 'desde': 6, 'hasta': 8, 'letra': 'Samekh', 'tarot': 'La Templanza'},
        {'numero': 16, 'desde': 6, 'hasta': 9, 'letra': 'Ayin', 'tarot': 'El Diablo'},
        {'numero': 17, 'desde': 7, 'hasta': 8, 'letra': 'Peh', 'tarot': 'La Torre'},
        {'numero': 18, 'desde': 7, 'hasta': 9, 'letra': 'Tzaddi', 'tarot': 'La Estrella'},
        {'numero': 19, 'desde': 7, 'hasta': 10, 'letra': 'Qoph', 'tarot': 'La Luna'},
        {'numero': 20, 'desde': 8, 'hasta': 9, 'letra': 'Resh', 'tarot': 'El Sol'},
        {'numero': 21, 'desde': 8, 'hasta': 10, 'letra': 'Shin', 'tarot': 'El Juicio'},
        {'numero': 22, 'desde': 9, 'hasta': 10, 'letra': 'Tav', 'tarot': 'El Mundo'}
    ]
    
    def __init__(self):
        pass
    
    @classmethod
    def obtener_sephira(cls, numero: int) -> Dict:
        """Obtiene información de una Sephira específica"""
        return cls.SEPHIROT.get(numero, cls.SEPHIROT[1])
    
    @classmethod
    def obtener_sendero(cls, numero: int) -> Dict:
        """Obtiene información de un sendero específico"""
        for sendero in cls.SENDEROS:
            if sendero['numero'] == numero:
                return sendero
        return cls.SENDEROS[0]
    
    @classmethod
    def obtener_sephirot_conectadas(cls, numero_sendero: int) -> Tuple[Dict, Dict]:
        """Obtiene las dos Sephirot que conecta un sendero"""
        sendero = cls.obtener_sendero(numero_sendero)
        sephira1 = cls.obtener_sephira(sendero['desde'])
        sephira2 = cls.obtener_sephira(sendero['hasta'])
        return sephira1, sephira2
    
    @classmethod
    def calcular_camino_espiritual(cls, vibracion: int) -> List[Dict]:
        """
        Calcula el camino espiritual basado en la vibración
        Retorna las Sephirot que debe trabajar la persona
        """
        # Mapeo de vibraciones a Sephirot principales
        mapeo = {
            1: [1, 2],      # Kether, Chokmah
            2: [2, 3],      # Chokmah, Binah
            3: [3, 6],      # Binah, Tiphareth
            4: [4, 6],      # Chesed, Tiphareth
            5: [5, 6],      # Geburah, Tiphareth
            6: [6],         # Tiphareth (centro)
            7: [7, 9],      # Netzach, Yesod
            8: [8, 9],      # Hod, Yesod
            9: [9, 10],     # Yesod, Malkuth
            10: [10],       # Malkuth
            11: [1, 6],     # Kether, Tiphareth (maestro)
            12: [6, 9],     # Tiphareth, Yesod
            13: [5, 8],     # Geburah, Hod
            14: [6, 7],     # Tiphareth, Netzach
            15: [8, 9],     # Hod, Yesod
            16: [7, 8],     # Netzach, Hod
            17: [7, 9],     # Netzach, Yesod
            18: [7, 10],    # Netzach, Malkuth
            19: [8, 9],     # Hod, Yesod
            20: [8, 10],    # Hod, Malkuth
            21: [9, 10],    # Yesod, Malkuth
            22: [1, 10]     # Kether, Malkuth (maestro constructor)
        }
        
        sephirot_numeros = mapeo.get(vibracion, [6])  # Default: Tiphareth
        return [cls.obtener_sephira(num) for num in sephirot_numeros]
    
    @classmethod
    def obtener_pilar(cls, sephira_numero: int) -> str:
        """Determina a qué pilar pertenece una Sephira"""
        pilar_izquierdo = [3, 5, 8]  # Pilar de la Severidad
        pilar_derecho = [2, 4, 7]    # Pilar de la Misericordia
        pilar_medio = [1, 6, 9, 10]  # Pilar del Equilibrio
        
        if sephira_numero in pilar_izquierdo:
            return "Pilar de la Severidad (Femenino)"
        elif sephira_numero in pilar_derecho:
            return "Pilar de la Misericordia (Masculino)"
        else:
            return "Pilar del Equilibrio (Neutral)"
    
    @classmethod
    def obtener_triada(cls, sephira_numero: int) -> str:
        """Determina a qué tríada pertenece una Sephira"""
        if sephira_numero == 1:
            return "Supernal (Divina)"
        elif sephira_numero in [2, 3]:
            return "Supernal (Divina)"
        elif sephira_numero in [4, 5, 6]:
            return "Ética (Moral)"
        elif sephira_numero in [7, 8, 9]:
            return "Astral (Psicológica)"
        else:
            return "Material (Física)"
    
    @classmethod
    def generar_coordenadas_arbol(cls, ancho: int = 800, alto: int = 800) -> Dict:
        """
        Genera coordenadas escaladas para dibujar el Árbol de la Vida
        """
        # Escalar las posiciones originales al tamaño deseado
        factor_x = ancho / 800
        factor_y = alto / 800
        
        coordenadas = {}
        for num, sephira in cls.SEPHIROT.items():
            x, y = sephira['posicion']
            coordenadas[num] = {
                'x': x * factor_x,
                'y': y * factor_y,
                'nombre': sephira['nombre'],
                'color': sephira['color']
            }
        
        return coordenadas
    
    @classmethod
    def obtener_conexiones(cls) -> List[Tuple[int, int]]:
        """Retorna lista de conexiones entre Sephirot para dibujar"""
        return [(s['desde'], s['hasta']) for s in cls.SENDEROS]
    
    @classmethod
    def analisis_completo_sephira(cls, numero: int) -> Dict:
        """Análisis completo de una Sephira"""
        sephira = cls.obtener_sephira(numero)
        pilar = cls.obtener_pilar(numero)
        triada = cls.obtener_triada(numero)
        
        # Encontrar senderos conectados
        senderos_conectados = []
        for sendero in cls.SENDEROS:
            if sendero['desde'] == numero or sendero['hasta'] == numero:
                senderos_conectados.append(sendero)
        
        return {
            'sephira': sephira,
            'pilar': pilar,
            'triada': triada,
            'senderos_conectados': senderos_conectados,
            'numero_senderos': len(senderos_conectados)
        }


class CalculadorAnioPersonal:
    """Calcula el año personal para predicciones anuales"""
    
    @staticmethod
    def calcular_anio_personal(dia: int, mes: int, anio_actual: int) -> int:
        """
        Calcula el año personal sumando día + mes + año actual
        y reduciendo a un dígito (1-9)
        """
        suma = dia + mes + anio_actual
        while suma > 9:
            suma = sum(int(d) for d in str(suma))
        return suma
    
    @staticmethod
    def calcular_mes_personal(anio_personal: int, mes_actual: int) -> int:
        """Calcula el mes personal"""
        suma = anio_personal + mes_actual
        while suma > 9:
            suma = sum(int(d) for d in str(suma))
        return suma
    
    @staticmethod
    def obtener_ciclos_vida(edad: int) -> Dict:
        """
        Calcula los ciclos de vida (cada 9 años)
        """
        ciclo_actual = (edad // 9) + 1
        anio_en_ciclo = (edad % 9) + 1
        
        return {
            'ciclo': ciclo_actual,
            'anio_en_ciclo': anio_en_ciclo,
            'descripcion': f"Ciclo {ciclo_actual}, Año {anio_en_ciclo} del ciclo"
        }
