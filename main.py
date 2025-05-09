from flask import Flask, jsonify, request, render_template_string
import diagnosticos 
from diagnosticos import enfermedad1

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
        except ValueError:
            resultado = "Error en la entrada"
    
    return render_template_string(html_form_diagnostico, resultado=resultado)


# Asegúrate de usar host='0.0.0.0'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#if __name__ == "__main__":
#    app.run(debug=True)

