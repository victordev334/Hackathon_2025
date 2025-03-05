import web
import json
from models.modulos_models import UsuarioModel

render = web.template.render('views/', base='master')

class ModulosVista:
    """Vista para renderizar la lista de módulos en HTML"""
    
    def GET(self):
        usuario_model = UsuarioModel()
        try:
            modulos = usuario_model.obtener_modulos()
        finally:
            usuario_model.close_connection()
        
        return render.modulos(modulos)



class ModulosAPI:
    """API para obtener módulos y detalles en JSON"""

    def GET(self):
        usuario_model = UsuarioModel()
        try:
            modulos = usuario_model.obtener_modulos()
        finally:
            usuario_model.close_connection()

        web.header('Content-Type', 'application/json')
        return json.dumps(modulos)

    def POST(self):
        """Obtener detalles de un módulo en JSON"""
        usuario_model = UsuarioModel()
        try:
            data = json.loads(web.data().decode('utf-8'))
            modulo_id = data.get('modulo_id')

            if not modulo_id:
                return json.dumps({"error": "Módulo no válido"})

            modulo_detalles = usuario_model.obtener_detalle_modulo(modulo_id)

            if not modulo_detalles:
                return json.dumps({"error": "Módulo no encontrado"})

        finally:
            usuario_model.close_connection()

        web.header('Content-Type', 'application/json')
        return json.dumps(modulo_detalles)