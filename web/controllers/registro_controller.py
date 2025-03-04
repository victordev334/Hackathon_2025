# controllers/registro_controller.py
import web
import json
from models.registro_model import UsuarioRegistroModel

class Registro:
    def GET(self):
        # Mostrar el formulario de registro
        return web.template.render('views', base='master').registro()

    def POST(self):
        try:
            # Leer datos JSON desde la petición
            data = json.loads(web.data().decode('utf-8'))

            # Extraer datos del JSON recibido
            username = data.get('username')
            nombre = data.get('nombre')
            primer_apellido = data.get('primerApellido')
            segundo_apellido = data.get('segundoApellido', '')  # Si es None, lo pone como string vacío
            correo = data.get('correo')
            password = data.get('password')

            # Verificar que los datos esenciales están presentes
            if not all([username, nombre, primer_apellido, correo, password]):
                return json.dumps({"success": False, "error": "Todos los campos obligatorios deben llenarse."})

            # Intentar registrar el usuario en la base de datos
            usuario_model = UsuarioRegistroModel()
            new_id, error_msg = usuario_model.register(username, nombre, primer_apellido, segundo_apellido, correo, password)
            usuario_model.close_connection()

            if new_id:
                return json.dumps({"success": True, "message": "Usuario registrado correctamente."})
            else:
                return json.dumps({"success": False, "error": error_msg})

        except Exception as e:
            print("❌ ERROR en el registro:", str(e))
            return json.dumps({"success": False, "error": "Error en el servidor."})

