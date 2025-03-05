import web
import json
from models.usuario_model import UsuarioModel

class Modulos:
    def GET(self):
        # Create an instance of UsuarioModel to access module methods
        usuario_model = UsuarioModel()
        
        # Fetch the list of modules
        modulos = usuario_model.obtener_modulos()
        
        # Close the database connection
        usuario_model.close_connection()
        
        # Render the modules view and pass the modules data
        render = web.template.render('views', base='master')
        return render.modulos(modulos)
    
    def POST(self):
        # Handle POST requests for module details
        usuario_model = UsuarioModel()
        data = web.input()
        
        # Get module details based on module ID
        module_id = int(data.get('modulo_id', 0))
        module_details = usuario_model.obtener_detalle_modulo(module_id)
        
        usuario_model.close_connection()
        
        # Return module details as JSON
        web.header('Content-Type', 'application/json')
        return json.dumps(module_details)
    
    def PUT(self):
        # Handle module progress tracking
        usuario_model = UsuarioModel()
        data = web.input()
        
        # Example of registering module progress
        result = usuario_model.registrar_progreso_modulo(
            usuario_id=data.get('usuario_id'),
            modulo_id=data.get('modulo_id'),
            porcentaje=data.get('porcentaje')
        )
        
        usuario_model.close_connection()
        
        # Return a response indicating success or failure
        return web.ok() if result else web.internalerror()