from flask import Flask, jsonify, request, render_template_string
import diagnosticos 
from diagnosticos import enfermedad1
from datetime import datetime
import csv
import os
import pandas as pd

app = Flask(__name__)

# HTML para el formulario
html_form = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Triage</title>
    <!-- Bootstrap CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f0f8ff;
            font-family: 'Segoe UI', sans-serif;
        }
        .container {
            margin-top: 50px;
            max-width: 600px;
            background-color: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        }
        .form-label {
            font-weight: bold;
        }
        .title {
            text-align: center;
            margin-bottom: 30px;
            color: #2b7a78;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2 class="title">Formulario de Triage</h2>
        <form method="POST">
            <div class="mb-3">
                <label class="form-label">Presión Sistólica</label>
                <input type="number" name="Presion_sistolica" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Presión Diastólica</label>
                <input type="number" name="Presion_diastolica" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Pulso</label>
                <input type="number" name="Pulso" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Temperatura</label>
                <input type="number" name="Temperatura" class="form-control" step="0.1" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Edad</label>
                <input type="number" name="edad" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Número de Hijos</label>
                <input type="number" name="hijos" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Número de Responsables</label>
                <input type="number" name="responsables" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary w-100">Calcular Suma</button>
        </form>

        {% if suma is not none %}
            <div class="alert alert-info text-center mt-4">
                <strong>Resultado de la suma:</strong> {{ suma }}
            </div>
        {% endif %}
    </div>
</body>
</html>
"""


html_form_diagnostico = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Diagnóstico - Triage</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #e8f5e9;
            font-family: 'Segoe UI', sans-serif;
        }
        .container {
            margin-top: 50px;
            max-width: 600px;
            background-color: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        }
        .title {
            text-align: center;
            margin-bottom: 30px;
            color: #388e3c;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2 class="title">Diagnóstico de Triage</h2>
        <form method="POST">
            <div class="mb-3">
                <label class="form-label">Presión Sistólica</label>
                <input type="number" name="Presion_sistolica" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Presión Diastólica</label>
                <input type="number" name="Presion_diastolica" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Pulso</label>
                <input type="number" name="Pulso" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Temperatura</label>
                <input type="number" name="Temperatura" class="form-control" step="0.1" required>
            </div>
            <button type="submit" class="btn btn-success w-100">Evaluar Diagnóstico</button>
        </form>

        {% if resultado %}
            <div class="alert alert-info text-center mt-4">
                <strong>Resultado:</strong> {{ resultado }}
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/")
def root():
    return "jona"

@app.route("/users/<user_id>")
def get_user(user_id):
    user = {"id": user_id, "name": "test", "telefono": "999-666-333"}
    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    data["status"] = "user created"
    return jsonify(data), 201

# Nueva ruta para mostrar formulario y calcular la suma
@app.route("/sumar", methods=["GET", "POST"])
def sumar():
    suma = None
    if request.method == "POST":
        try:
            edad = int(request.form["edad"])
            hijos = int(request.form["hijos"])
            responsables = int(request.form["responsables"])
            suma = edad + hijos + responsables
        except ValueError:
            suma = "Error en la entrada"
    return render_template_string(html_form, suma=suma)



@app.route("/diagnostico", methods=["GET", "POST"])
def diagnostico():
    resultado = None
    if request.method == "POST":
        try:
            ps = float(request.form["Presion_sistolica"])
            pd = float(request.form["Presion_diastolica"])
            pulso = float(request.form["Pulso"])
            temp = float(request.form["Temperatura"])

            resultado = enfermedad1(ps, pd, pulso, temp)

            # Obtener la fecha y hora actuales
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Definir el nombre del archivo CSV
            csv_file = 'resultados_diagnostico.csv'

            # Verificar si el archivo existe para escribir encabezados si es necesario
            file_exists = os.path.isfile(csv_file)

            # Escribir los datos en el archivo CSV
            with open(csv_file, mode='a', newline='', encoding='utf-8') as archivo:
                writer = csv.writer(archivo)
                if not file_exists:
                    # Escribir encabezados si el archivo es nuevo
                    writer.writerow(['Fecha y Hora', 'Presión Sistólica', 'Presión Diastólica', 'Pulso', 'Temperatura', 'Resultado'])
                writer.writerow([timestamp, ps, pd, pulso, temp, resultado])

        except ValueError:
            resultado = "Error en la entrada"
    
    return render_template_string(html_form_diagnostico, resultado=resultado)


@app.route("/reporte")
def reporte():
    try:
        # Leer el archivo CSV
        df = pd.read_csv("resultados_diagnostico.csv")

        # numero total de predicciones por categoria
        conteo_categorias = df['Resultado'].value_counts().to_dict()
        # Obtener los últimos 5 registros realizados
        ultimos_registros = df.tail(5).to_dict(orient='records') # por la manera en que se construye la data siempre los ultimos registros seran los ultimos registrados.
        #Fecha de la última predicción.
        fecha_ultima  = df['Fecha y Hora'].max()

        # Renderizar la plantilla con los datos
        return render_template_string(html_template,
                                      conteo_categorias=conteo_categorias,
                                      ultimos_registros=ultimos_registros,
                                      fecha_ultima=fecha_ultima)

    except FileNotFoundError:
        return "El archivo 'resultados_diagnostico.csv' no se encontró."
    except Exception as e:
        return f"Ocurrió un error al procesar el archivo CSV: {e}"


#Palntilla HTML para mostrar los resultados
html_template = '''
<!doctype html>
<html>
<head>
    <title>Estadísticas de Diagnósticos</title>
    <style>
        body {
            background-color: #ffffff;
            color: #2e7d32;
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        h1, h2 {
            color: #1b5e20;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #a5d6a7;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #81c784;
            color: #ffffff;
        }
        tr:nth-child(even) {
            background-color: #e8f5e9;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background-color: #c8e6c9;
            margin: 5px 0;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Estadísticas de Diagnósticos</h1>
    <h2>Número total de predicciones por categoría:</h2>
    <ul>
        {% for categoria, conteo in conteo_categorias.items() %}
            <li><strong>{{ categoria }}:</strong> {{ conteo }}</li>
        {% endfor %}
    </ul>
    <h2>Últimas 5 predicciones realizadas:</h2>
    <table>
        <tr>
            {% for columna in ultimos_registros[0].keys() %}
                <th>{{ columna }}</th>
            {% endfor %}
        </tr>
        {% for registro in ultimos_registros %}
            <tr>
                {% for valor in registro.values() %}
                    <td>{{ valor }}</td>
                {% endfor %}
            </tr>
        {% endfor %}
    </table>
    <h2>Fecha de la última predicción:</h2>
    <p>{{ fecha_ultima }}</p>
</body>
</html>
'''

# Asegúrate de usar host='0.0.0.0'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#if __name__ == "__main__":
#    app.run(debug=True)

