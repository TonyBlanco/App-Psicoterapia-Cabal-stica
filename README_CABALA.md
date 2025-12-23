# Sistema de Astrología Cabalística Interpretativa

## 📖 Descripción

Sistema completo de análisis numerológico y cabalístico basado en el Árbol de la Vida de la Cábala Hebrea. Combina numerología pitagórica con interpretaciones cabalísticas profundas para ofrecer análisis personalizados del sendero espiritual.

## ✨ Características

### 🔢 Cálculos Numerológicos
- **Vibración del Nombre**: Análisis pitagórico del nombre completo
- **Vibración de la Fecha**: Análisis de la fecha de nacimiento
- **Sendero del Alma**: Combinación holística de ambas vibraciones
- **Número de Expresión**: Quién eres en esencia
- **Número de Destino**: Tu camino de vida
- **Tikun**: Corrección kármica personal

### 🌳 Árbol de la Vida
- **10 Sephirot**: Emanaciones divinas con interpretaciones completas
- **22 Senderos**: Caminos entre las Sephirot
- **3 Pilares**: Misericordia, Severidad y Equilibrio
- **4 Mundos**: Atziluth, Briah, Yetzirah, Assiah

### 💕 Compatibilidad
- Análisis entre dos personas
- Compatibilidad de Sendero del Alma
- Compatibilidad de Expresión y Destino
- Porcentajes y niveles de armonía

### 📅 Predicciones
- Año Personal (ciclos de 9 años)
- Mes Personal
- Ciclos de Vida
- Recomendaciones anuales

### 📄 Reportes PDF
- Portada personalizada
- Árbol de la Vida visualizado
- Análisis numerológico detallado
- Interpretaciones cabalísticas
- Gráficos de vibraciones
- Predicciones anuales

## 🚀 Instalación

### Requisitos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

2. **Verificar instalación**:
```bash
python3 main.py
```

## 💻 Uso

### Modo Interactivo (CLI)

Ejecutar el programa principal:
```bash
python3 main.py
```

### Menú Principal

```
1. Análisis Individual Completo
2. Cálculo Rápido de Vibración
3. Análisis de Compatibilidad (2 personas)
4. Consultar Interpretación de un Número
5. Ver Árbol de la Vida (Sephirot)
6. Calcular Año Personal
7. Generar Reporte PDF
8. Ayuda
0. Salir
```

### Ejemplos de Uso

#### Análisis Individual
```python
from cabala_calculator import CabalaCalculator

calc = CabalaCalculator()
analisis = calc.calcular_sendero_alma("JUAN PEREZ", "01/08/1959")

print(f"Sendero del Alma: {analisis['sendero_alma']}")
print(f"Número de Expresión: {analisis['numero_expresion']}")
print(f"Número de Destino: {analisis['numero_destino']}")
```

#### Generar Reporte PDF
```python
from report_generator import GeneradorReportePDF

generador = GeneradorReportePDF()
generador.generar_reporte_completo(
    nombre="JUAN PEREZ",
    fecha="01/08/1959",
    output_file="mi_reporte.pdf"
)
```

#### Análisis de Compatibilidad
```python
from cabala_calculator import CabalaCalculator

calc = CabalaCalculator()

persona1 = calc.calcular_sendero_alma("MARIA GARCIA", "15/03/1985")
persona2 = calc.calcular_sendero_alma("CARLOS LOPEZ", "22/11/1983")

compatibilidad = calc.calcular_compatibilidad(persona1, persona2)
print(f"Compatibilidad: {compatibilidad['compatibilidad_total']}%")
```

## 📚 Módulos

### `cabala_calculator.py`
Cálculos numerológicos principales:
- Conversión pitagórica de letras a números
- Reducción de números (1-9, 11, 22)
- Cálculo de vibraciones
- Análisis de compatibilidad

### `interpretaciones.py`
Base de datos de interpretaciones:
- 22 vibraciones/senderos completos
- Arquetipos y significados
- Aspectos de luz y sombra
- Lecciones kármicas
- Consejos espirituales

### `sephirot.py`
Árbol de la Vida cabalístico:
- 10 Sephirot con atributos
- 22 Senderos conectores
- Pilares y tríadas
- Cálculo de año personal
- Ciclos de vida

### `report_generator.py`
Generación de reportes PDF:
- Visualización del Árbol de la Vida
- Gráficos de vibraciones
- Análisis completo en PDF
- Reportes de compatibilidad

### `main.py`
Interfaz CLI interactiva:
- Menú principal
- Flujos de análisis
- Generación de reportes
- Sistema de ayuda

## 🔮 Interpretaciones

### Las 22 Vibraciones

