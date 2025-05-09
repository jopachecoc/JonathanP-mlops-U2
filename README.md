# JonathanP-mlops-U2
Proyecto con foco en la predicción de la clasificación de las enfermedades para los pacientes.

# Definicion del problema.

Dados los avances tecnológicos, en el campo de la medicina la cantidad de información que existe de los pacientes es muy abundante. Sin embargo, para algunas enfermedades no tan comunes, llamadas huérfanas, los datos que existen escasean. Se requiere construir un modelo que sea capaz de predecir, dados los datos de síntomas de un paciente, si es posible o no que este sufra de alguna enfermedad. Esto se requiere tanto para enfermedades comunes (muchos datos) como para enfermedades huérfanas (pocos datos).

# Propósito
Desarrollar un modelo de clasificación clínica basado en aprendizaje automático que priorice pacientes según la gravedad de su condición, optimizando la asignación de recursos médicos y reduciendo el tiempo de atención en casos críticos mediante un sistema de triaje automatizado y validado clínicamente.

# Enfoque Técnico

## Algoritmo Propuesto
- **Tipo**: Clasificación supervisada  
- **Inputs**:  
  - Variables clínicas  
  - Signos vitales  
  - Antecedentes médicos  

## Métricas de Performance
- **Precisión objetivo**: ≥X% en identificación de casos graves  

## Procesamiento de Datos
1. Captura de parámetros clínicos  
2. Normalización según protocolos  
3. Clasificación en categorías de urgencia  
4. Generación de alertas prioritarias  

# Estructura del Repositorio

# Estructura del Repositorio

```bash
.
├── 📄 main.py 🐍            # Punto de entrada principal
│   └── 📄 diagnosticos.py🐍 # Módulo de la funcion que me realiza la clasificacion de la enfermeddad (importado)
├── 📄 Dockerfile 🐳         # Configuración para contenedorización
├── 📄 requirements.txt      # Dependencias del proyecto 
├── 📄 README.md             # Documentación esencial
└── 📄 .gitignore            # Archivos excluidos de Git
```



