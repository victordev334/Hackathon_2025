import web
from controllers.login_controller import Login as LoginController
from controllers.registro_controller import Registro as RegistroController
from controllers.modulos_controller import Modulos as ModulosController

urls = (
    '/', 'Index',
    '/Login', LoginController,
    '/Registro', RegistroController,
    '/Modulos', ModulosController,
)

app = web.application(urls, globals())
render = web.template.render('views', base='master')

class Index:
    def GET(self):
        return render.index()

if __name__ == "__main__":
    app.run()