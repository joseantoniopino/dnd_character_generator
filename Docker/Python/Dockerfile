FROM python:bullseye

# Actualizar sistema y instalar dependencias
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

# Crear un directorio para nuestra aplicación
RUN mkdir /app
WORKDIR /app

# Copiar los archivos necesarios para nuestra aplicación
COPY ./requirements.txt /app

# Instalar las dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el resto de los archivos de nuestra aplicación
COPY . /app

# Exponer el puerto en el cual nuestra aplicación escuchará
EXPOSE 8000

# Ejecutar nuestra aplicación al iniciar el contenedor
CMD ["tail", "-f", "/dev/null"]