import web
import json
from models.login import UsuarioModel

class Login:
    def GET(self):
        render = web.template.render('views', base='master')
        return render.login()

    def POST(self):
        try:
            data = json.loads(web.data().decode('utf-8'))
            username = data.get("username", "").strip().lower()
            password = data.get("password", "")

            print(f"📌 Intentando iniciar sesión con: {username}")

            usuario_model = UsuarioModel()
            user = usuario_model.login(username, password)  # Retorna (id_usuario, nombre_usuario, contraseña)
            usuario_model.close_connection()

            if user:
                web.ctx.session.user_id = user[0]
                web.ctx.session.user_name = user[1]  # 🔥 Guardamos el nombre en sesión también

                print(f"✅ Usuario autenticado: {user[1]} (ID: {user[0]})")

                return json.dumps({
                    "success": True,
                    "message": "Inicio de sesión exitoso",
                    "user_id": user[0],
                    "user_name": user[1]  # 🔥 Aseguramos que se envía al frontend
                })
            else:
                print("❌ Credenciales incorrectas")
                return json.dumps({"success": False, "error": "Credenciales incorrectas"})

        except Exception as e:
            print("❌ ERROR en login:", str(e))
            return json.dumps({"success": False, "error": "Error en el servidor"})
