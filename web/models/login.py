# models/usuario.py
import psycopg2
from config import DATABASE_URL

class UsuarioModel:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(DATABASE_URL)
        except Exception as e:
            print("Error conectando a la base de datos:", e)
            self.conn = None

    def login(self, username, password):
        """
        Busca en la base de datos un usuario cuyo nombre o correo coincida y la contraseña sea la indicada.
        Se asume que las contraseñas se almacenan en texto plano, pero en producción es recomendable usar hashing.
        """
        if not self.conn:
            return None
        
        query = """
            SELECT id_usuario, nombre, "primer_apellido", "segundo_apellido", correo
            FROM Usuarios
            WHERE (nombre = %s OR correo = %s) AND contraseña = %s
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute(query, (username, username, password))
                user = cur.fetchone()
            return user
        except Exception as e:
            print("Error en la consulta de login:", e)
            return None

    def close_connection(self):
        if self.conn:
            self.conn.close()
