"""
Base de Datos de Interpretaciones Cabalísticas
22 Vibraciones/Senderos del Árbol de la Vida
"""

class InterpretacionesCabalisticas:
    """Interpretaciones detalladas de las 22 vibraciones cabalísticas"""
    
    VIBRACIONES = {
        1: {
            'numero': 1,
            'nombre': 'El Mago - Aleph (א)',
            'sephira': 'Kether',
            'arquetipo': 'El Iniciador',
            'elemento': 'Aire',
            'planeta': 'Mercurio',
            'significado': 'Inicio, liderazgo, independencia, creatividad original',
            'luz': 'Pionero natural, líder innato, capacidad de manifestación, voluntad fuerte, originalidad',
            'sombra': 'Egoísmo, arrogancia, impaciencia, autoritarismo, aislamiento',
            'leccion': 'Aprender a liderar sin dominar, usar el poder personal para el bien común',
            'profesion': 'Emprendedor, líder, inventor, director, pionero en cualquier campo',
            'salud': 'Cabeza, cerebro, sistema nervioso. Tendencia a estrés por exceso de actividad mental',
            'espiritualidad': 'Conexión directa con la Fuente Divina, capacidad de canalizar energía creadora',
            'consejo': 'Cultiva la humildad y aprende a trabajar en equipo sin perder tu individualidad'
        },
        2: {
            'numero': 2,
            'nombre': 'La Sacerdotisa - Beth (ב)',
            'sephira': 'Chokmah',
            'arquetipo': 'La Intuitiva',
            'elemento': 'Agua',
            'planeta': 'Luna',
            'significado': 'Intuición, receptividad, dualidad, misterio, sabiduría oculta',
            'luz': 'Intuición profunda, sensibilidad psíquica, diplomacia, cooperación, paciencia',
            'sombra': 'Indecisión, dependencia emocional, pasividad, manipulación sutil',
            'leccion': 'Equilibrar la receptividad con la acción, confiar en la intuición sin perderse en ella',
            'profesion': 'Consejero, terapeuta, mediador, investigador, trabajador social',
            'salud': 'Sistema reproductivo, estómago, emociones. Sensibilidad a ambientes energéticos',
            'espiritualidad': 'Acceso a los misterios ocultos, capacidad de percibir más allá del velo',
            'consejo': 'Confía en tu intuición pero verifica con la razón. Establece límites emocionales claros'
        },
        3: {
            'numero': 3,
            'nombre': 'La Emperatriz - Gimel (ג)',
            'sephira': 'Binah',
            'arquetipo': 'La Creadora',
            'elemento': 'Tierra',
            'planeta': 'Venus',
            'significado': 'Creatividad, abundancia, fertilidad, expresión, belleza',
            'luz': 'Creatividad desbordante, expresión artística, alegría, sociabilidad, optimismo',
            'sombra': 'Dispersión, superficialidad, vanidad, exceso de indulgencia',
            'leccion': 'Enfocar la energía creativa, dar forma concreta a las ideas',
            'profesion': 'Artista, comunicador, diseñador, escritor, entertainer',
            'salud': 'Garganta, tiroides, sistema reproductivo. Necesidad de expresión creativa',
            'espiritualidad': 'Manifestación de la belleza divina, creatividad como acto sagrado',
            'consejo': 'Canaliza tu creatividad en proyectos concretos. No disperses tu energía'
        },
        4: {
            'numero': 4,
            'nombre': 'El Emperador - Daleth (ד)',
            'sephira': 'Chesed',
            'arquetipo': 'El Constructor',
            'elemento': 'Fuego',
            'planeta': 'Aries',
            'significado': 'Estructura, orden, estabilidad, disciplina, fundamentos sólidos',
            'luz': 'Organización, disciplina, confiabilidad, construcción de bases sólidas, practicidad',
            'sombra': 'Rigidez, terquedad, resistencia al cambio, exceso de control',
            'leccion': 'Equilibrar estructura con flexibilidad, construir sin limitar',
            'profesion': 'Arquitecto, ingeniero, administrador, constructor, planificador',
            'salud': 'Huesos, estructura corporal, rodillas. Necesidad de ejercicio regular',
            'espiritualidad': 'Manifestación de lo divino en lo material, sacralidad de la forma',
            'consejo': 'Mantén la estructura pero permite la flexibilidad. El cambio es parte de la vida'
        },
        5: {
            'numero': 5,
            'nombre': 'El Hierofante - Heh (ה)',
            'sephira': 'Geburah',
            'arquetipo': 'El Maestro',
            'elemento': 'Tierra',
            'planeta': 'Tauro',
            'significado': 'Libertad, cambio, aventura, experiencia, versatilidad',
            'luz': 'Adaptabilidad, curiosidad, libertad, experiencias variadas, comunicación',
            'sombra': 'Inquietud, irresponsabilidad, dispersión, adicciones, impulsividad',
            'leccion': 'Usar la libertad con responsabilidad, aprender de las experiencias',
            'profesion': 'Viajero, vendedor, comunicador, promotor, agente de cambio',
            'salud': 'Sistema nervioso, manos, pulmones. Necesidad de variedad y movimiento',
            'espiritualidad': 'Libertad espiritual, exploración de diferentes caminos',
            'consejo': 'Disfruta la libertad pero mantén compromisos importantes. Aprende de cada experiencia'
        },
        6: {
            'numero': 6,
            'nombre': 'Los Enamorados - Vav (ו)',
            'sephira': 'Tiphareth',
            'arquetipo': 'El Armonizador',
            'elemento': 'Aire',
            'planeta': 'Géminis',
            'significado': 'Amor, armonía, responsabilidad, elección, equilibrio',
            'luz': 'Amor incondicional, servicio, armonía, responsabilidad, sanación',
            'sombra': 'Codependencia, sacrificio excesivo, perfeccionismo, crítica',
            'leccion': 'Amar sin perder la identidad, servir sin sacrificarse',
            'profesion': 'Sanador, consejero, maestro, cuidador, trabajador comunitario',
            'salud': 'Corazón, pecho, sistema circulatorio. Necesidad de equilibrio emocional',
            'espiritualidad': 'Amor como camino espiritual, servicio desinteresado',
            'consejo': 'Cuida de otros pero no olvides cuidarte a ti mismo. El amor empieza por dentro'
        },
        7: {
            'numero': 7,
            'nombre': 'El Carro - Zayin (ז)',
            'sephira': 'Netzach',
            'arquetipo': 'El Buscador',
            'elemento': 'Agua',
            'planeta': 'Cáncer',
            'significado': 'Búsqueda interior, análisis, espiritualidad, perfección',
            'luz': 'Sabiduría profunda, análisis, intuición, conexión espiritual, perfeccionamiento',
            'sombra': 'Aislamiento, escepticismo, frialdad, perfeccionismo paralizante',
            'leccion': 'Equilibrar mente y corazón, compartir la sabiduría adquirida',
            'profesion': 'Investigador, científico, filósofo, místico, analista',
            'salud': 'Sistema digestivo, nervios. Necesidad de tiempo a solas para recargar',
            'espiritualidad': 'Búsqueda de la verdad última, conexión con lo trascendente',
            'consejo': 'No te aísles en tu búsqueda. La sabiduría se completa al compartirla'
        },
        8: {
            'numero': 8,
            'nombre': 'La Justicia - Chet (ח)',
            'sephira': 'Hod',
            'arquetipo': 'El Manifestador',
            'elemento': 'Fuego',
            'planeta': 'Leo',
            'significado': 'Poder, abundancia material, logro, autoridad, karma',
            'luz': 'Poder de manifestación, éxito material, liderazgo, justicia, equilibrio',
            'sombra': 'Materialismo, abuso de poder, obsesión por el éxito, dureza',
            'leccion': 'Usar el poder con sabiduría, equilibrar lo material con lo espiritual',
            'profesion': 'Ejecutivo, empresario, banquero, juez, administrador de alto nivel',
            'salud': 'Hígado, vesícula, sistema muscular. Necesidad de equilibrio trabajo-descanso',
            'espiritualidad': 'Ley del karma, manifestación consciente, poder espiritual',
            'consejo': 'El verdadero poder viene del servicio. Usa tu influencia para el bien común'
        },
        9: {
            'numero': 9,
            'nombre': 'El Ermitaño - Teth (ט)',
            'sephira': 'Yesod',
            'arquetipo': 'El Humanitario',
            'elemento': 'Tierra',
            'planeta': 'Virgo',
            'significado': 'Culminación, compasión universal, sabiduría, finalización',
            'luz': 'Compasión universal, sabiduría, generosidad, visión amplia, sanación colectiva',
            'sombra': 'Mártir, dispersión emocional, dificultad para cerrar ciclos',
            'leccion': 'Soltar el pasado, servir sin apego, completar ciclos',
            'profesion': 'Humanitario, sanador global, artista universal, filántropo',
            'salud': 'Pies, sistema linfático. Necesidad de conexión con la tierra',
            'espiritualidad': 'Conciencia universal, compasión ilimitada, servicio a la humanidad',
            'consejo': 'Suelta lo que ya cumplió su ciclo. Tu misión es más grande que tus apegos'
        },
        10: {
            'numero': 10,
            'nombre': 'La Rueda de la Fortuna - Yod (י)',
            'sephira': 'Malkuth',
            'arquetipo': 'El Transformador',
            'elemento': 'Fuego',
            'planeta': 'Júpiter',
            'significado': 'Ciclos, cambio, destino, oportunidad, renovación',
            'luz': 'Adaptabilidad a ciclos, optimismo, fe en el proceso, renovación constante',
            'sombra': 'Resistencia al cambio, victimización, falta de responsabilidad',
            'leccion': 'Fluir con los ciclos de la vida, tomar responsabilidad del destino',
            'profesion': 'Agente de cambio, consultor, coach de transformación',
            'salud': 'Todo el cuerpo. Necesidad de adaptarse a cambios constantes',
            'espiritualidad': 'Comprensión de los ciclos cósmicos, fe en el plan divino',
            'consejo': 'Acepta los ciclos naturales. Cada final es un nuevo comienzo'
        },
        11: {
            'numero': 11,
            'nombre': 'La Fuerza - Kaph (כ)',
            'sephira': 'Kether-Chokmah',
            'arquetipo': 'El Iluminador (Número Maestro)',
            'elemento': 'Aire',
            'planeta': 'Urano',
            'significado': 'Iluminación, inspiración, intuición elevada, maestría espiritual',
            'luz': 'Inspiración divina, intuición elevada, capacidad de iluminar a otros, visión espiritual',
            'sombra': 'Nerviosismo extremo, idealismo poco práctico, fanatismo',
            'leccion': 'Anclar la inspiración en lo práctico, ser canal sin ego',
            'profesion': 'Maestro espiritual, visionario, inventor, líder inspirador',
            'salud': 'Sistema nervioso muy sensible. Necesidad de prácticas de anclaje',
            'espiritualidad': 'Conexión directa con planos superiores, canal de luz',
            'consejo': 'Ancla tu visión en la realidad. Eres un puente entre cielo y tierra'
        },
        12: {
            'numero': 12,
            'nombre': 'El Colgado - Lamed (ל)',
            'sephira': 'Binah-Chesed',
            'arquetipo': 'El Sacrificado',
            'elemento': 'Agua',
            'planeta': 'Neptuno',
            'significado': 'Sacrificio, rendición, nueva perspectiva, suspensión',
            'luz': 'Capacidad de ver desde otra perspectiva, sacrificio consciente, rendición al flujo',
            'sombra': 'Victimización, parálisis, escapismo, martirio',
            'leccion': 'Soltar el control, confiar en el proceso, ver con nuevos ojos',
            'profesion': 'Sanador, místico, artista contemplativo, trabajador social',
            'salud': 'Pies, sistema linfático, adicciones. Necesidad de límites claros',
            'espiritualidad': 'Rendición al plan divino, muerte del ego',
            'consejo': 'A veces soltar es la mayor fortaleza. Cambia tu perspectiva'
        },
        13: {
            'numero': 13,
            'nombre': 'La Muerte - Mem (מ)',
            'sephira': 'Geburah-Tiphareth',
            'arquetipo': 'El Transformador',
            'elemento': 'Agua',
            'planeta': 'Escorpio',
            'significado': 'Transformación profunda, muerte y renacimiento, regeneración',
            'luz': 'Capacidad de transformación, renacimiento, profundidad emocional, regeneración',
            'sombra': 'Miedo al cambio, apego destructivo, crisis constantes',
            'leccion': 'Abrazar la transformación, soltar lo que ya no sirve',
            'profesion': 'Terapeuta profundo, investigador de lo oculto, transformador social',
            'salud': 'Órganos reproductivos, sistema de eliminación. Necesidad de purificación',
            'espiritualidad': 'Muerte mística, renacimiento espiritual, alquimia interior',
            'consejo': 'No temas a los finales. Son puertas hacia nuevos comienzos'
        },
        14: {
            'numero': 14,
            'nombre': 'La Templanza - Nun (נ)',
            'sephira': 'Tiphareth-Netzach',
            'arquetipo': 'El Alquimista',
            'elemento': 'Fuego',
            'planeta': 'Sagitario',
            'significado': 'Equilibrio, moderación, alquimia, integración',
            'luz': 'Equilibrio perfecto, moderación, capacidad de integrar opuestos, sanación',
            'sombra': 'Excesos, falta de límites, dispersión',
            'leccion': 'Encontrar el punto medio, integrar polaridades',
            'profesion': 'Sanador holístico, mediador, diplomático, alquimista moderno',
            'salud': 'Hígado, caderas, sistema nervioso. Necesidad de equilibrio en todo',
            'espiritualidad': 'Alquimia espiritual, integración de opuestos, el camino del medio',
            'consejo': 'Busca el equilibrio en todo. La virtud está en el punto medio'
        },
        15: {
            'numero': 15,
            'nombre': 'El Diablo - Samekh (ס)',
            'sephira': 'Hod-Yesod',
            'arquetipo': 'El Tentado',
            'elemento': 'Tierra',
            'planeta': 'Capricornio',
            'significado': 'Apego material, sombra, tentación, poder instintivo',
            'luz': 'Comprensión de la sombra, poder instintivo integrado, maestría material',
            'sombra': 'Adicciones, materialismo, manipulación, esclavitud a deseos',
            'leccion': 'Integrar la sombra, liberarse de ataduras, usar el poder instintivo sabiamente',
            'profesion': 'Psicólogo profundo, trabajador con adicciones, terapeuta de sombra',
            'salud': 'Adicciones, sistema reproductivo. Necesidad de trabajo con la sombra',
            'espiritualidad': 'Integración de la sombra, liberación de ataduras kármicas',
            'consejo': 'Reconoce tus cadenas para poder liberarte. La sombra integrada es poder'
        },
        16: {
            'numero': 16,
            'nombre': 'La Torre - Ayin (ע)',
            'sephira': 'Hod-Netzach',
            'arquetipo': 'El Destructor',
            'elemento': 'Fuego',
            'planeta': 'Marte',
            'significado': 'Destrucción necesaria, revelación súbita, liberación',
            'luz': 'Liberación de estructuras obsoletas, revelación, renovación radical',
            'sombra': 'Caos, destrucción sin propósito, resistencia al cambio necesario',
            'leccion': 'Permitir que lo viejo se derrumbe para dar paso a lo nuevo',
            'profesion': 'Agente de cambio radical, revolucionario, demoledor de paradigmas',
            'salud': 'Sistema nervioso, accidentes. Necesidad de canalizar energía constructivamente',
            'espiritualidad': 'Destrucción del ego, iluminación súbita, despertar forzado',
            'consejo': 'Las crisis son oportunidades. Deja que se derrumbe lo que debe caer'
        },
        17: {
            'numero': 17,
            'nombre': 'La Estrella - Peh (פ)',
            'sephira': 'Netzach-Yesod',
            'arquetipo': 'La Esperanza',
            'elemento': 'Aire',
            'planeta': 'Acuario',
            'significado': 'Esperanza, inspiración, guía divina, renovación',
            'luz': 'Esperanza renovada, inspiración celestial, guía clara, sanación',
            'sombra': 'Idealismo desconectado, desilusión, falta de fe',
            'leccion': 'Mantener la fe, ser guía para otros, conectar con la inspiración divina',
            'profesion': 'Guía espiritual, sanador, inspirador, visionario',
            'salud': 'Sistema circulatorio, tobillos. Necesidad de mantener la esperanza',
            'espiritualidad': 'Conexión con la guía divina, fe renovada, estrella guía',
            'consejo': 'Mantén la fe incluso en la oscuridad. Eres una luz para otros'
        },
        18: {
            'numero': 18,
            'nombre': 'La Luna - Tzaddi (צ)',
            'sephira': 'Netzach-Malkuth',
            'arquetipo': 'El Soñador',
            'elemento': 'Agua',
            'planeta': 'Piscis',
            'significado': 'Ilusión, intuición profunda, subconsciente, misterio',
            'luz': 'Intuición profunda, conexión con el subconsciente, capacidad psíquica',
            'sombra': 'Ilusión, confusión, miedo, engaño, paranoia',
            'leccion': 'Discernir entre intuición e ilusión, navegar el mundo emocional',
            'profesion': 'Psíquico, artista, soñador, trabajador con el subconsciente',
            'salud': 'Sistema linfático, pies, emociones. Necesidad de claridad mental',
            'espiritualidad': 'Navegación del subconsciente, trabajo con sueños, misterios lunares',
            'consejo': 'No todo lo que brilla es oro. Desarrolla discernimiento en lo sutil'
        },
        19: {
            'numero': 19,
            'nombre': 'El Sol - Qoph (ק)',
            'sephira': 'Hod-Yesod',
            'arquetipo': 'El Radiante',
            'elemento': 'Fuego',
            'planeta': 'Sol',
            'significado': 'Claridad, éxito, vitalidad, iluminación, alegría',
            'luz': 'Claridad mental, éxito, vitalidad, alegría, iluminación consciente',
            'sombra': 'Arrogancia, exceso de ego, ceguera por el éxito',
            'leccion': 'Brillar sin opacar a otros, compartir la luz',
            'profesion': 'Líder inspirador, sanador solar, maestro, figura pública',
            'salud': 'Corazón, columna vertebral, vitalidad general. Necesidad de expresión',
            'espiritualidad': 'Iluminación consciente, conexión con el Yo Superior',
            'consejo': 'Brilla con tu luz propia pero no ciegues a otros. Comparte tu calidez'
        },
        20: {
            'numero': 20,
            'nombre': 'El Juicio - Resh (ר)',
            'sephira': 'Hod-Malkuth',
            'arquetipo': 'El Renacido',
            'elemento': 'Fuego',
            'planeta': 'Plutón',
            'significado': 'Renacimiento, juicio final, llamado superior, despertar',
            'luz': 'Renacimiento espiritual, respuesta al llamado, juicio justo, despertar',
            'sombra': 'Juicio severo, culpa, resistencia al llamado',
            'leccion': 'Responder al llamado del alma, renacer en consciencia superior',
            'profesion': 'Transformador social, juez, líder de renacimiento colectivo',
            'salud': 'Todo el ser. Necesidad de renovación completa',
            'espiritualidad': 'Renacimiento espiritual, respuesta al llamado divino',
            'consejo': 'Escucha el llamado de tu alma. Es tiempo de renacer'
        },
        21: {
            'numero': 21,
            'nombre': 'El Mundo - Shin (ש)',
            'sephira': 'Yesod-Malkuth',
            'arquetipo': 'El Completo',
            'elemento': 'Tierra',
            'planeta': 'Saturno',
            'significado': 'Culminación, totalidad, logro completo, integración',
            'luz': 'Logro total, integración completa, maestría, realización',
            'sombra': 'Estancamiento en el logro, resistencia a nuevos ciclos',
            'leccion': 'Celebrar los logros y prepararse para nuevos ciclos',
            'profesion': 'Maestro consumado, líder mundial, integrador de sistemas',
            'salud': 'Estructura completa. Necesidad de mantener la totalidad',
            'espiritualidad': 'Integración total, maestría completa, unidad con el Todo',
            'consejo': 'Celebra tus logros pero no te estanques. Siempre hay un nuevo nivel'
        },
        22: {
            'numero': 22,
            'nombre': 'El Loco - Tav (ת)',
            'sephira': 'Kether-Malkuth (Número Maestro)',
            'arquetipo': 'El Constructor Maestro',
            'elemento': 'Éter',
            'planeta': 'Tierra',
            'significado': 'Maestría material, construcción a gran escala, visión práctica',
            'luz': 'Capacidad de manifestar grandes visiones, maestro constructor, poder de materialización',
            'sombra': 'Obsesión con el control, megalomanía, colapso por exceso',
            'leccion': 'Construir con visión espiritual, manifestar lo divino en lo material',
            'profesion': 'Constructor de imperios, arquitecto de sistemas, líder visionario práctico',
            'salud': 'Todo el sistema. Necesidad de equilibrio entre visión y práctica',
            'espiritualidad': 'Manifestación del plan divino en la Tierra, puente entre mundos',
            'consejo': 'Tu visión puede cambiar el mundo. Construye con sabiduría y amor'
        }
    }
    
    @classmethod
    def obtener_interpretacion(cls, numero: int) -> dict:
        """Obtiene la interpretación completa de un número"""
        return cls.VIBRACIONES.get(numero, cls.VIBRACIONES[1])
    
    @classmethod
    def obtener_tikun(cls, numero: int) -> str:
        """Obtiene la lección kármica (Tikun) específica"""
        tikun_especificos = {
            0: "Integración total de todas las lecciones",
            1: "Aprender humildad y trabajo en equipo",
            2: "Desarrollar confianza en sí mismo y tomar decisiones",
            3: "Enfocar la energía creativa y evitar dispersión",
            4: "Desarrollar flexibilidad y apertura al cambio",
            5: "Cultivar compromiso y responsabilidad",
            6: "Establecer límites saludables y evitar codependencia",
            7: "Abrirse emocionalmente y conectar con otros",
            8: "Equilibrar poder material con valores espirituales",
            9: "Soltar el pasado y completar ciclos pendientes"
        }
        return tikun_especificos.get(numero, "Integración y equilibrio de energías")
    
    @classmethod
    def obtener_compatibilidad_texto(cls, nivel: str, porcentaje: float) -> str:
        """Genera texto de compatibilidad detallado"""
        textos = {
            "Perfecta": f"Compatibilidad excepcional ({porcentaje}%). Almas gemelas con senderos alineados. Conexión profunda y natural.",
            "Excelente": f"Muy alta compatibilidad ({porcentaje}%). Senderos complementarios que se potencian mutuamente.",
            "Muy Buena": f"Alta compatibilidad ({porcentaje}%). Buena armonía con oportunidades de crecimiento mutuo.",
            "Buena": f"Compatibilidad positiva ({porcentaje}%). Relación viable con trabajo consciente.",
            "Regular": f"Compatibilidad moderada ({porcentaje}%). Requiere esfuerzo y comprensión mutua.",
            "Desafiante": f"Compatibilidad baja ({porcentaje}%). Relación que demanda mucho trabajo interior."
        }
        return textos.get(nivel, f"Compatibilidad: {porcentaje}%")
    
    @classmethod
    def obtener_consejo_anual(cls, anio_personal: int) -> str:
        """Obtiene el consejo para un año personal específico"""
        consejos = {
            1: "Año de nuevos comienzos. Inicia proyectos, toma la iniciativa, planta semillas.",
            2: "Año de paciencia y cooperación. Cultiva relaciones, desarrolla proyectos iniciados.",
            3: "Año de creatividad y expresión. Comunica, crea, socializa, disfruta.",
            4: "Año de trabajo y construcción. Establece bases sólidas, organiza, disciplina.",
            5: "Año de cambio y libertad. Viaja, experimenta, adapta, libera lo viejo.",
            6: "Año de responsabilidad y amor. Cuida relaciones, hogar, familia, armoniza.",
            7: "Año de introspección y espiritualidad. Estudia, medita, busca sabiduría interior.",
            8: "Año de logros materiales. Cosecha, expande, lidera, materializa.",
            9: "Año de culminación y cierre. Completa ciclos, suelta, prepara lo nuevo."
        }
        return consejos.get(anio_personal, "Año de integración y equilibrio.")
