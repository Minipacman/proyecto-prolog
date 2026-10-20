# Imagen base ligera de Linux con Python
FROM python:3.10-slim

# Instalar SWI-Prolog en el sistema operativo del contenedor
RUN apt-get update && apt-get install -y \
    swi-prolog \
    && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY app.py /app/
COPY proyecto.pl /app/

# Instalar Flask
RUN pip install --no-cache-dir flask

# Exponer el puerto de Flask
EXPOSE 5000

# Comando para arrancar el servidor web
CMD ["python", "app.py"]