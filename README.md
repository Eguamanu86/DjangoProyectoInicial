# Curso-Programacion-Orientado-Objetos-UNEMI
curso de Programación orientado a Objetos con Python


## Utilizar entorno virtual venv (SOLO LA PRIMERA VEZ)

        1. python -m venv venv
        2. source venv/Scripts/activate
        3. python -m pip install --upgrade pip
        4. pip install -r requirements.txt

A partir de ahora asegurate de estar dentro del entorno virtual (venv):

        source venv/Scripts/activate

## Levantar servicio Django dentro de entorno virtual venv
        1. python manage.py runserver 0.0.0.0:8001
        Abrir navegador: http://localhost:8001/
