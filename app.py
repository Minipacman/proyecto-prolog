from flask import Flask, render_template_string, request, jsonify
import subprocess

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consulta de materias ESCOM</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
            margin: 0;
            padding: 30px 20px;
        }
        .card {
            max-width: 950px;
            margin: 0 auto;
            background: #1e293b;
            border-radius: 12px;
            padding: 25px 30px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            border: 1px solid #334155;
        }
        h2 {
            color: #38bdf8;
            margin-top: 0;
            font-size: 24px;
            border-bottom: 2px solid #334155;
            padding-bottom: 10px;
        }
        h3 {
            font-size: 16px;
            margin-top: 20px;
            margin-bottom: 10px;
            padding-left: 8px;
        }
        label {
            font-weight: 600;
            display: block;
            margin-bottom: 8px;
            color: #94a3b8;
        }
        input[type="text"] {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #475569;
            background: #0f172a;
            color: #f8fafc;
            border-radius: 8px;
            box-sizing: border-box;
            font-size: 15px;
            margin-bottom: 15px;
            font-family: 'Consolas', 'Courier New', monospace;
        }
        input[type="text"]:focus {
            outline: none;
            border-color: #38bdf8;
        }
        .grid-section {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 10px;
        }
        .example-btn {
            background: #0f172a;
            border: 1px solid #334155;
            color: #cbd5e1;
            padding: 10px;
            border-radius: 6px;
            font-size: 12px;
            cursor: pointer;
            text-align: left;
            transition: all 0.2s;
        }
        .example-btn:hover {
            border-color: #38bdf8;
            color: #38bdf8;
            background: #1e293b;
        }
        .example-btn strong {
            display: block;
            margin-bottom: 3px;
        }
        .badge-regla { color: #f43f5e; border-left: 4px solid #f43f5e; }
        .badge-predicado { color: #10b981; border-left: 4px solid #10b981; }

        button.submit-btn {
            background-color: #0284c7;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
            width: 100%;
            font-weight: bold;
            transition: background 0.2s;
            margin-top: 10px;
        }
        button.submit-btn:hover {
            background-color: #0369a1;
        }
        .output-box {
            margin-top: 20px;
            background: #020617;
            color: #4ade80;
            padding: 15px;
            border-radius: 8px;
            font-family: 'Consolas', 'Courier New', monospace;
            min-height: 120px;
            max-height: 350px;
            overflow-y: auto;
            white-space: pre-wrap;
            border: 1px solid #1e293b;
        }
    </style>
</head>
<body>
    <div class="card">
        <h2>Consulta de materias ESCOM-IA</h2>
        
        <label>Selecciona una regla o predicado para ejecutarla:</label>

        <!-- SECCIÓN DE REGLAS ACADÉMICAS -->
        <h3 class="badge-regla">⚙️ REGLAS</h3>
        <div class="grid-section" style="grid-template-columns: 1fr; margin-bottom: 10px;">
            <div class="example-btn" onclick="setQuery('consulta(1, Profe, calculo, Turno)')">
                <strong style="color:#f43f5e;">Consulta General</strong>
                <code>consulta(1, Profe, calculo, Turno)</code>
            </div>
        </div>
        <div class="grid-section">
            <div class="example-btn" onclick="setQuery('filtro1_profesor(calculo, P1, P2, matutino)')">
                <strong style="color:#f43f5e;">Filtro por profesor</strong>
                <code>filtro1_profesor(calculo, P1, P2, matutino)</code>
            </div>
            <div class="example-btn" onclick="setQuery('materias_por_semestre(1, M1, M2)')">
                <strong style="color:#f43f5e;">Filtro de materias por semestre</strong>
                <code>materias_por_semestre(1, M1, M2)</code>
            </div>
            <div class="example-btn" onclick="setQuery('materia_ambos_turnos(Materia)')">
                <strong style="color:#f43f5e;"> Materias que se cursan en ambos turnos</strong>
                <code>materia_ambos_turnos(Materia)</code>
            </div>
            <div class="example-btn" onclick="setQuery('materia_seriada_1(M1, S1, M2, S2)')">
                <strong style="color:#f43f5e;">Materias seriadas(1,2)</strong>
                <code>materia_seriada_1(M1, S1, M2, S2)</code>
            </div>
            <div class="example-btn" onclick="setQuery('mismo_semestre(calculo, M2, 1)')">
                <strong style="color:#f43f5e;">Materias que se cursan en el mismo semestre</strong>
                <code>mismo_semestre(calculo, M2, 1)</code>
            </div>
            <div class="example-btn" onclick="setQuery('filtro_turno(1, P1, P2)')">
                <strong style="color:#f43f5e;">Filtro de porfesor por turno </strong>
                <code>filtro_turno(1, P1, P2)</code>
            </div>
        </div>

        <!-- SECCIÓN DE PREDICADOS -->
        <h3 class="badge-predicado">📌 Predicados de Listas y Profesores</h3>
        <div class="grid-section">
            <div class="example-btn" onclick="setQuery('todos_profesores(1, Lista)')">
                <strong style="color:#10b981;">Lista de todos los profesores</strong>
                <code>todos_profesores(1, Lista)</code>
            </div>
<div class="example-btn" onclick="setQuery(&quot;profesor_materias('MARTINEZ PERALES JOSE CRUZ', Lista)&quot;)">
                <strong style="color:#10b981;">Materias que imparte un mismo profesor</strong>
                <code>profesor_materias('MARTINEZ PERALES JOSE CRUZ', Lista)</code>
            </div>
            <div class="example-btn" onclick="setQuery('profesor_ambos_turnos(Profe)')">
                <strong style="color:#10b981;">Porfesor que imparte clases en ambos turnos</strong>
                <code>profesor_ambos_turnos(Profe)</code>
            </div>
            <div class="example-btn" onclick="setQuery('profesor_exclusivo_turno(matutino, Profe)')">
                <strong style="color:#10b981;">Profesor exclusivo de un turno</strong>
                <code>profesor_exclusivo_turno(matutino, Profe)</code>
            </div>
        </div>
        <div class="grid-section" style="grid-template-columns: 1fr;">
            <div class="example-btn" onclick="setQuery('seriacion_avanzada(M1, M2)')">
                <strong style="color:#10b981;">Seriacion avanzada (A,B,C)</strong>
                <code>seriacion_avanzada(M1, M2)</code>
            </div>
        </div>

        <form id="prologForm">
            <label for="query" style="margin-top: 15px;">Consulta activa a Prolog:</label>
            <input type="text" id="query" name="query" value="consulta(1, Profe, calculo, Turno)" required>
            <button type="submit" class="submit-btn">Ejecutar Consulta</button>
        </form>

        <label style="margin-top:20px;">Resultado de SWI-Prolog:</label>
        <div class="output-box" id="result">Esperando consulta...</div>
    </div>

    <script>
        function setQuery(text) {
            document.getElementById('query').value = text;
        }

        document.getElementById('prologForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const query = document.getElementById('query').value;
            const resultDiv = document.getElementById('result');
            resultDiv.innerText = "Consultando a SWI-Prolog...";

            try {
                const response = await fetch('/query', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ query: query })
                });
                const data = await response.json();
                resultDiv.innerText = data.result;
            } catch (err) {
                resultDiv.innerText = "Error de conexión con el servidor.";
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/query', methods=['POST'])
def run_query():
    data = request.get_json()
    user_query = data.get('query', '').strip()

    if user_query.endswith('.'):
        user_query = user_query[:-1]

    prolog_goal = f"forall({user_query}, (writeln({user_query}))), halt."

    cmd = [
        "swipl", "-q",
        "-s", "proyecto.pl",
        "-g", prolog_goal
    ]

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        output = proc.stdout.strip()
        
        if not output:
            if proc.stderr:
                output = f"Error de sintaxis o en Prolog:\n{proc.stderr.strip()}"
            else:
                output = "false. (No se encontraron coincidencias)"

        return jsonify({"result": output})
    except Exception as e:
        return jsonify({"result": f"Error al ejecutar SWI-Prolog: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)