import psycopg2
import json
from config import DATABASE_URL

# Conexión a la base de datos
try:
    conn = psycopg2.connect(DATABASE_URL)
    print("✅ Conectado a la base de datos.")
except Exception as e:
    print("❌ ERROR conectando a la base de datos:", e)
    exit()

def modulo_existe(titulo):
    """Verifica si un módulo ya existe en la base de datos."""
    query = "SELECT id_modulo FROM Modulos WHERE titulo = %s"
    with conn.cursor() as cur:
        cur.execute(query, (titulo,))
        return cur.fetchone() is not None

def insertar_modulo(titulo, descripcion, descripcion_detallada, orden):
    """Inserta un módulo en la base de datos si no existe."""
    if modulo_existe(titulo):
        print(f"⚠️ Módulo '{titulo}' ya existe. No se inserta.")
        return

    query = """INSERT INTO Modulos (titulo, descripcion, descripcion_detallada, orden)
               VALUES (%s, %s, %s, %s)"""
    with conn.cursor() as cur:
        cur.execute(query, (titulo, descripcion, descripcion_detallada, orden))
    conn.commit()
    print(f"✅ Módulo '{titulo}' insertado correctamente.")

# Módulos estáticos
modulos_estaticos = [
    {
        'titulo': 'Grooming: Conceptos Fundamentales',
        'descripcion': 'Comprender el acoso sexual online en profundidad',
        'descripcion_detallada': (
            'El grooming es un tipo de acoso sexual en línea en el que un adulto (o en ocasiones, un joven mayor) '
            'busca ganarse la confianza de un menor con fines de explotación y abuso. A menudo, el agresor adopta '
            'una identidad falsa o se hace pasar por alguien de la misma edad para acercarse a la víctima. \n\n'
            '**Características principales del grooming:**\n'
            '- Está dirigido a niños, niñas y adolescentes, aunque también puede ocurrir contra adultos vulnerables.\n'
            '- Se basa en la manipulación emocional y la construcción de una relación de confianza.\n'
            '- Puede ocurrir en cualquier plataforma digital: redes sociales (Instagram, TikTok, Facebook), videojuegos '
            'en línea (Roblox, Fortnite), foros, chats o aplicaciones de mensajería.\n\n'
            '**Etapas comunes en el proceso de grooming:**\n'
            '1. **Contacto inicial**: El agresor localiza a la posible víctima y envía solicitudes de amistad o inicia '
            'conversaciones casuales.\n'
            '2. **Construcción de confianza**: Mediante halagos, escucha activa y muestras de interés en hobbies o problemas '
            'personales, el agresor establece un vínculo.\n'
            '3. **Aislamiento**: El groomer anima a la víctima a mantener la relación en secreto, alegando que “nadie '
            'entendería” o que “les van a separar”.\n'
            '4. **Incremento de la intimidad**: Empieza a hablar de temas sexuales, solicita fotos o videos personales, '
            'y hace ver que todo es un “juego” o “prueba de confianza”.\n'
            '5. **Explotación**: Con material íntimo ya obtenido, el agresor chantajea o amenaza con difundirlo. Puede '
            'exigir más contenido o incluso un encuentro físico.\n\n'
            '**Importancia de la prevención:**\n'
            'Según diversas organizaciones de protección infantil, una parte significativa de menores que interactúan en '
            'internet ha sido contactada al menos una vez por un desconocido. El grooming se agrava cuando el menor, por '
            'falta de orientación, no identifica a tiempo el peligro. En este módulo profundizaremos en cada una de estas '
            'etapas, compartiendo estadísticas, ejemplos prácticos y recomendaciones para comprender cómo se inicia y por '
            'qué es tan peligroso.'
        ),
        'orden': 1
    },
    {
        'titulo': 'Psicología del Groomer',
        'descripcion': 'Estrategias de manipulación y control emocional',
        'descripcion_detallada': (
            'Un groomer suele ser alguien que ha desarrollado habilidades para manipular y engañar, aprovechando la inocencia '
            'o vulnerabilidad de la víctima. Aunque no existe un perfil psicológico único, se han identificado ciertos '
            'rasgos y patrones de comportamiento:\n\n'
            '1. **Empatía fingida y carisma**: Fingir interés genuino en la vida de la víctima (sus problemas, aficiones o '
            'emociones) para ganarse su confianza.\n'
            '2. **Paciencia y persistencia**: No siempre buscan resultados inmediatos; a veces esperan semanas o meses '
            'para consolidar la relación.\n'
            '3. **Uso de la mentira y el engaño**: Adoptan identidades falsas (como otro adolescente, una chica/o de la '
            'misma edad o un famoso) para que la víctima baje la guardia.\n'
            '4. **Dominio de técnicas de persuasión**: Utilizan halagos, refuerzos positivos, promesas de ayuda y manipulación '
            'emocional (“si realmente te importo, mándame…”).\n'
            '5. **Capacidad de detectar vulnerabilidades**: Buscan menores con baja autoestima, problemas familiares o '
            'sentimientos de soledad para explotarlos.\n\n'
            '**Tácticas más comunes de un groomer:**\n'
            '- **Normalización del contenido sexual**: Comienzan introduciendo bromas o comentarios insinuantes de forma '
            'gradual, haciéndolo parecer normal.\n'
            '- **Gaslighting**: Hacer dudar a la víctima de sus percepciones y sentimientos, minimizando la gravedad de '
            'la situación (“no es para tanto”, “lo hacemos todos”).\n'
            '- **Chantaje**: Si logran obtener material íntimo, amenazan con difundirlo para forzar a la víctima a '
            'enviar más contenido o incluso concertar un encuentro.\n\n'
            'Conocer cómo opera la mente de un groomer nos ayuda a entender mejor cómo detectar señales tempranas de '
            'manipulación y así intervenir oportunamente.'
        ),
        'orden': 2
    },
    {
        'titulo': 'Identificación de Riesgos',
        'descripcion': 'Reconoce señales de peligro en entornos digitales',
        'descripcion_detallada': (
            'La detección temprana es clave para evitar que el grooming progrese. Algunas señales de alerta o indicadores '
            'de riesgo son:\n\n'
            '1. **Cambios repentinos en el comportamiento**: El menor puede volverse más reservado, ansioso o reaccionar '
            'con irritabilidad cuando se menciona su actividad en internet.\n'
            '2. **Secreto sobre sus interacciones en línea**: Cerrar ventanas de chat al sentir que alguien se acerca, '
            'borrar el historial o negarse a mostrar con quién habla.\n'
            '3. **Regalos o beneficios inexplicables**: Recibir recargas telefónicas, “skins” en videojuegos, dinero o '
            'obsequios sin un origen claro.\n'
            '4. **Nuevos contactos sospechosos**: Un adulto (o desconocido) que insiste en mantener conversaciones '
            'privadas, hace preguntas íntimas o pide fotos.\n'
            '5. **Lenguaje sexualizado o adulto**: Si el menor empieza a usar términos o expresiones inusuales de '
            'índole sexual, puede significar que alguien lo está exponiendo a esa temática.\n\n'
            '**Casos en videojuegos y foros**:\n'
            '- Plataformas como Discord, Twitch, Roblox o Fortnite pueden servir para el contacto inicial, aprovechando '
            'chat de voz o mensajería privada. A menudo, los agresores intentan llevar la conversación fuera de la '
            'plataforma pública hacia un espacio más privado. \n\n'
            'Este módulo aborda historias reales y ejemplos de conversaciones, explicando qué hacer si sospechas que un '
            'menor está siendo víctima de grooming.'
        ),
        'orden': 3
    },
    {
        'titulo': 'Estrategias de Protección',
        'descripcion': 'Técnicas de prevención y defensa digital',
        'descripcion_detallada': (
            'Protegerse contra el grooming requiere una combinación de educación digital, supervisión responsable y uso '
            'de herramientas de seguridad. Algunas acciones clave:\n\n'
            '1. **Hablar abiertamente en familia**: Fomentar la confianza para que los menores puedan contar sin miedo '
            'si algo les incomoda en internet.\n'
            '2. **Establecer límites de tiempo y contenido**: Orientar sobre cuánto tiempo y en qué plataformas pueden '
            'navegar o jugar, explicando los riesgos de compartir información personal.\n'
            '3. **Control parental y seguridad**: Utilizar software que bloquee ciertos sitios o filtre contenido '
            'inapropiado. Revisar periódicamente (de forma acordada) los contactos del menor.\n'
            '4. **Enseñar ciberseguridad**: Explicar la importancia de contraseñas seguras, el uso de verificación en '
            'dos pasos y la desconfianza ante enlaces sospechosos.\n'
            '5. **Fomentar el pensamiento crítico**: Ayudar a reconocer conductas inapropiadas, entender que “no todo '
            'lo que se ve en línea es cierto” y que no todos son quienes dicen ser.\n\n'
            '**Pasos adicionales en caso de sospecha:**\n'
            '- Bloquear de inmediato al contacto sospechoso.\n'
            '- Recopilar evidencias (capturas de pantalla, mensajes) y no borrarlas.\n'
            '- Buscar ayuda de profesionales, denunciar ante la plataforma y, si es grave, a las autoridades.\n\n'
            'Este módulo brinda recomendaciones para padres, docentes y los propios jóvenes, promoviendo una cultura de '
            'autocuidado digital y responsabilidad compartida.'
        ),
        'orden': 4
    },
    {
        'titulo': 'Seguridad en Redes Sociales',
        'descripcion': 'Configuración de privacidad y gestión de contactos',
        'descripcion_detallada': (
            'Las redes sociales se han convertido en el principal canal de contacto para la mayoría de grooming, debido a '
            'su amplia difusión entre menores. Para minimizar el riesgo:\n\n'
            '1. **Perfiles privados**: En plataformas como Instagram, Facebook y TikTok, configura la cuenta como privada '
            'para que solo amigos o conocidos puedan ver publicaciones.\n'
            '2. **Selección rigurosa de contactos**: Acepta o sigue únicamente a personas que realmente conozcas. Desconfía '
            'de perfiles sin foto, con pocos seguidores o con información contradictoria.\n'
            '3. **Desactivar la ubicación**: Evitar el uso de geolocalización en tiempo real y no etiquetar lugares que '
            'frecuentas, como escuela o tu casa.\n'
            '4. **Filtros de mensajes**: Muchas redes permiten desactivar o filtrar mensajes directos de desconocidos; '
            'activa esta opción para evitar contactos no deseados.\n'
            '5. **Bloqueo y reporte**: Si alguien te hace sentir incómodo o intenta que hagas algo que no quieres, bloquea '
            'y reporta inmediatamente a la plataforma.\n\n'
            'En este módulo se incluyen guías prácticas para configurar la privacidad de manera adecuada en diferentes '
            'aplicaciones y consejos para detectar cuentas falsas o posibles estafas.'
        ),
        'orden': 5
    },
    {
        'titulo': 'Marco Legal',
        'descripcion': 'Leyes y consecuencias del grooming',
        'descripcion_detallada': (
            'Cada vez más países cuentan con legislaciones que tipifican el grooming como delito, pudiendo conllevar penas '
            'de prisión y registro en bases de delincuentes sexuales. \n\n'
            '**Aspectos legales más relevantes:**\n'
            '1. **Leyes y códigos penales**: Países como España, Argentina, México y Chile, entre otros, contemplan penas '
            'para el ciberacoso sexual a menores. Dependiendo del país, la condena puede variar.\n'
            '2. **Proceso de denuncia**: Es vital recopilar evidencias (conversaciones, capturas de pantalla, fotos o '
            'videos) y presentarlas a la policía local o fiscalía especializada en delitos informáticos.\n'
            '3. **Protección a la víctima**: En muchos lugares, la víctima tiene derecho a medidas de protección, asesoría '
            'psicológica y asistencia legal gratuita.\n'
            '4. **Cooperación de plataformas**: Redes sociales y compañías tecnológicas suelen colaborar con las autoridades '
            'para bloquear y rastrear a agresores, especialmente cuando se aporta prueba suficiente.\n'
            '5. **Delitos conexos**: A menudo el grooming deriva en producción y distribución de pornografía infantil, lo cual '
            'agrega cargos legales más graves.\n\n'
            'Este módulo explica cómo proceder ante la sospecha o confirmación de un caso de grooming, qué organismos de '
            'ayuda existen y qué derechos y recursos amparan a las víctimas. Recuerda que denunciar no solo detiene al '
            'agresor, sino que puede prevenir nuevos casos de abuso.'
        ),
        'orden': 6
    }
]

