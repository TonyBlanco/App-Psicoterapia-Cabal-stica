#!/usr/bin/env python3
"""
Ejemplos de Uso del Sistema de Astrología Cabalística
Demostraciones de las principales funcionalidades
"""

from cabala_calculator import CabalaCalculator
from interpretaciones import InterpretacionesCabalisticas
from sephirot import ArbolDeLaVida, CalculadorAnioPersonal
from report_generator import GeneradorReportePDF
from datetime import datetime


def ejemplo_1_analisis_basico():
    """Ejemplo 1: Análisis básico de una persona"""
    print("\n" + "="*70)
    print("EJEMPLO 1: ANÁLISIS BÁSICO")
    print("="*70)
    
    calc = CabalaCalculator()
    
    # Calcular sendero del alma
    analisis = calc.calcular_sendero_alma("JUAN PEREZ", "01/08/1959")
    
    print(f"\nNombre: {analisis['nombre']}")
    print(f"Fecha: {analisis['fecha']}")
    print(f"\nVibración del Nombre: {analisis['vibracion_nombre']['vibracion']}")
    print(f"Vibración de la Fecha: {analisis['vibracion_fecha']['vibracion']}")
    print(f"Sendero del Alma: {analisis['sendero_alma']}")
    print(f"Número de Expresión: {analisis['numero_expresion']}")
    print(f"Número de Destino: {analisis['numero_destino']}")
    print(f"Tikun (Corrección Kármica): {analisis['tikun']}")
    print(f"Alineación: {analisis['alineacion']['porcentaje']}% - {analisis['alineacion']['estado']}")


def ejemplo_2_interpretacion_detallada():
    """Ejemplo 2: Obtener interpretación detallada de un número"""
    print("\n" + "="*70)
    print("EJEMPLO 2: INTERPRETACIÓN DETALLADA")
    print("="*70)
    
    numero = 8
    interp = InterpretacionesCabalisticas.obtener_interpretacion(numero)
    
    print(f"\nNúmero: {interp['numero']}")
    print(f"Nombre: {interp['nombre']}")
    print(f"Arquetipo: {interp['arquetipo']}")
    print(f"Sephira: {interp['sephira']}")
    print(f"Elemento: {interp['elemento']}")
    print(f"Planeta: {interp['planeta']}")
    print(f"\nSignificado: {interp['significado']}")
    print(f"\nLuz: {interp['luz']}")
    print(f"\nSombra: {interp['sombra']}")
    print(f"\nLección: {interp['leccion']}")
    print(f"\nConsejo: {interp['consejo']}")


def ejemplo_3_compatibilidad():
    """Ejemplo 3: Análisis de compatibilidad entre dos personas"""
    print("\n" + "="*70)
    print("EJEMPLO 3: ANÁLISIS DE COMPATIBILIDAD")
    print("="*70)
    
    calc = CabalaCalculator()
    
    # Calcular senderos de ambas personas
    persona1 = calc.calcular_sendero_alma("MARIA GARCIA", "15/03/1985")
    persona2 = calc.calcular_sendero_alma("CARLOS LOPEZ", "22/11/1983")
    
    # Calcular compatibilidad
    comp = calc.calcular_compatibilidad(persona1, persona2)
    
    print(f"\n{comp['persona1']} & {comp['persona2']}")
    print(f"\nCompatibilidad Total: {comp['compatibilidad_total']}%")
    print(f"Nivel: {comp['nivel']}")
    print(f"Armonía: {'Sí' if comp['armonia'] else 'Requiere trabajo'}")
    
    print(f"\nDetalles:")
    print(f"  Sendero del Alma: {comp['compatibilidad_sendero']}%")
    print(f"  Expresión: {comp['compatibilidad_expresion']}%")
    print(f"  Destino: {comp['compatibilidad_destino']}%")
    
    texto = InterpretacionesCabalisticas.obtener_compatibilidad_texto(
        comp['nivel'], comp['compatibilidad_total']
    )
    print(f"\nInterpretación: {texto}")


