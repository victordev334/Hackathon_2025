import web
import json
from models.modulos_models import UsuarioModel

class ModulosAPI:
    """Clase para la API de módulos (devuelve JSON)"""
    def GET(self):
        usuario_model = UsuarioModel()
        try:
            modulos = usuario_model.obtener_modulos()
        finally:
            usuario_model.close_connection()

        web.header('Content-Type', 'application/json')
        return json.dumps(modulos)
    
    def POST(self):
        """Permite obtener detalles de un módulo específico"""
        usuario_model = UsuarioModel()
        try:
            data = json.loads(web.data().decode('utf-8'))
            modulo_id = int(data.get('modulo_id', 0))
            modulo_detalles = usuario_model.obtener_detalle_modulo(modulo_id)
        finally:
            usuario_model.close_connection()

        web.header('Content-Type', 'application/json')
        return json.dumps(modulo_detalles)

class ModulosVista:
    """Clase para la vista de módulos (devuelve HTML)"""
    def GET(self):
        usuario_model = UsuarioModel()
        try:
            modulos = usuario_model.obtener_modulos()
        finally:
            usuario_model.close_connection()

        render = web.template.render('views', base='master')
        return render.modulos(modulos)

