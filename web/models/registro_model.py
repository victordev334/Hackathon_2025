# models/usuario.py
import psycopg2
from config import DATABASE_URL

class UsuarioRegistroModel:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(DATABASE_URL)
        except Exception as e:
            print("Error conectando a la base de datos:", e)
            self.conn = None

    def register(self, username, nombre, primer_apellido, segundo_apellido, correo, password):
        """
        Intenta registrar un usuario. Si el correo ya existe, devuelve None con un mensaje de error.
        """
        if not self.conn:
            print("❌ ERROR: No hay conexión a la base de datos.")
            return None, "Error de conexión con la base de datos"

        query = """
            INSERT INTO Usuarios (nombre_usuario, nombre, primer_apellido, segundo_apellido, correo, contraseña)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id_usuario;
        """
        
        try:
            print(f"📌 Intentando insertar usuario: {username}, {nombre}, {primer_apellido}, {segundo_apellido}, {correo}")

            with self.conn.cursor() as cur:
                cur.execute(query, (username, nombre, primer_apellido, segundo_apellido, correo, password))
                new_id = cur.fetchone()[0]
                self.conn.commit()
                print(f"✅ Usuario insertado con ID: {new_id}")
                return new_id, None
            
        except psycopg2.IntegrityError as e:
            self.conn.rollback()
            print("❌ ERROR: El correo ya está registrado.")
            return None, "Este correo ya está registrado. Intente con otro correo."
        
        except Exception as e:
            self.conn.rollback()
            print(f"❌ ERROR en el registro de usuario: {e}")
            return None, "Error desconocido en la base de datos"


    def close_connection(self):
        if self.conn:
            self.conn.close()
