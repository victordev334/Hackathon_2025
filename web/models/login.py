# models/usuario.py
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

    def login(self, username, password):
        """
        Busca en la base de datos un usuario cuyo nombre coincida y la contraseña sea la indicada.
        """
        if not self.conn:
            print("❌ ERROR: No hay conexión a la base de datos.")
            return None

        # Normalizar el input del usuario
        username = username.strip().lower()

        query = """
            SELECT id_usuario, nombre_usuario, contraseña
            FROM Usuarios
            WHERE LOWER(nombre_usuario) = %s
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute(query, (username,))
                user = cur.fetchone()

            if not user:
                print("❌ Usuario no encontrado")
                return None

            # Comparar la contraseña (asegúrate de que la contraseña en la BD esté en texto plano o usa hashing)
            stored_password = user[2]
            if stored_password == password:
                print(f"✅ Usuario autenticado correctamente: {user[1]}")
                return user
            else:
                print("❌ Contraseña incorrecta")
                return None

        except Exception as e:
            print("❌ Error en la consulta de login:", e)
            return None

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("🔌 Conexión cerrada correctamente.")
