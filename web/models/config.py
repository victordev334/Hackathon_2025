import os
from dotenv import load_dotenv

# Cargar el archivo .env
load_dotenv()

# Extraer las variables de entorno necesarias
DATABASE_URL = os.getenv('DATABASE_URL')
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