def ejemplo_4_arbol_vida():
    """Ejemplo 4: Explorar el Árbol de la Vida"""
    print("\n" + "="*70)
    print("EJEMPLO 4: ÁRBOL DE LA VIDA")
    print("="*70)
    
    arbol = ArbolDeLaVida()
    
    # Obtener información de una Sephira
    sephira = arbol.obtener_sephira(6)  # Tiphareth
    print(f"\nSephira: {sephira['nombre']}")
    print(f"Significado: {sephira['significado']}")
    print(f"Atributo: {sephira['atributo']}")
    print(f"Mundo: {sephira['mundo']}")
    print(f"Descripción: {sephira['descripcion']}")
    
    # Obtener pilar y tríada
    pilar = arbol.obtener_pilar(6)
    triada = arbol.obtener_triada(6)
    print(f"\nPilar: {pilar}")
    print(f"Tríada: {triada}")
    
    # Calcular camino espiritual para una vibración
    print(f"\nCamino espiritual para vibración 14:")
    camino = arbol.calcular_camino_espiritual(14)
    for s in camino:
        print(f"  - {s['nombre']}: {s['descripcion']}")


def ejemplo_5_anio_personal():
    """Ejemplo 5: Calcular año personal"""
    print("\n" + "="*70)
    print("EJEMPLO 5: AÑO PERSONAL")
    print("="*70)
    
    calc = CabalaCalculator()
    calc_anio = CalculadorAnioPersonal()
    
    # Calcular vibración de fecha
    vib_fecha = calc.calcular_vibracion_fecha("01/08/1959")
    
    # Año actual
    anio_actual = datetime.now().year
    
    # Calcular año personal
    anio_personal = calc_anio.calcular_anio_personal(
        vib_fecha['dia'], 
        vib_fecha['mes'], 
        anio_actual
    )
    
    print(f"\nFecha de nacimiento: {vib_fecha['fecha']}")
    print(f"Año actual: {anio_actual}")
    print(f"Año Personal: {anio_personal}")
    
    # Obtener consejo
    consejo = InterpretacionesCabalisticas.obtener_consejo_anual(anio_personal)
    print(f"\nConsejo para este año: {consejo}")
    
    # Calcular ciclos de vida
    edad = anio_actual - vib_fecha['anio']
    ciclos = calc_anio.obtener_ciclos_vida(edad)
    
    print(f"\nEdad: {edad} años")
    print(f"Ciclo de vida: {ciclos['ciclo']}")
    print(f"Año {ciclos['anio_en_ciclo']} del ciclo de 9 años")


def ejemplo_6_generar_pdf():
    """Ejemplo 6: Generar reporte PDF completo"""
    print("\n" + "="*70)
    print("EJEMPLO 6: GENERAR REPORTE PDF")
    print("="*70)
    
    generador = GeneradorReportePDF()
    
    print("\nGenerando reporte PDF completo...")
    archivo = generador.generar_reporte_completo(
        nombre="JUAN PEREZ",
        fecha="01/08/1959",
        output_file="ejemplo_reporte.pdf"
    )
    
    import os
    if os.path.exists(archivo):
        size = os.path.getsize(archivo)
        print(f"✅ Reporte generado exitosamente!")
        print(f"   Archivo: {archivo}")
        print(f"   Tamaño: {size:,} bytes")
        print(f"   Ubicación: {os.path.abspath(archivo)}")
    else:
        print("❌ Error al generar el reporte")


def ejemplo_7_pdf_compatibilidad():
    """Ejemplo 7: Generar PDF de compatibilidad"""
    print("\n" + "="*70)
    print("EJEMPLO 7: PDF DE COMPATIBILIDAD")
    print("="*70)
    
    calc = CabalaCalculator()
    generador = GeneradorReportePDF()
    
    # Calcular análisis de ambas personas
    persona1 = calc.calcular_sendero_alma("MARIA GARCIA", "15/03/1985")
    persona2 = calc.calcular_sendero_alma("CARLOS LOPEZ", "22/11/1983")
    
    print("\nGenerando PDF de compatibilidad...")
    archivo = generador.generar_reporte_compatibilidad(
        persona1,
        persona2,
        "ejemplo_compatibilidad.pdf"
    )
    
    import os
    if os.path.exists(archivo):
        size = os.path.getsize(archivo)
        print(f"✅ PDF de compatibilidad generado!")
        print(f"   Archivo: {archivo}")
        print(f"   Tamaño: {size:,} bytes")
    else:
        print("❌ Error al generar el PDF")


