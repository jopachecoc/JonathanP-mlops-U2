# Construcción de la Aplicación Web e Imagen Docker

## Desarrollo de la Solución

### 1. Función de Clasificación Médica
Se construyó la función en Python que contiene las reglas para clasificar enfermedades según:
- Pulso cardíaco
- Presión arterial
- Temperatura corporal

El código se almacenó en el archivo:  
📄 `diagnostico.py`

### 2. Aplicación Web con Flask
Se desarrolló la interfaz web usando Flask que:
- Importa la función del archivo `diagnostico.py`
- Expone un endpoint REST para diagnósticos
- El código principal se almacena en:  
📄 `main.py`

### 3. Gestión de Dependencias
Se creó el archivo:  
📄 `requirements.txt`  
Conteniendo todas las dependencias necesarias:
```
text
flask==2.3.2
numpy==1.24.3
```

# Pasos a tener en cuenta para la ejecucion de la imagen
Para la ejecucion de este tener en cuenta:

# 1 comando para cargar la imagen.
```
docker load -i imagen.tar
```
#2 comando para ejecutar la imagen
```
docker run --rm diagnostico_imagen
```
#3 ispecionar el front 
Si desea inspeccionar el endpoint de prediccion dirigirse 
```
localhost:5000/diagnostico
```