1. **El Mago (Aleph)** - Inicio, liderazgo, creatividad
2. **La Sacerdotisa (Beth)** - Intuición, receptividad, misterio
3. **La Emperatriz (Gimel)** - Creatividad, abundancia, expresión
4. **El Emperador (Daleth)** - Estructura, orden, disciplina
5. **El Hierofante (Heh)** - Libertad, cambio, aventura
6. **Los Enamorados (Vav)** - Amor, armonía, elección
7. **El Carro (Zayin)** - Búsqueda interior, análisis
8. **La Justicia (Chet)** - Poder, manifestación, karma
9. **El Ermitaño (Teth)** - Compasión universal, sabiduría
10. **La Rueda (Yod)** - Ciclos, cambio, destino
11. **La Fuerza (Kaph)** - Iluminación, maestría (Maestro)
12. **El Colgado (Lamed)** - Sacrificio, nueva perspectiva
13. **La Muerte (Mem)** - Transformación, renacimiento
14. **La Templanza (Nun)** - Equilibrio, alquimia
15. **El Diablo (Samekh)** - Sombra, poder instintivo
16. **La Torre (Ayin)** - Destrucción necesaria, revelación
17. **La Estrella (Peh)** - Esperanza, inspiración
18. **La Luna (Tzaddi)** - Intuición profunda, misterio
19. **El Sol (Qoph)** - Claridad, éxito, vitalidad
20. **El Juicio (Resh)** - Renacimiento, despertar
21. **El Mundo (Shin)** - Culminación, totalidad
22. **El Loco (Tav)** - Constructor maestro (Maestro)

### Las 10 Sephirot

1. **Kether** - Corona, voluntad divina
2. **Chokmah** - Sabiduría primordial
3. **Binah** - Entendimiento, comprensión
4. **Chesed** - Misericordia, amor
5. **Geburah** - Severidad, justicia
6. **Tiphareth** - Belleza, armonía (centro)
7. **Netzach** - Victoria, eternidad
8. **Hod** - Gloria, esplendor
9. **Yesod** - Fundamento, subconsciente
10. **Malkuth** - Reino, mundo material

## 📊 Formato de Datos

### Entrada de Nombre
- Usar nombre completo
- Solo letras (A-Z, Ñ)
- Mayúsculas o minúsculas
- Ejemplo: "JUAN PEREZ" o "María García"

### Entrada de Fecha
- Formato: DD/MM/AAAA
- Ejemplo: "01/08/1959"
- También acepta: AAAA-MM-DD

## 🎨 Reportes PDF

Los reportes PDF incluyen:

1. **Portada**: Nombre, fecha, símbolo del Árbol de la Vida
2. **Árbol de la Vida**: Visualización con sendero iluminado
3. **Análisis Numerológico**: Cálculos detallados paso a paso
4. **Interpretación**: Significado completo del sendero
5. **Gráficos**: Visualizaciones de vibraciones y alineación
6. **Año Personal**: Predicciones y recomendaciones

## 🔧 Personalización

### Modificar Interpretaciones

Editar `interpretaciones.py` para personalizar:
- Textos de interpretación
- Consejos espirituales
- Recomendaciones profesionales

### Ajustar Visualizaciones

Editar `report_generator.py` para:
- Cambiar colores del Árbol de la Vida
- Modificar diseño de páginas PDF
- Agregar nuevos gráficos

### Extender Cálculos

Editar `cabala_calculator.py` para:
- Agregar nuevos tipos de cálculos
- Modificar algoritmos de reducción
- Implementar nuevas compatibilidades

## 📖 Fundamentos Teóricos

### Numerología Pitagórica
Sistema que asigna valores numéricos a las letras:
- A, J, S = 1
- B, K, T = 2
- C, L, U = 3
- D, M, V = 4
- E, N, W = 5
- F, O, X = 6
- G, P, Y = 7
- H, Q, Z = 8
- I, R = 9

### Números Maestros
- **11**: Iluminación, intuición elevada
- **22**: Constructor maestro, manifestación

### Cábala Hebrea
Sistema místico judío que estudia:
- El Árbol de la Vida (Etz Chaim)
- Las 10 Sephirot (emanaciones divinas)
- Los 22 Senderos (letras hebreas)
- Los 4 Mundos de la creación

## 🤝 Contribuciones

Este es un sistema educativo y espiritual. Las contribuciones son bienvenidas:
- Mejoras en interpretaciones
- Nuevas visualizaciones
- Correcciones de cálculos
- Traducciones

## ⚠️ Disclaimer

Este sistema es para fines educativos y de autoconocimiento. No sustituye:
- Consejo profesional
- Terapia psicológica
- Asesoramiento médico
- Decisiones importantes de vida

Use la información como guía de reflexión personal.

## 📜 Licencia

Sistema de código abierto para uso educativo y personal.

## 📧 Soporte

Para preguntas o problemas:
1. Revisar la sección de Ayuda en el menú
2. Consultar este README
3. Verificar los comentarios en el código

## 🙏 Agradecimientos

Basado en:
- Tradición cabalística hebrea
- Sistema pitagórico de numerología
- Tarot y arquetipos universales
- Sabiduría ancestral de múltiples tradiciones

---

✡️ **Que la luz del Árbol de la Vida ilumine tu camino** ✡️
