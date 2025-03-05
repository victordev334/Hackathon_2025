# controllers/login.py
import web
import json
from models.login import UsuarioModel

class Login:
    def GET(self):
        return web.template.render('views', base='master').login()

    def POST(self):
        try:
            # Leer los datos JSON enviados desde JavaScript
            data = json.loads(web.data().decode('utf-8'))
            username = data.get("username").strip().lower()
            password = data.get("password")

            print(f"📌 Intentando iniciar sesión con: {username}")

            usuario_model = UsuarioModel()
            user = usuario_model.login(username, password)
            usuario_model.close_connection()

            if user:
                print(f"✅ Usuario autenticado: {user[1]}")
                return json.dumps({"success": True, "message": "Inicio de sesión exitoso", "user": user[1]})
            else:
                print("❌ Credenciales incorrectas")
                return json.dumps({"success": False, "error": "Credenciales incorrectas"})
                

        except Exception as e:
            print("❌ ERROR en login:", str(e))
            return json.dumps({"success": False, "error": "Error en el servidor"})
        
    class Principal1:
        def GET(self):
            return web.template.render('views', base='master').modulos()
