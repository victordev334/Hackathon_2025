import web
from controllers.login_controller import Login as LoginController
from controllers.registro_controller import Registro as RegistroController
from controllers.modulos_controller import ModulosAPI as ModulosAPIController, ModulosVista as ModulosVistaController

# Definimos las rutas de la aplicación
urls = (
    '/', 'Index',
    '/Login', LoginController,
    '/Registro', RegistroController,
    '/Modulos', ModulosAPIController,  # API que devuelve JSON
    '/ModulosVista', ModulosVistaController  # Vista que muestra los módulos en HTML
)

# Inicializar la aplicación
app = web.application(urls, globals())
render = web.template.render('views', base='master')

# Página principal
class Index:
    def GET(self):
        return render.index()

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run()
