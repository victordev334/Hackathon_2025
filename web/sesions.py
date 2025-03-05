import os
import web

# Crear carpeta 'sessions' si no existe
if not os.path.exists('sessions'):
    os.makedirs('sessions')

# Configurar sesión en disco
session_store = web.session.DiskStore('sessions')

# Inicializar sesión
session = web.session.Session(None, session_store, initializer={'user_id': None})
