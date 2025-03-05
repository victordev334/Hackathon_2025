import web
from models.principal import PrincipalModel  # Importa correctamente el modelo

# Asegúrate de tener la ruta para renderizar la vista correctamente
render = web.template.render('views', base='master')  # Asumiendo que 'master' es la plantilla base

class Principal:
    def __init__(self):
        self.model = PrincipalModel()  # Crea una instancia de PrincipalModel en lugar de Principal

    def GET(self):
        try:
            # Obtener los datos del modelo
            modulos = self.model.get_modulos()
            estadisticas = self.model.get_estadisticas()
            recursos = self.model.get_recursos()
            denuncias_info = self.model.get_denuncias_info()
            bot_features = self.model.get_bot_features()

            # Pasar los datos a la vista
            return render.principal(modulos=modulos, 
                                    estadisticas=estadisticas, 
                                    recursos=recursos, 
                                    denuncias_info=denuncias_info, 
                                    bot_features=bot_features)
        except Exception as e:
            print("❌ Error obteniendo datos en el controlador principal:", str(e))
            return render.error(message="Ocurrió un error al cargar la información.")
