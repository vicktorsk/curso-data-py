# Iniciar el contenedor. Desde tu terminal, navega al directorio donde tienes tu docker-compose.yml

docker-compose up -d
docker-compose up -d --build

El flag -d inicia el contenedor en modo "detached" (desacoplado), lo que significa que el contenedor se ejecuta en segundo plano.

# Acceder al contenedor. Una vez que el contenedor esté en ejecución, puedes acceder a su terminal



Este comando abrirá una sesión de bash dentro del contenedor, donde podrás ejecutar comandos de Python o instalar paquetes adicionales como lo harías en cualquier terminal de Linux.


===
Comandos Docker
===

-- Listar contenedores
docker ps

-- Reconstruir un sólo service
docker-compose build jupyter-notebook

-- Levantar y construir contenedores
docker-compose up -d --build

-- Levantar contenedores
docker-compose up -d

-- Acceder al contenedor
docker exec -it python_env /bin/bash
docker exec -it flask_app /bin/bash
docker exec -it fastapi_app /bin/bash
docker exec -it jupyter_notebook /bin/bash

-- Instalar paquetes (dentro del contenedor)
pip install pandas plotly

-- Ejecutar script de python (dentro del contenedor)
python data_analysis.py

-- Levantar fastApi
uvicorn app:app --host 0.0.0.0 --reload

-- Levantar jupyter
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
cvkljh xmnkcjalsdjsñdjasdljdlksdjalskdjasldjasldkajs








# Instalar Paquetes. Dentro del contenedor, si necesitas instalar algún paquete, puedes hacerlo con pip.

pip install pandas plotly

# Ejecutar el script de Python. Navega al directorio /app (que está vinculado a tu directorio local /proyecto-visualizacion/ gracias al volumen configurado en docker-compose.yml)

python data_analysis.py
