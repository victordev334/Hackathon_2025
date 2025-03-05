# app.py
import os
import web

from controllers.login_controller import Login as LoginController
from controllers.registro_controller import Registro as RegistroController
from controllers.modulos_controller import (
    ModulosAPI as ModulosAPIController,
    ModulosVista as ModulosVistaController
)

# Rutas de la aplicación
urls = (
    '/', 'Index',
    '/Login', LoginController,
    '/Registro', RegistroController,
    '/Modulos', ModulosAPIController,       
    '/ModulosVista', ModulosVistaController 
)

# Inicializar la aplicación
app = web.application(urls, globals())

# Crear carpeta 'sessions' si no existe
if not os.path.exists('sessions'):
    os.makedirs('sessions')

# Configurar sesión en disco
session_store = web.session.DiskStore('sessions')

# Inicializar sesión (la asignamos a `web.ctx.session`)
session = web.session.Session(app, session_store, initializer={'user_id': None})

# 🔥 IMPORTANTE: Hacer que `session` esté disponible en `web.ctx`
def session_hook():
    web.ctx.session = session

# Añadir el hook para asegurarnos de que `session` está disponible en todas las peticiones
app.add_processor(web.loadhook(session_hook))

# Renderizador de vistas
render = web.template.render('views', base='master')

class Index:
    def GET(self):
        return render.index()

if __name__ == "__main__":
    app.run()
