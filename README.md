# Curso-Programacion-Orientado-Objetos-UNEMI
curso de Programación orientado a Objetos con Python


## Utilizar entorno virtual venv (SOLO LA PRIMERA VEZ)

        1. python -m venv venv
        2. source venv/Scripts/activate
        3. python -m pip install --upgrade pip
        4. pip install -r requirements.txt

### Para instalar una libreria dentro de entorno virtual venv
        pip install <libreria>

### Para crear una nueva aplicacion Django dentro de entorno virtual venv
        python manage.py startapp <nombre_app>

A partir de ahora asegurate de estar dentro del entorno virtual (venv):

        source venv/Scripts/activate

## Levantar servicio Django dentro de entorno virtual venv
        1. python manage.py runserver 0.0.0.0:8000
        Abrir navegador: http://localhost:8000/
