import web
from controllers.login_controller import Login as LoginController
from controllers.registro_controller import Registro as RegistroController
from controllers.modulos_controller import ModulosAPI as ModulosAPIController, ModulosVista as ModulosVistaController

urls = (
    '/', 'Index',
    '/Login', LoginController,
    '/Registro', RegistroController,
    '/Modulos', ModulosAPIController,  # API que devuelve JSON
    '/ModulosVista', ModulosVistaController,  # Vista que muestra los módulos
)

app = web.application(urls, globals())
render = web.template.render('views', base='master')

class Index:
    def GET(self):
        return render.index()

if __name__ == "__main__":
    app.run()
