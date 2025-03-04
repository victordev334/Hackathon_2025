# Hackathon_2025
Hackathon CiberSeguridad (design thinking)

# Guardar Cambios en ramas y repositorio

Traer los Cambios a la rama que estes trabajando
```shell
git pull origin pruebas --rebase
```

comando de guardado de cambios
```shell
git add .
git commit -m "Descripción de los cambios"
```

Actualizar cambios solamente en tu rama propia
```shell
git push -u origin nombre_de_rama
```

# configurar proyecto
## Creacion del virtual environment

```
python -m venv venv
```

## activar y desactivar el virtual environment 

### Activar
```shell
source venv/bin/activate
```

### Desactivar

```shell
deactivate
```

# Instalar las librerias 
## Si ya creaste el archivo instala el requirements.txt

```shell
pip install -r requirements.txt
```

## Actualizar Pip

```shell
pip install --upgrade pip
```

## Actualizar versiones de librerias y paquetes instalables
```shell
sudo apt-get update
```

## Para este proyecto se usaran las librerias de [WEBPY](https://webpy.org/)

```shell
pip install web.py
```

## Para conexión a la base de datos de [supabase](https://supabase.com/)

```shell
pip install supabase
```

# Crear archivos para la ejecución
## Crear el archivo .env (necesario para la conexión a la abse de datos)

```
SUPABASE_URL="URL_DE_TU_BD"
SUPABASE_KEY="KEY_DE_TU_BD"
```

## Crear el archivo requirements.txt
```shell
pip freeze > requirements.txt
```

## Crear el archivo runtime.txt

```shell
python -V > runtime.txt
```

## ver carateristicas del sistema operativo

```shell
neofetch
```

## Crear el archivo os.txt

```shell
uname -a > os.txt
```

## Crear el archivo .gitignore

```
_pycache_/
*.pyc
smm/
venv/
```

# Iniciar la ejecucion del proyecto 

```shell
uvicorn app:app --reload
```

# NOTAS:

## Si un archivo el cual quieres ignorar ya fue agregado al repositorio, debes eliminarlo del seguimiento de Git con los siguientes comandos:

```shell
git rm --cached <archivo ignorado>
git commit -m "Ignorar archivo <archivo ignorado>"
git push origin <tu_rama>
```

# si tiene cambios desatados ocupa este comando y 

```shell
git reset --hard
```

## si el navegador no hace cambios

`Presiona Ctrl + Shift + R (Windows/Linux) o Cmd + Shift + R (Mac).`

## eliminar pycache y archivo temporales de python

```shell
find . -name "__pycache__" -type d -exec rm -r {} +
find . -name "*.pyc" -delete
```

## 📧 Contacto
Para cualquier duda o sugerencia, puedes contactar a [leyendary2024@gmail.com].
