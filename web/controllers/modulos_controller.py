# controllers/modulos_controller.py
import web
import json
from models.modulos_models import UsuarioModel

render = web.template.render('views/', base='master')

class ModulosVista:
    """Vista para renderizar la lista de módulos en HTML"""
    
    def GET(self):
        # Validar sesión usando web.ctx.session en lugar de importar `session`
        if not hasattr(web.ctx, 'session') or not web.ctx.session.get('user_id'):
            raise web.seeother('/Login')

        usuario_model = UsuarioModel()
        try:
            modulos = usuario_model.obtener_modulos()
        finally:
            usuario_model.close_connection()
        
        return render.modulos(modulos)


class ModulosAPI:
    """API para obtener módulos y detalles en JSON"""

    def GET(self):
        if not hasattr(web.ctx, 'session') or not web.ctx.session.get('user_id'):
            web.header('Content-Type', 'application/json')
            return json.dumps({"success": False, "error": "No hay sesión activa"})

        usuario_model = UsuarioModel()
        try:
            modulos = usuario_model.obtener_modulos()
        finally:
            usuario_model.close_connection()

        web.header('Content-Type', 'application/json')
        return json.dumps(modulos)

    def POST(self):
        if not hasattr(web.ctx, 'session') or not web.ctx.session.get('user_id'):
            web.header('Content-Type', 'application/json')
            return json.dumps({"success": False, "error": "No hay sesión activa"})

        data = json.loads(web.data().decode('utf-8'))
        modulo_id = data.get('modulo_id')

        if not modulo_id:
            web.header('Content-Type', 'application/json')
            return json.dumps({"success": False, "error": "Módulo no válido"})

        usuario_model = UsuarioModel()
        try:
            if data.get('complete'):
                user_id = web.ctx.session.get('user_id')
                exito = usuario_model.marcar_modulo_completado(user_id, modulo_id)
                web.header('Content-Type', 'application/json')
                return json.dumps({"success": exito, "message": "Módulo completado" if exito else "Error al completar módulo"})
            else:
                modulo_detalles = usuario_model.obtener_detalle_modulo(modulo_id)
                web.header('Content-Type', 'application/json')
                return json.dumps(modulo_detalles if modulo_detalles else {"error": "Módulo no encontrado"})
        finally:
            usuario_model.close_connection()
