import psycopg2
import json
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
        """Obtiene todos los módulos disponibles en la base de datos."""
        if not self.conn:
            return []

        query = "SELECT id_modulo, titulo, descripcion FROM Modulos ORDER BY orden"
        try:
            with self.conn.cursor() as cur:
                cur.execute(query)
                modulos = cur.fetchall()

            return [{'id_modulo': m[0], 'titulo': m[1], 'descripcion': m[2]} for m in modulos]
        except Exception as e:
            print("❌ Error obteniendo módulos:", e)
            return []

    def obtener_detalle_modulo(self, modulo_id):
        """Obtiene el detalle de un módulo y sus preguntas."""
        if not self.conn:
            return None

        query_modulo = "SELECT id_modulo, titulo, descripcion_detallada FROM Modulos WHERE id_modulo = %s"
        query_preguntas = "SELECT id_pregunta, texto_pregunta, opciones FROM Preguntas WHERE modulo_id = %s"

        try:
            with self.conn.cursor() as cur:
                # Obtener datos del módulo
                cur.execute(query_modulo, (modulo_id,))
                modulo = cur.fetchone()

                # Si el módulo no existe, devolver None
                if not modulo:
                    return None

                # Obtener preguntas del módulo
                cur.execute(query_preguntas, (modulo_id,))
                preguntas = cur.fetchall()

            preguntas_list = []
            for p in preguntas:
                opciones = p[2]  # `opciones` ya es JSONB en PostgreSQL, lo traemos directamente
                if isinstance(opciones, str):  # Si por alguna razón es string, lo convertimos
                    try:
                        opciones = json.loads(opciones)
                    except json.JSONDecodeError:
                        print(f"❌ Error al decodificar opciones para la pregunta {p[0]}")
                        opciones = []

                preguntas_list.append({
                    'id_pregunta': p[0],
                    'texto_pregunta': p[1],
                    'opciones': opciones
                })

            return {
                'id_modulo': modulo[0],
                'titulo': modulo[1],
                'descripcion_detallada': modulo[2],
                'preguntas': preguntas_list
            }
        except Exception as e:
            print("❌ Error obteniendo detalles del módulo:", e)
            return None
