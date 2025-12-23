#!/usr/bin/env python3
"""
Sistema de Astrología Cabalística Interpretativa
Aplicación CLI para análisis numerológico y cabalístico
"""

import sys
import os
from datetime import datetime

# Importar módulos propios
from cabala_calculator import CabalaCalculator, validar_nombre, validar_fecha
from interpretaciones import InterpretacionesCabalisticas
from sephirot import ArbolDeLaVida, CalculadorAnioPersonal
from report_generator import GeneradorReportePDF


class AstrologiaCabalisticaCLI:
    """Interfaz de línea de comandos para el sistema cabalístico"""
    
    def __init__(self):
        self.calculator = CabalaCalculator()
        self.interpretaciones = InterpretacionesCabalisticas()
        self.arbol = ArbolDeLaVida()
        self.generador_pdf = GeneradorReportePDF()
        self.personas_guardadas = []
    
    def mostrar_banner(self):
        """Muestra el banner de bienvenida"""
        print("\n" + "="*70)
        print("   ✡️  SISTEMA DE ASTROLOGÍA CABALÍSTICA INTERPRETATIVA  ✡️")
        print("="*70)
        print("   Análisis Numerológico basado en el Árbol de la Vida")
        print("="*70 + "\n")
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal"""
        print("\n" + "-"*70)
        print("MENÚ PRINCIPAL")
        print("-"*70)
        print("1. Análisis Individual Completo")
        print("2. Cálculo Rápido de Vibración")
        print("3. Análisis de Compatibilidad (2 personas)")
        print("4. Consultar Interpretación de un Número")
        print("5. Ver Árbol de la Vida (Sephirot)")
        print("6. Calcular Año Personal")
        print("7. Generar Reporte PDF")
        print("8. Ayuda")
        print("0. Salir")
        print("-"*70)
    
    def solicitar_datos_persona(self, numero_persona: int = 0) -> dict:
        """Solicita los datos de una persona"""
        titulo = f"PERSONA {numero_persona}" if numero_persona > 0 else "DATOS PERSONALES"
        print(f"\n{titulo}")
        print("-" * 40)
        
        # Solicitar nombre
        while True:
            nombre = input("Nombre completo: ").strip()
            if validar_nombre(nombre):
                break
            print("❌ Nombre inválido. Debe tener al menos 2 letras.")
        
        # Solicitar fecha
        while True:
            fecha = input("Fecha de nacimiento (DD/MM/AAAA): ").strip()
            if validar_fecha(fecha):
                break
            print("❌ Fecha inválida. Use formato DD/MM/AAAA (ej: 01/08/1959)")
        
        return {'nombre': nombre, 'fecha': fecha}
    
    def analisis_individual_completo(self):
        """Realiza un análisis individual completo"""
        print("\n" + "="*70)
        print("ANÁLISIS INDIVIDUAL COMPLETO")
        print("="*70)
        
        datos = self.solicitar_datos_persona()
        
        print("\n⏳ Calculando análisis cabalístico...")
        
        # Calcular sendero del alma
        analisis = self.calculator.calcular_sendero_alma(datos['nombre'], datos['fecha'])
        
        # Guardar para posible uso posterior
        self.personas_guardadas.append(analisis)
        
        # Mostrar resultados
        self._mostrar_analisis_completo(analisis)
        
        # Preguntar si desea generar PDF
        respuesta = input("\n¿Desea generar un reporte PDF completo? (s/n): ").strip().lower()
        if respuesta == 's':
            self.generar_pdf_individual(analisis)
    
    def _mostrar_analisis_completo(self, analisis: dict):
        """Muestra el análisis completo en consola"""
        print("\n" + "="*70)
        print("RESULTADOS DEL ANÁLISIS")
        print("="*70)
        
        # Datos básicos
        print(f"\n👤 Nombre: {analisis['nombre']}")
        print(f"📅 Fecha: {analisis['fecha']}")
        
        # Vibraciones
        print("\n" + "-"*70)
        print("VIBRACIONES NUMEROLÓGICAS")
        print("-"*70)
        vib_nombre = analisis['vibracion_nombre']
        print(f"Vibración del Nombre: {vib_nombre['vibracion']}")
        print(f"  Proceso: {vib_nombre['proceso'][:60]}...")
        
        vib_fecha = analisis['vibracion_fecha']
        print(f"\nVibración de la Fecha: {vib_fecha['vibracion']}")
        print(f"  Día: {vib_fecha['dia']} → {vib_fecha['vibracion_dia']}")
        print(f"  Mes: {vib_fecha['mes']} → {vib_fecha['vibracion_mes']}")
        print(f"  Año: {vib_fecha['anio']} → {vib_fecha['vibracion_anio']}")
        
        # Sendero del Alma
        print("\n" + "-"*70)
        print("✨ SENDERO DEL ALMA ✨")
        print("-"*70)
        sendero = analisis['sendero_alma']
        print(f"Número del Sendero: {sendero}")
        
        interp = self.interpretaciones.obtener_interpretacion(sendero)
        print(f"Nombre: {interp['nombre']}")
        print(f"Arquetipo: {interp['arquetipo']}")
        print(f"Elemento: {interp['elemento']} | Planeta: {interp['planeta']}")
        
        # Números complementarios
        print(f"\nNúmero de Expresión (Quién Eres): {analisis['numero_expresion']}")
        print(f"Número de Destino (Tu Camino): {analisis['numero_destino']}")
        print(f"Tikun (Corrección Kármica): {analisis['tikun']}")
        
        # Alineación
        alineacion = analisis['alineacion']
        print(f"\n🔮 Alineación Holística: {alineacion['porcentaje']}%")
        print(f"   Estado: {alineacion['estado']}")
        
        # Interpretación
        print("\n" + "-"*70)
        print("INTERPRETACIÓN CABALÍSTICA")
        print("-"*70)
        print(f"\n📖 Significado: {interp['significado']}")
        print(f"\n✨ Luz: {interp['luz']}")
        print(f"\n🌑 Sombra: {interp['sombra']}")
        print(f"\n🎓 Lección: {interp['leccion']}")
        print(f"\n💼 Profesión: {interp['profesion']}")
        print(f"\n💡 Consejo: {interp['consejo']}")
        
        # Sephirot del camino
        print("\n" + "-"*70)
        print("SEPHIROT EN TU CAMINO")
        print("-"*70)
        sephirot_camino = self.arbol.calcular_camino_espiritual(sendero)
        for sephira in sephirot_camino:
            print(f"\n🔯 {sephira['nombre']} - {sephira['significado']}")
            print(f"   {sephira['descripcion']}")
            pilar = self.arbol.obtener_pilar(list(self.arbol.SEPHIROT.keys())[
                list(self.arbol.SEPHIROT.values()).index(sephira)])
            print(f"   Pilar: {pilar}")
    
    def calculo_rapido(self):
        """Cálculo rápido de vibración"""
        print("\n" + "="*70)
        print("CÁLCULO RÁPIDO DE VIBRACIÓN")
        print("="*70)
        
        datos = self.solicitar_datos_persona()
        
        vib_nombre = self.calculator.calcular_vibracion_nombre(datos['nombre'])
        vib_fecha = self.calculator.calcular_vibracion_fecha(datos['fecha'])
        
        sendero = (vib_nombre['vibracion'] + vib_fecha['vibracion'])
        sendero_reducido = self.calculator._reducir_numero_22(sendero)
        
        print("\n" + "-"*70)
        print("RESULTADOS")
        print("-"*70)
        print(f"Vibración del Nombre: {vib_nombre['vibracion']}")
        print(f"Vibración de la Fecha: {vib_fecha['vibracion']}")
        print(f"Sendero del Alma: {sendero_reducido}")
        
        interp = self.interpretaciones.obtener_interpretacion(sendero_reducido)
        print(f"\n{interp['nombre']}")
        print(f"Arquetipo: {interp['arquetipo']}")
    
    def analisis_compatibilidad(self):
        """Análisis de compatibilidad entre dos personas"""
        print("\n" + "="*70)
        print("ANÁLISIS DE COMPATIBILIDAD")
        print("="*70)
        
        # Persona 1
        datos1 = self.solicitar_datos_persona(1)
        analisis1 = self.calculator.calcular_sendero_alma(datos1['nombre'], datos1['fecha'])
        
        # Persona 2
        datos2 = self.solicitar_datos_persona(2)
        analisis2 = self.calculator.calcular_sendero_alma(datos2['nombre'], datos2['fecha'])
        
        print("\n⏳ Calculando compatibilidad...")
        
        # Calcular compatibilidad
        compatibilidad = self.calculator.calcular_compatibilidad(analisis1, analisis2)
        
        # Mostrar resultados
        print("\n" + "="*70)
        print("RESULTADOS DE COMPATIBILIDAD")
        print("="*70)
        print(f"\n{compatibilidad['persona1']} & {compatibilidad['persona2']}")
        print("\n" + "-"*70)
        
        comp_total = compatibilidad['compatibilidad_total']
        print(f"\n💕 COMPATIBILIDAD TOTAL: {comp_total}%")
        print(f"   Nivel: {compatibilidad['nivel']}")
        print(f"   {'✅ Relación Armoniosa' if compatibilidad['armonia'] else '⚠️  Requiere Trabajo'}")
        
        print("\n" + "-"*70)
        print("DETALLES")
        print("-"*70)
        print(f"Sendero del Alma: {compatibilidad['sendero1']} - {compatibilidad['sendero2']}")
        print(f"  Compatibilidad: {compatibilidad['compatibilidad_sendero']}%")
        
        print(f"\nExpresión: {analisis1['numero_expresion']} - {analisis2['numero_expresion']}")
        print(f"  Compatibilidad: {compatibilidad['compatibilidad_expresion']}%")
        
        print(f"\nDestino: {analisis1['numero_destino']} - {analisis2['numero_destino']}")
        print(f"  Compatibilidad: {compatibilidad['compatibilidad_destino']}%")
        
        print("\n" + "-"*70)
        print("INTERPRETACIÓN")
        print("-"*70)
        texto = self.interpretaciones.obtener_compatibilidad_texto(
            compatibilidad['nivel'], comp_total
        )
        print(f"\n{texto}")
        
        # Preguntar si desea generar PDF
        respuesta = input("\n¿Desea generar un reporte PDF de compatibilidad? (s/n): ").strip().lower()
        if respuesta == 's':
            filename = f"compatibilidad_{analisis1['nombre'].replace(' ', '_')}_{analisis2['nombre'].replace(' ', '_')}.pdf"
            print(f"\n⏳ Generando PDF: {filename}")
            self.generador_pdf.generar_reporte_compatibilidad(analisis1, analisis2, filename)
            print(f"✅ PDF generado exitosamente: {filename}")
    
    def consultar_interpretacion(self):
        """Consulta la interpretación de un número específico"""
        print("\n" + "="*70)
        print("CONSULTAR INTERPRETACIÓN DE NÚMERO")
        print("="*70)
        
        while True:
            try:
                numero = int(input("\nIngrese un número (1-22): "))
                if 1 <= numero <= 22:
                    break
                print("❌ Número fuera de rango. Debe ser entre 1 y 22.")
            except ValueError:
                print("❌ Entrada inválida. Ingrese un número.")
        
        interp = self.interpretaciones.obtener_interpretacion(numero)
        
        print("\n" + "="*70)
        print(f"NÚMERO {numero}: {interp['nombre']}")
        print("="*70)
        print(f"\nArquetipo: {interp['arquetipo']}")
        print(f"Sephira: {interp['sephira']}")
        print(f"Elemento: {interp['elemento']}")
        print(f"Planeta: {interp['planeta']}")
        print(f"\n📖 Significado: {interp['significado']}")
        print(f"\n✨ Luz: {interp['luz']}")
        print(f"\n🌑 Sombra: {interp['sombra']}")
        print(f"\n🎓 Lección: {interp['leccion']}")
        print(f"\n💼 Profesión: {interp['profesion']}")
        print(f"\n🏥 Salud: {interp['salud']}")
        print(f"\n🔮 Espiritualidad: {interp['espiritualidad']}")
        print(f"\n💡 Consejo: {interp['consejo']}")
    
    def ver_arbol_vida(self):
        """Muestra información sobre el Árbol de la Vida"""
        print("\n" + "="*70)
        print("ÁRBOL DE LA VIDA - LAS 10 SEPHIROT")
        print("="*70)
        
        for num in range(1, 11):
            sephira = self.arbol.obtener_sephira(num)
            pilar = self.arbol.obtener_pilar(num)
            triada = self.arbol.obtener_triada(num)
            
            print(f"\n{num}. {sephira['nombre']} - {sephira['significado']}")
            print(f"   Atributo: {sephira['atributo']}")
            print(f"   Mundo: {sephira['mundo']}")
            print(f"   Pilar: {pilar}")
            print(f"   Tríada: {triada}")
            print(f"   {sephira['descripcion']}")
    
    def calcular_anio_personal(self):
        """Calcula el año personal"""
        print("\n" + "="*70)
        print("CÁLCULO DE AÑO PERSONAL")
        print("="*70)
        
        datos = self.solicitar_datos_persona()
        
        vib_fecha = self.calculator.calcular_vibracion_fecha(datos['fecha'])
        anio_actual = datetime.now().year
        
        calc_anio = CalculadorAnioPersonal()
        anio_personal = calc_anio.calcular_anio_personal(
            vib_fecha['dia'], vib_fecha['mes'], anio_actual
        )
        
        # Calcular edad y ciclos
        fecha_nac = vib_fecha['fecha_obj']
        edad = anio_actual - fecha_nac.year
        ciclos = calc_anio.obtener_ciclos_vida(edad)
        
        print("\n" + "-"*70)
        print(f"AÑO PERSONAL {anio_actual}")
        print("-"*70)
        print(f"\n📅 Tu Año Personal: {anio_personal}")
        
        consejo = self.interpretaciones.obtener_consejo_anual(anio_personal)
        print(f"\n💡 {consejo}")
        
        print("\n" + "-"*70)
        print("CICLOS DE VIDA")
        print("-"*70)
        print(f"Edad: {edad} años")
        print(f"Ciclo: {ciclos['ciclo']}")
        print(f"Año {ciclos['anio_en_ciclo']} del ciclo de 9 años")
    
    def generar_pdf_individual(self, analisis: dict = None):
        """Genera un reporte PDF individual"""
        if analisis is None:
            if not self.personas_guardadas:
                print("\n❌ No hay análisis previos. Realice un análisis primero.")
                return
            analisis = self.personas_guardadas[-1]
        
        nombre_archivo = f"reporte_{analisis['nombre'].replace(' ', '_')}.pdf"
        
        print(f"\n⏳ Generando reporte PDF: {nombre_archivo}")
        print("   Esto puede tomar unos segundos...")
        
        try:
            self.generador_pdf.generar_reporte_completo(
                analisis['nombre'], 
                analisis['fecha'],
                nombre_archivo
            )
            print(f"\n✅ ¡Reporte PDF generado exitosamente!")
            print(f"   Archivo: {nombre_archivo}")
            print(f"   Ubicación: {os.path.abspath(nombre_archivo)}")
        except Exception as e:
            print(f"\n❌ Error al generar PDF: {str(e)}")
    
    def mostrar_ayuda(self):
        """Muestra información de ayuda"""
        print("\n" + "="*70)
        print("AYUDA - SISTEMA DE ASTROLOGÍA CABALÍSTICA")
        print("="*70)
        print("""
