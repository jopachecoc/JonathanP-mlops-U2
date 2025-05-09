# Usa una imagen base de Python
FROM python:3.13.3-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expone el puerto donde correrá Flask (por defecto 5000)
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "main.py"]