# Insertar módulos en la base de datos
for modulo in modulos_estaticos:
    insertar_modulo(modulo['titulo'], modulo['descripcion'], modulo['descripcion_detallada'], modulo['orden'])

# Obtener IDs de módulos insertados
modulo_ids = {}
with conn.cursor() as cur:
    cur.execute("SELECT id_modulo, titulo FROM Modulos")
    for row in cur.fetchall():
        modulo_ids[row[1]] = row[0]

def pregunta_existe(texto_pregunta, modulo_id):
    """Verifica si una pregunta ya existe en la base de datos."""
    query = "SELECT id_pregunta FROM Preguntas WHERE texto_pregunta = %s AND modulo_id = %s"
    with conn.cursor() as cur:
        cur.execute(query, (texto_pregunta, modulo_id))
        return cur.fetchone() is not None

def insertar_pregunta(modulo_titulo, texto_pregunta, opciones):
    """Inserta una pregunta en la base de datos si no existe."""
    modulo_id = modulo_ids.get(modulo_titulo)
    if not modulo_id:
        print(f"⚠️ No se encontró el módulo '{modulo_titulo}'. Saltando pregunta.")
        return

    if pregunta_existe(texto_pregunta, modulo_id):
        print(f"⚠️ Pregunta '{texto_pregunta}' ya existe. No se inserta.")
        return

    query = """INSERT INTO Preguntas (modulo_id, texto_pregunta, tipo, opciones)
               VALUES (%s, %s, 'opcion multiple', %s)"""
    with conn.cursor() as cur:
        cur.execute(query, (modulo_id, texto_pregunta, json.dumps(opciones)))
    conn.commit()
    print(f"✅ Pregunta '{texto_pregunta}' insertada correctamente.")

