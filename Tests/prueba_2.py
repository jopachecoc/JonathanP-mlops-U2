import requests
import pytest  

def test_diagnostico_enfermedad_leve():
    url = "http://localhost:5000/diagnostico"
    
    # Datos de entrada esperados para "ENFERMEDAD LEVE"
    data = {
        "Presion_sistolica": 110,
        "Presion_diastolica": 70,
        "Pulso": 80,

        "Temperatura": 38.0
    }

    # Enviamos la solicitud POST
    response = requests.post(url, data=data)

    assert response.status_code == 200
    assert "ENFERMEDAD LEVE" in response.text