def ejemplo_8_numeros_maestros():
    """Ejemplo 8: Trabajar con números maestros (11, 22)"""
    print("\n" + "="*70)
    print("EJEMPLO 8: NÚMEROS MAESTROS")
    print("="*70)
    
    calc = CabalaCalculator()
    
    # Ejemplo con número maestro 11
    print("\nNúmero Maestro 11:")
    interp11 = InterpretacionesCabalisticas.obtener_interpretacion(11)
    print(f"Nombre: {interp11['nombre']}")
    print(f"Arquetipo: {interp11['arquetipo']}")
    print(f"Significado: {interp11['significado']}")
    
    # Ejemplo con número maestro 22
    print("\nNúmero Maestro 22:")
    interp22 = InterpretacionesCabalisticas.obtener_interpretacion(22)
    print(f"Nombre: {interp22['nombre']}")
    print(f"Arquetipo: {interp22['arquetipo']}")
    print(f"Significado: {interp22['significado']}")


def ejemplo_9_validaciones():
    """Ejemplo 9: Validaciones de entrada"""
    print("\n" + "="*70)
    print("EJEMPLO 9: VALIDACIONES")
    print("="*70)
    
    from cabala_calculator import validar_nombre, validar_fecha
    
    # Validar nombres
    nombres_prueba = ["JUAN", "A", "MARIA GARCIA", "123", ""]
    print("\nValidación de nombres:")
    for nombre in nombres_prueba:
        valido = validar_nombre(nombre)
        print(f"  '{nombre}': {'✅ Válido' if valido else '❌ Inválido'}")
    
    # Validar fechas
    fechas_prueba = ["01/08/1959", "15-03-1985", "2000-12-31", "32/13/2000", "abc"]
    print("\nValidación de fechas:")
    for fecha in fechas_prueba:
        valido = validar_fecha(fecha)
        print(f"  '{fecha}': {'✅ Válido' if valido else '❌ Inválido'}")


def ejemplo_10_todos_los_senderos():
    """Ejemplo 10: Mostrar todos los 22 senderos"""
    print("\n" + "="*70)
    print("EJEMPLO 10: LOS 22 SENDEROS")
    print("="*70)
    
    print("\nLos 22 Senderos del Árbol de la Vida:\n")
    for i in range(1, 23):
        interp = InterpretacionesCabalisticas.obtener_interpretacion(i)
        print(f"{i:2d}. {interp['nombre']:30s} - {interp['arquetipo']}")


def main():
    """Ejecuta todos los ejemplos"""
    print("\n" + "="*70)
    print("EJEMPLOS DE USO - SISTEMA DE ASTROLOGÍA CABALÍSTICA")
    print("="*70)
    
    ejemplos = [
        ("Análisis Básico", ejemplo_1_analisis_basico),
        ("Interpretación Detallada", ejemplo_2_interpretacion_detallada),
        ("Compatibilidad", ejemplo_3_compatibilidad),
        ("Árbol de la Vida", ejemplo_4_arbol_vida),
        ("Año Personal", ejemplo_5_anio_personal),
        ("Generar PDF", ejemplo_6_generar_pdf),
        ("PDF Compatibilidad", ejemplo_7_pdf_compatibilidad),
        ("Números Maestros", ejemplo_8_numeros_maestros),
        ("Validaciones", ejemplo_9_validaciones),
        ("Todos los Senderos", ejemplo_10_todos_los_senderos),
    ]
    
    print("\nEjemplos disponibles:")
    for i, (nombre, _) in enumerate(ejemplos, 1):
        print(f"{i:2d}. {nombre}")
    print(" 0. Ejecutar todos")
    
    try:
        opcion = input("\nSeleccione un ejemplo (0-10): ").strip()
        
        if opcion == '0':
            for nombre, func in ejemplos:
                func()
                input("\nPresione Enter para continuar...")
        elif opcion.isdigit() and 1 <= int(opcion) <= len(ejemplos):
            ejemplos[int(opcion) - 1][1]()
        else:
            print("Opción inválida")
    
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido")
    except Exception as e:
        print(f"\nError: {str(e)}")
    
    print("\n" + "="*70)
    print("FIN DE LOS EJEMPLOS")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
