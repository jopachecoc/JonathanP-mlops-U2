# Dockerfile
FROM python:3.10-slim

# Instala dependencias del sistema necesarias para compilar algunos paquetes de Python
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala dependencias de Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copia el código fuente
COPY . .

## Expone el puerto donde correrá Flask (por defecto 5000)
EXPOSE 5000

# Comando por defecto
CMD ["python", "main.py"]




## Usa una imagen base de Python
#FROM python:3.13.3-slim
#
## Establece el directorio de trabajo dentro del contenedor
#WORKDIR /app
#
## Copia los archivos necesarios al contenedor
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt
#
#COPY . .
#
## Expone el puerto donde correrá Flask (por defecto 5000)
#EXPOSE 5000
#
## Comando para ejecutar la app
#CMD ["python", "main.py"]