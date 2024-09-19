from flask import Flask, request, jsonify
import requests
import json
import os

# Cargar la configuración desde config.json
config_path = os.path.join(os.path.dirname(__file__), 'config.json')
with open(config_path, 'r') as config_file:
    config = json.load(config_file)

OLLAMA_URL = config.get('ollama_url')
API_ENDPOINT = config.get('api_endpoint')
FLASK_HOST = config.get('flask_host', '127.0.0.1')
FLASK_PORT = config.get('flask_port', 5000)

# Configuración interna del modelo
model_config = config.get('model_config', {})

app = Flask(__name__)

@app.route('/consultar', methods=['POST'])
def consultar():
    try:
        # Obtener datos del POST
        data = request.json
        consulta = data.get('consulta', '')

        if not consulta:
            return jsonify({"error": "Consulta no proporcionada"}), 400

        # Crear el cuerpo de la solicitud basado en los parámetros del modelo y la consulta
        request_body = model_config.copy()
        request_body['prompt'] = consulta

        # Hacer la solicitud a Ollama
        response = requests.post(
            f"{OLLAMA_URL}{API_ENDPOINT}",
            json=request_body,
            headers={"Content-Type": "application/json"}
        )

        # Comprobar si la solicitud fue exitosa
        if response.status_code == 200:
            ollama_response = response.json()
            return jsonify({"response": ollama_response.get('response', '')})
        else:
            return jsonify({
                "error": "Error en la consulta a Ollama",
                "details": response.text
            }), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host=FLASK_HOST, port=FLASK_PORT)
