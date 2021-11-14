# apiproductos_django
Comandos a ejecutar

py -m venv env "Crea el entorno virtual"

./env/Scripts/activate "activa en env"

pip install -r requirements.txt "instala todo los requerimientos para el proyecto"

pip install --upgrade pip "actualizar pip"

# Desde ese punto recordar esar parado en la carpeta que contiene el manage.py

python manage.py makemigrations api "crea la migracion en caso de no tenerlas, recuerde tener la bd creada en postgreSQL"

python manage.py migrations "crea la migracion y las bd en postgreSQL"

python manage.py runserver "inicia la api"