Este sistema calcula y analiza tu sendero espiritual basado en:

1. NUMEROLOGÍA PITAGÓRICA
   - Convierte letras en números (A=1, B=2, etc.)
   - Reduce números a un dígito (1-9) o números maestros (11, 22)

2. CÁBALA HEBREA
   - 22 Senderos del Árbol de la Vida
   - 10 Sephirot (emanaciones divinas)
   - Interpretaciones basadas en tradición cabalística

3. CÁLCULOS PRINCIPALES
   - Vibración del Nombre: Tu esencia y expresión
   - Vibración de la Fecha: Tu destino y propósito
   - Sendero del Alma: Combinación holística de ambas
   - Tikun: Tu corrección kármica

4. REPORTES PDF
   - Análisis completo con visualizaciones
   - Árbol de la Vida personalizado
   - Interpretaciones detalladas
   - Predicciones anuales

5. COMPATIBILIDAD
   - Análisis entre dos personas
   - Porcentajes de armonía
   - Recomendaciones para la relación

Para más información sobre numerología cabalística, consulte textos
tradicionales como el Sefer Yetzirah y el Zohar.
        """)
    
    def ejecutar(self):
        """Ejecuta el programa principal"""
        self.mostrar_banner()
        
        while True:
            self.mostrar_menu_principal()
            
            try:
                opcion = input("\nSeleccione una opción: ").strip()
                
                if opcion == '1':
                    self.analisis_individual_completo()
                elif opcion == '2':
                    self.calculo_rapido()
                elif opcion == '3':
                    self.analisis_compatibilidad()
                elif opcion == '4':
                    self.consultar_interpretacion()
                elif opcion == '5':
                    self.ver_arbol_vida()
                elif opcion == '6':
                    self.calcular_anio_personal()
                elif opcion == '7':
                    self.generar_pdf_individual()
                elif opcion == '8':
                    self.mostrar_ayuda()
                elif opcion == '0':
                    print("\n✨ Gracias por usar el Sistema de Astrología Cabalística")
                    print("   Que la luz del Árbol de la Vida ilumine tu camino ✡️\n")
                    break
                else:
                    print("\n❌ Opción inválida. Intente nuevamente.")
                
                input("\nPresione Enter para continuar...")
                
            except KeyboardInterrupt:
                print("\n\n✨ Programa interrumpido. ¡Hasta pronto! ✡️\n")
                break
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")
                input("\nPresione Enter para continuar...")


def main():
    """Función principal"""
    app = AstrologiaCabalisticaCLI()
    app.ejecutar()


if __name__ == "__main__":
    main()
