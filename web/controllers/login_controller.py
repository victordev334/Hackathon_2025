# controllers/login.py
import web
from models.login import UsuarioModel

# Se asume que tus vistas se encuentran en la carpeta 'views'
render = web.template.render('views', base='master')

class Login:
    def GET(self):
        # Muestra el formulario de login (archivo login.html)
        return render.login()

    def POST(self):
        # Recoge los datos enviados desde el formulario
        data = web.input()
        username = data.get('username')
        password = data.get('password')
        
        usuario_model = UsuarioModel()
        user = usuario_model.login(username, password)
        usuario_model.close_connection()

        if user:
            # Si el usuario se autentica correctamente, se muestra un mensaje de bienvenida.
            # En una aplicación real se debería iniciar una sesión, establecer cookies, etc.
            mensaje = "Login exitoso, bienvenido {0} {1}".format(user[1], user[2])
            return render.index(message=mensaje)
        else:
            # Si falla la autenticación se recarga el formulario mostrando un error.
            return render.login(error="Credenciales inválidas, inténtalo de nuevo.")
