FROM python:3.9-slim

WORKDIR /app

# 1. Copiamos el archivo de requisitos primero
COPY requirements.txt .

# 2. Instalamos las librerías (requests, beautifulsoup, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copiamos el código de la aplicación
COPY ./app ./app

# 4. Ejecutamos (Agregamos -u para ver los logs en tiempo real sin buffer)
CMD ["python", "-u", "app/main.py"]