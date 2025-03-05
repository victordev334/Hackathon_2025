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

def actualizar_o_insertar_modulo(titulo, descripcion, descripcion_detallada, orden):
    """Si el módulo existe, lo actualiza; si no, lo inserta."""
    query_check = "SELECT id_modulo FROM Modulos WHERE titulo = %s"
    query_update = """UPDATE Modulos SET descripcion = %s, descripcion_detallada = %s, orden = %s WHERE titulo = %s"""
    query_insert = """INSERT INTO Modulos (titulo, descripcion, descripcion_detallada, orden) VALUES (%s, %s, %s, %s)"""

    with conn.cursor() as cur:
        cur.execute(query_check, (titulo,))
        modulo_existente = cur.fetchone()

        if modulo_existente:
            cur.execute(query_update, (descripcion, descripcion_detallada, orden, titulo))
            print(f"♻️ Módulo '{titulo}' actualizado correctamente.")
        else:
            cur.execute(query_insert, (titulo, descripcion, descripcion_detallada, orden))
            print(f"✅ Módulo '{titulo}' insertado correctamente.")
    
    conn.commit()

# Módulos estáticos en texto plano (sin Markdown)
modulos_estaticos = [
    {
        'titulo': 'Grooming: Conceptos Fundamentales',
        'descripcion': 'Comprender el acoso sexual online en profundidad',
        'descripcion_detallada': (
            "El grooming es un tipo de acoso sexual en línea en el que un adulto busca ganarse la confianza de un menor con fines de explotación. "
            "A menudo, el agresor adopta una identidad falsa o se hace pasar por alguien de la misma edad para acercarse a la víctima. "
            "Características principales del grooming: "
            "Está dirigido a niños, niñas y adolescentes, aunque también puede ocurrir contra adultos vulnerables. "
            "Se basa en la manipulación emocional y la construcción de una relación de confianza. "
            "Puede ocurrir en redes sociales como Instagram, TikTok, Facebook, videojuegos en línea como Roblox, Fortnite, chats o aplicaciones de mensajería. "
            "Etapas comunes en el grooming: "
            "1. Contacto inicial: El agresor localiza a la víctima y envía solicitudes de amistad o inicia conversaciones casuales. "
            "2. Construcción de confianza: Halagos, escucha activa e interés en hobbies o problemas personales para establecer un vínculo. "
            "3. Aislamiento: El groomer convence a la víctima de mantener la relación en secreto. "
            "4. Incremento de la intimidad: Introduce temas sexuales, solicita fotos personales y lo hace ver como un juego. "
            "5. Explotación: Chantajea con material íntimo para exigir más contenido o incluso un encuentro físico. "
            "Importancia de la prevención: "
            "Es crucial que los menores reciban educación digital para identificar el grooming y evitar caer en manipulación."
        ),
        'orden': 1
    },
    {
        'titulo': 'Psicología del Groomer',
        'descripcion': 'Estrategias de manipulación y control emocional',
        'descripcion_detallada': (
            "Los groomers desarrollan habilidades para manipular a sus víctimas, fingiendo empatía, usando mentiras y detectando vulnerabilidades. "
            "Métodos que emplean: "
            "1. Fingir interés genuino en la vida de la víctima para ganarse su confianza. "
            "2. Paciencia y persistencia, esperando semanas o meses para consolidar la relación. "
            "3. Adoptar identidades falsas para que la víctima baje la guardia. "
            "4. Usar halagos, refuerzos positivos y manipulación emocional para convencer a la víctima. "
            "5. Identificar y explotar vulnerabilidades como baja autoestima o problemas familiares. "
            "Comprender cómo opera la mente de un groomer nos ayuda a detectar señales tempranas de manipulación y a intervenir oportunamente."
        ),
        'orden': 2
    },
    {
        'titulo': 'Identificación de Riesgos',
        'descripcion': 'Reconoce señales de peligro en entornos digitales',
        'descripcion_detallada': (
            "Es fundamental identificar señales de alerta en casos de grooming. "
            "Señales de peligro: "
            "1. Cambios repentinos en el comportamiento, como ansiedad o aislamiento. "
            "2. Secreto sobre interacciones en línea, borrar historiales o negar contactos. "
            "3. Recibir regalos, dinero o beneficios sin explicación. "
            "4. Adultos desconocidos insistiendo en mantener conversaciones privadas. "
            "5. Uso de lenguaje sexualizado o adulto en conversaciones. "
            "El conocimiento de estas señales ayuda a prevenir que el grooming avance."
        ),
        'orden': 3
    },
    {
        'titulo': 'Estrategias de Protección',
        'descripcion': 'Técnicas de prevención y defensa digital',
        'descripcion_detallada': (
            "Prevenir el grooming requiere educación digital, supervisión responsable y herramientas de seguridad. "
            "Estrategias clave: "
            "1. Hablar abiertamente con los menores sobre seguridad en internet. "
            "2. Establecer límites de tiempo y contenido en redes sociales. "
            "3. Uso de controles parentales y filtros de seguridad. "
            "4. Enseñar ciberseguridad: uso de contraseñas seguras y evitar compartir datos personales. "
            "5. Fomentar el pensamiento crítico para detectar posibles engaños en internet."
        ),
        'orden': 4
    },
    {
        'titulo': 'Seguridad en Redes Sociales',
        'descripcion': 'Configuración de privacidad y gestión de contactos',
        'descripcion_detallada': (
            "Las redes sociales pueden ser un canal de contacto para el grooming si no se configuran correctamente. "
            "Medidas de seguridad: "
            "1. Mantener perfiles privados en redes sociales. "
            "2. Aceptar solicitudes solo de personas conocidas. "
            "3. Desactivar la ubicación en publicaciones y en tiempo real. "
            "4. Filtrar mensajes para evitar contacto con desconocidos. "
            "5. Bloquear y reportar cuentas sospechosas que soliciten información personal."
        ),
        'orden': 5
    },
    {
        'titulo': 'Marco Legal',
        'descripcion': 'Leyes y consecuencias del grooming',
        'descripcion_detallada': (
            "El grooming es un delito en muchos países y puede conllevar penas de prisión. "
            "Aspectos legales: "
            "1. Leyes en diferentes países establecen castigos severos para el grooming. "
            "2. Proceso de denuncia: recopilar evidencias y contactar autoridades. "
            "3. Protección a la víctima: derecho a asistencia legal y psicológica. "
            "4. Redes sociales colaboran con autoridades para rastrear a agresores. "
            "5. El grooming puede derivar en delitos más graves como la pornografía infantil. "
            "Denunciar estos casos es clave para proteger a más personas y prevenir nuevos abusos."
        ),
        'orden': 6
    }
]

# Insertar o actualizar módulos en la base de datos
for modulo in modulos_estaticos:
    actualizar_o_insertar_modulo(modulo['titulo'], modulo['descripcion'], modulo['descripcion_detallada'], modulo['orden'])

# Cerrar conexión
conn.close()
print("🔌 Conexión cerrada.")
