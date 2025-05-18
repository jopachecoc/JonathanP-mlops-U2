import requests
import time
import pytest  
import os
from bs4 import BeautifulSoup

BASE_URL = "http://127.0.0.1:5000"

# Datos de prueba

casos_prueba = [
    {"Presion_sistolica": 110, "Presion_diastolica": 70, "Pulso": 80, "Temperatura": 36.5},
    {"Presion_sistolica": 25, "Presion_diastolica": 70, "Pulso": 80, "Temperatura": 37.5},
    {"Presion_sistolica": 120, "Presion_diastolica": 70, "Pulso": 120, "Temperatura": 36.1},
    {"Presion_sistolica": 130, "Presion_diastolica": 70, "Pulso": 120, "Temperatura": 38.8},
    {"Presion_sistolica": 140, "Presion_diastolica": 70, "Pulso": 120, "Temperatura": 37.1},
    {"Presion_sistolica": 150, "Presion_diastolica": 70, "Pulso": 120, "Temperatura": 36.8},
    {"Presion_sistolica": 160, "Presion_diastolica": 70, "Pulso": 120, "Temperatura": 38.2},
    {"Presion_sistolica": 170, "Presion_diastolica": 70, "Pulso": 120, "Temperatura": 39},
    {"Presion_sistolica": 200, "Presion_diastolica": 70, "Pulso": 120, "Temperatura": 38},
    {"Presion_sistolica": 95, "Presion_diastolica": 70, "Pulso": 120, "Temperatura": 37},
    {"Presion_sistolica": 99, "Presion_diastolica": 70, "Pulso": 120, "Temperatura": 36.1},
    {"Presion_sistolica": 38, "Presion_diastolica": 70, "Pulso": 120, "Temperatura": 36.7},
    {"Presion_sistolica": 52, "Presion_diastolica": 70, "Pulso": 120, "Temperatura": 36.9},
    {"Presion_sistolica": 196, "Presion_diastolica": 70, "Pulso": 120, "Temperatura": 36.2},
    {"Presion_sistolica": 900, "Presion_diastolica": 70, "Pulso": 120, "Temperatura": 36.2},
]

def test_diagnostico_y_reporte():
    # Paso 1: Limpiar archivo CSV si existe 
    if os.path.exists("resultados_diagnostico.csv"):
        os.remove("resultados_diagnostico.csv")

    # Paso 2: Enviar los diagnósticos
    for caso in casos_prueba:
        response = requests.post(
            f"{BASE_URL}/diagnostico",
            data=caso
        )
        assert response.status_code == 200
        time.sleep(0.5)  # Evitar que los timestamps se dupliquen

    # Paso 3: Solicitar reporte
    reporte = requests.get(f"{BASE_URL}/reporte")
    assert reporte.status_code == 200
    html = reporte.text
    print(html)

    # Paso 3: Parsear el HTML para encontrar la tabla
    soup = BeautifulSoup(html, "html.parser")
    #tabla = soup.find("table")
    # esta la cambie por las dos que se tenian
    tablas = soup.find_all("table")
    tabla = tablas[0]
    filas = tabla.find_all("tr")

    # Paso 4: Obtener la última fila (exceptuando la fila de encabezado)
    ultima_fila = filas[-1]  # última fila <tr>
    columnas = ultima_fila.find_all("td")



    # Paso 5: El campo "Resultado" es el último de la fila
    resultado = columnas[-1].text.strip()

    # Paso 6: Verificar que sea "ENFERMEDAD TERMINAL"
    assert resultado == "ENFERMEDAD TERMINAL", f"Se esperaba 'ENFERMEDAD TERMINAL' pero se obtuvo '{resultado}'"
#    assert resultado == "ENFERMEDAD TERMINAL"

