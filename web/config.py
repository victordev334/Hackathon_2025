import os
from dotenv import load_dotenv

# Cargar el archivo .env
load_dotenv()

# Extraer las variables de entorno necesarias
DATABASE_URL = os.getenv('DATABASE_URL')
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

# Verificación de carga de variables
print("DATABASE_URL:", DATABASE_URL)
print("SUPABASE_URL:", SUPABASE_URL)
print("SUPABASE_KEY:", "Cargado" if SUPABASE_KEY else "No cargado")
print("SECRET_KEY:", "Cargado" if SECRET_KEY else "No cargado")
