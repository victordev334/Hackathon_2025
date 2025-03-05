import psycopg2
from config import DATABASE_URL

class UsuarioModel:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(DATABASE_URL)
            print("✅ Conexión a la base de datos establecida correctamente.")
        except Exception as e:
            print("❌ ERROR conectando a la base de datos:", e)
            self.conn = None

    def close_connection(self):
        """Cierra la conexión con la base de datos"""
        if self.conn:
            self.conn.close()
            print("🔌 Conexión cerrada correctamente.")

    def obtener_modulos(self):
        """
        Obtiene la lista de módulos combinando los de la base de datos con los módulos estáticos.
        """
        modulos_estaticos = [
            {'id_modulo': 1, 'titulo': 'Grooming: Conceptos Fundamentales', 'descripcion': 'Comprender el acoso sexual online en profundidad', 'emoji': '🕵️'},
            {'id_modulo': 2, 'titulo': 'Psicología del Groomer', 'descripcion': 'Estrategias de manipulación y control emocional', 'emoji': '🎭'},
            {'id_modulo': 3, 'titulo': 'Identificación de Riesgos', 'descripcion': 'Reconoce señales de peligro en entornos digitales', 'emoji': '🚨'},
            {'id_modulo': 4, 'titulo': 'Estrategias de Protección', 'descripcion': 'Técnicas de prevención y defensa digital', 'emoji': '🛡️'},
            {'id_modulo': 5, 'titulo': 'Seguridad en Redes Sociales', 'descripcion': 'Configuración de privacidad y gestión de contactos', 'emoji': '📱'},
            {'id_modulo': 6, 'titulo': 'Marco Legal', 'descripcion': 'Leyes y consecuencias del grooming', 'emoji': '⚖️'}
        ]

        if not self.conn:
            return modulos_estaticos  # Si la BD falla, devolver solo los estáticos

        query = "SELECT id_modulo, titulo, descripcion FROM Modulos ORDER BY orden"
        try:
            with self.conn.cursor() as cur:
                cur.execute(query)
                modulos_db = cur.fetchall()

            modulos_bd_dicts = [{'id_modulo': m[0], 'titulo': m[1], 'descripcion': m[2], 'emoji': '📘'} for m in modulos_db]

            titulos_en_bd = {m['titulo'] for m in modulos_bd_dicts}
            modulos_final = modulos_bd_dicts + [m for m in modulos_estaticos if m['titulo'] not in titulos_en_bd]

            return modulos_final
        except Exception as e:
            print("❌ Error obteniendo módulos:", e)
            return modulos_estaticos

    def obtener_detalle_modulo(self, modulo_id):
        """
        Obtiene los detalles de un módulo específico desde la base de datos o los estáticos.
        """
        detalles_estaticos = {
            1: {'id_modulo': 1, 'titulo': 'Grooming: Conceptos Fundamentales', 'descripcion_detallada': 'Módulo introductorio...'},
            2: {'id_modulo': 2, 'titulo': 'Psicología del Groomer', 'descripcion_detallada': 'Análisis de estrategias psicológicas...'},
            3: {'id_modulo': 3, 'titulo': 'Identificación de Riesgos', 'descripcion_detallada': 'Reconocimiento de señales de peligro...'},
            4: {'id_modulo': 4, 'titulo': 'Estrategias de Protección', 'descripcion_detallada': 'Técnicas y herramientas para prevenir...'},
            5: {'id_modulo': 5, 'titulo': 'Seguridad en Redes Sociales', 'descripcion_detallada': 'Configuración de privacidad y seguridad...'},
            6: {'id_modulo': 6, 'titulo': 'Marco Legal', 'descripcion_detallada': 'Aspectos legales sobre el grooming...'}
        }

        if modulo_id in detalles_estaticos:
            return detalles_estaticos[modulo_id]

        if not self.conn:
            return None

        query = "SELECT id_modulo, titulo, descripcion FROM Modulos WHERE id_modulo = %s"
        try:
            with self.conn.cursor() as cur:
                cur.execute(query, (modulo_id,))
                modulo = cur.fetchone()
            
            if modulo:
                return {'id_modulo': modulo[0], 'titulo': modulo[1], 'descripcion_detallada': modulo[2]}
            return None
        except Exception as e:
            print("❌ Error obteniendo detalles del módulo:", e)
            return None
