Realizado por Jonathan Pacheco

# Predicción de Enfermedades

Descripción: Proyecto que muestra una aplicación mediante el uso de Flask para predecir el estado de un paciente haciendo como uso el pulso, temperatura, frecuencia cardiaca y como salida arroja las siguientes clasificaciones.

- NO ENFERMO
- ENFERMEDAD LEVE
- ENFERMEDAD AGUDA
- ENFERMEDAD CRÓNICA


## Prerrequisitos para poder ejecutar la aplicación

* Tener Docker instalado en su computadora
* Tener VScode u otro IDE para ejecutar código python.


# Archivos adjuntos

* diagnosticos.py 						Funcion que realiza el proceso de clasificación del tipo de enfermedad 
* main.py								Funcion de codigo fuente primaria 
* requeriments.txt						Requerimientos para que main pueda ser correctamente
* Dockerfile							Archivo para crear la imagen
* README.md								Descripción reproducir el proceso.


## pasos para la construcción de la imagen docker

### 1. Colocar todos los archivos en la misma carpeta (archivos mensionados anteriormente)

* diagnosticos.py 
* main.py
* requeriments.txt
* Dockerfile
* README.md

### 2. Construir la imagen con Docker

Ejecutar el siguiente comando en la terminal. (previo a esto ubicarse en la localización de la carpeta de archivos creada anteriormente)

```docker build -t primera_app1.```  (colocar el punto)

### 3. Ejecutar la imagen

```docker run -p primera_app1```

levantara la imagen el el puerto 5000

### 4. abrir en la siguiente ruta del navegador para ver la imagen 

http://127.0.0.1:5000/diagnostico

### 5. Obtener las métricas, diligencias los datos de:
Diligenciar cada uno de los campos en la aplicacion, por ejemplo:

presión sistólica : 85
Presión diastólica: 100
Pulso: 65
Temperatura:36

Click en “evaluar diagnóstico“.

Luego verás el resultado de la clasificación del paciente