# Preguntas estáticas
preguntas_estaticas = [
    # === Módulo 1: Grooming: Conceptos Fundamentales ===
    {
        'modulo': 'Grooming: Conceptos Fundamentales',
        'pregunta': '¿Qué es el grooming?',
        'opciones': [
            {'texto': 'Un delito de acoso en línea dirigido principalmente a menores', 'es_correcta': True},
            {'texto': 'Un deporte de competencia internacional', 'es_correcta': False},
            {'texto': 'Una plataforma de mensajería segura', 'es_correcta': False}
        ]
    },
    {
        'modulo': 'Grooming: Conceptos Fundamentales',
        'pregunta': '¿Cuál de las siguientes etapas describe un paso común en el grooming?',
        'opciones': [
            {'texto': 'Aislamiento y secretismo en la relación con el agresor', 'es_correcta': True},
            {'texto': 'Reporte inmediato a las autoridades', 'es_correcta': False},
            {'texto': 'Acceso controlado a redes sociales por parte de los padres', 'es_correcta': False}
        ]
    },

    # === Módulo 2: Psicología del Groomer ===
    {
        'modulo': 'Psicología del Groomer',
        'pregunta': '¿Qué rasgo suelen mostrar los groomers para ganarse la confianza de la víctima?',
        'opciones': [
            {'texto': 'Empatía fingida y halagos constantes', 'es_correcta': True},
            {'texto': 'Aversión a cualquier contacto en línea', 'es_correcta': False},
            {'texto': 'Miedo a hablar de temas personales', 'es_correcta': False}
        ]
    },
    {
        'modulo': 'Psicología del Groomer',
        'pregunta': '¿Qué técnica utilizan para manipular a la víctima?',
        'opciones': [
            {'texto': 'Gaslighting, haciendo que dude de su percepción', 'es_correcta': True},
            {'texto': 'Mostrar su identidad real desde el inicio', 'es_correcta': False},
            {'texto': 'Ignorar por completo las emociones de la víctima', 'es_correcta': False}
        ]
    },

    # === Módulo 3: Identificación de Riesgos ===
    {
        'modulo': 'Identificación de Riesgos',
        'pregunta': '¿Cuál de estas situaciones puede ser señal de grooming?',
        'opciones': [
            {'texto': 'Un adulto desconocido envía regalos virtuales o dinero sin razón', 'es_correcta': True},
            {'texto': 'Tener un debate público en un foro escolar', 'es_correcta': False},
            {'texto': 'Compartir memes con tu grupo de amigos cercanos', 'es_correcta': False}
        ]
    },
    {
        'modulo': 'Identificación de Riesgos',
        'pregunta': '¿Qué conducta puede mostrar una víctima al ser aislada por un groomer?',
        'opciones': [
            {'texto': 'Evitar hablar de su nuevo “amigo” y ocultar conversaciones', 'es_correcta': True},
            {'texto': 'Contar abiertamente a familiares y amigos quién le escribe', 'es_correcta': False},
            {'texto': 'Sentirse muy feliz y seguro al compartir datos personales', 'es_correcta': False}
        ]
    },

    # === Módulo 4: Estrategias de Protección ===
    {
        'modulo': 'Estrategias de Protección',
        'pregunta': '¿Qué práctica es clave para prevenir el grooming?',
        'opciones': [
            {'texto': 'Mantener comunicación abierta y enseñar ciberseguridad básica', 'es_correcta': True},
            {'texto': 'Aceptar solicitudes de amistad de todos para sociabilizar más', 'es_correcta': False},
            {'texto': 'Confiar en que todas las personas en internet son sinceras', 'es_correcta': False}
        ]
    },
    {
        'modulo': 'Estrategias de Protección',
        'pregunta': '¿Cuál es la medida correcta ante sospecha de grooming?',
        'opciones': [
            {'texto': 'Bloquear al agresor y recopilar evidencias antes de denunciarlas', 'es_correcta': True},
            {'texto': 'Ignorar los mensajes y no contárselo a nadie', 'es_correcta': False},
            {'texto': 'Compartir más datos para “desenmascarar” al groomer', 'es_correcta': False}
        ]
    },

    # === Módulo 5: Seguridad en Redes Sociales ===
    {
        'modulo': 'Seguridad en Redes Sociales',
        'pregunta': '¿Qué configuración contribuye a evitar el contacto de desconocidos?',
        'opciones': [
            {'texto': 'Mantener la cuenta privada o con acceso solo a amigos', 'es_correcta': True},
            {'texto': 'Publicar libremente ubicación y rutina diaria', 'es_correcta': False},
            {'texto': 'Aceptar peticiones de todo el mundo para tener más seguidores', 'es_correcta': False}
        ]
    },
    {
        'modulo': 'Seguridad en Redes Sociales',
        'pregunta': '¿Cuál es una buena práctica de seguridad en redes sociales?',
        'opciones': [
            {'texto': 'Bloquear y reportar perfiles que solicitan información íntima', 'es_correcta': True},
            {'texto': 'Mantener contacto con extraños para conocer “nuevos amigos”', 'es_correcta': False},
            {'texto': 'Publicar contenido explícito para “desmotivar” a groomers', 'es_correcta': False}
        ]
    },

    # === Módulo 6: Marco Legal ===
    {
        'modulo': 'Marco Legal',
        'pregunta': '¿Qué se debe hacer al sospechar de un caso de grooming?',
        'opciones': [
            {'texto': 'Guardar evidencias (mensajes, capturas) y denunciar a las autoridades', 'es_correcta': True},
            {'texto': 'Exponerlo públicamente en redes sociales sin contactar a la policía', 'es_correcta': False},
            {'texto': 'Esperar a tener más pruebas sin actuar ni consultar a nadie', 'es_correcta': False}
        ]
    },
    {
        'modulo': 'Marco Legal',
        'pregunta': '¿Por qué es importante denunciar un caso de grooming?',
        'opciones': [
            {'texto': 'Para detener al agresor y prevenir nuevos abusos a otras víctimas', 'es_correcta': True},
            {'texto': 'Para castigar a la víctima y quitarle credibilidad', 'es_correcta': False},
            {'texto': 'Porque no existen consecuencias legales reales contra el agresor', 'es_correcta': False}
        ]
    }
]

# Insertar preguntas en la base de datos
for pregunta in preguntas_estaticas:
    insertar_pregunta(pregunta['modulo'], pregunta['pregunta'], pregunta['opciones'])

# Cerrar conexión
conn.close()
print("🔌 Conexión cerrada.")
