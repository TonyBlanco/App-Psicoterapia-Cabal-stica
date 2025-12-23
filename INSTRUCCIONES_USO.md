# 🔮 Sistema de Astrología Cabalística - Instrucciones de Uso

## 📦 Instalación Rápida

```bash
# 1. Instalar dependencias
pip3 install matplotlib

# 2. Verificar instalación
python3 main.py
```

## 🚀 Formas de Uso

### Opción 1: Interfaz CLI Interactiva (Recomendado)

```bash
python3 main.py
```

Esto abrirá un menú interactivo con todas las opciones:
- Análisis individual completo
- Cálculo rápido de vibración
- Análisis de compatibilidad
- Consultar interpretaciones
- Ver Árbol de la Vida
- Calcular año personal
- Generar reportes PDF

### Opción 2: Ejemplos de Código

```bash
python3 ejemplo_uso.py
```

Muestra 10 ejemplos prácticos de cómo usar cada funcionalidad.

### Opción 3: Uso Programático

```python
from cabala_calculator import CabalaCalculator
from report_generator import GeneradorReportePDF

# Análisis básico
calc = CabalaCalculator()
analisis = calc.calcular_sendero_alma("TU NOMBRE", "DD/MM/AAAA")
print(f"Tu Sendero del Alma: {analisis['sendero_alma']}")

# Generar PDF
generador = GeneradorReportePDF()
generador.generar_reporte_completo("TU NOMBRE", "DD/MM/AAAA", "mi_reporte.pdf")
```

## 📋 Ejemplos Rápidos

### Análisis Individual
```bash
python3 -c "
from cabala_calculator import CabalaCalculator
calc = CabalaCalculator()
analisis = calc.calcular_sendero_alma('MARIA GARCIA', '15/03/1985')
print(f'Sendero del Alma: {analisis[\"sendero_alma\"]}')
print(f'Alineación: {analisis[\"alineacion\"][\"porcentaje\"]}%')
"
```

### Compatibilidad
```bash
python3 -c "
from cabala_calculator import CabalaCalculator
calc = CabalaCalculator()
p1 = calc.calcular_sendero_alma('MARIA GARCIA', '15/03/1985')
p2 = calc.calcular_sendero_alma('CARLOS LOPEZ', '22/11/1983')
comp = calc.calcular_compatibilidad(p1, p2)
print(f'Compatibilidad: {comp[\"compatibilidad_total\"]}%')
"
```

### Generar PDF
```bash
python3 -c "
from report_generator import GeneradorReportePDF
gen = GeneradorReportePDF()
gen.generar_reporte_completo('JUAN PEREZ', '01/08/1959', 'reporte.pdf')
print('PDF generado: reporte.pdf')
"
```

## 📖 Formato de Datos

### Nombre
- Usar nombre completo
- Solo letras (A-Z, Ñ)
- Ejemplo: "MARIA GARCIA" o "Juan Pérez"

### Fecha
- Formato: DD/MM/AAAA
- Ejemplo: "15/03/1985"
- También acepta: "1985-03-15"

## 🎯 Casos de Uso Comunes

### 1. Conocer tu Sendero del Alma
```bash
python3 main.py
# Seleccionar opción 1: Análisis Individual Completo
# Ingresar tu nombre y fecha de nacimiento
```

### 2. Análisis de Pareja
```bash
python3 main.py
# Seleccionar opción 3: Análisis de Compatibilidad
# Ingresar datos de ambas personas
```

### 3. Generar Reporte Profesional
```bash
python3 main.py
# Seleccionar opción 1: Análisis Individual
# Al final, elegir generar PDF
```

### 4. Consultar Significado de un Número
```bash
python3 main.py
# Seleccionar opción 4: Consultar Interpretación
# Ingresar número del 1 al 22
```

### 5. Ver tu Año Personal
```bash
python3 main.py
# Seleccionar opción 6: Calcular Año Personal
# Ingresar tu fecha de nacimiento
```

## 📄 Archivos Generados

Los PDFs se generan en el directorio actual:
- `reporte_NOMBRE.pdf` - Análisis individual completo (6 páginas)
- `compatibilidad_NOMBRE1_NOMBRE2.pdf` - Análisis de pareja

Contenido del PDF individual:
1. Portada personalizada
2. Árbol de la Vida con tu sendero iluminado
3. Análisis numerológico detallado
4. Interpretación cabalística completa
5. Gráficos de vibraciones
6. Año personal y predicciones

## 🔍 Interpretación de Resultados

### Vibración del Nombre (1-22)
Representa tu esencia, cómo te expresas en el mundo.

### Vibración de la Fecha (1-22)
Representa tu destino, el camino que viniste a recorrer.

### Sendero del Alma (1-22)
Combinación holística de ambas vibraciones. Tu camino espiritual único.

### Tikun (0-9)
Tu corrección kármica, la lección principal de esta vida.

### Alineación (0-100%)
Qué tan alineado estás entre tu expresión y tu destino.
- 95-100%: Perfectamente alineado
- 85-94%: Altamente armonizado
- 70-84%: Bien alineado
- 50-69%: Requiere trabajo interior

### Compatibilidad (0-100%)
- 90-100%: Excelente - Almas complementarias
- 75-89%: Muy buena - Gran potencial
- 60-74%: Buena - Relación viable
- 45-59%: Regular - Requiere esfuerzo
- 0-44%: Desafiante - Mucho trabajo

## 🎨 Personalización

### Modificar Interpretaciones
Editar `interpretaciones.py` - Línea 15 en adelante

### Cambiar Colores del PDF
Editar `report_generator.py` - Buscar códigos de color (#RRGGBB)

### Agregar Nuevos Cálculos
Editar `cabala_calculator.py` - Agregar métodos a la clase

## ⚠️ Solución de Problemas

### Error: "No module named 'matplotlib'"
```bash
pip3 install matplotlib
```

### Error: "Permission denied"
```bash
chmod +x main.py
python3 main.py
```

### PDF no se genera
Verificar que matplotlib esté instalado y que tengas permisos de escritura.

### Fecha inválida
Usar formato DD/MM/AAAA (ejemplo: 01/08/1959)

## 📚 Más Información

- Ver `README_CABALA.md` para documentación completa
- Ejecutar `python3 ejemplo_uso.py` para ver ejemplos
- En el menú principal, opción 8 para ayuda

## 🙏 Notas Importantes

- Este sistema es para autoconocimiento y reflexión personal
- No sustituye consejo profesional, terapia o asesoramiento médico
- Basado en tradiciones ancestrales de numerología y cábala
- Los resultados son guías para la reflexión, no verdades absolutas

---

✡️ **Que la luz del Árbol de la Vida ilumine tu camino** ✡️
