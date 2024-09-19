# Ollama Flask Bot

Este proyecto es un bot basado en Flask que se comunica con una instancia local de Ollama para generar respuestas a consultas. El bot recibe consultas a través de solicitudes POST y devuelve la respuesta generada por Ollama.

## Requisitos

- Python 3.x
- Flask
- Requests

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/ollama-flask-bot.git
   cd ollama-flask-bot
   ```

2. **Crea un entorno virtual (opcional pero recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configura los parámetros en `config.json`:**

   Asegúrate de que los valores en `config.json` sean correctos antes de ejecutar el bot. Aquí está la configuración final:

   ```json
   {
     "ollama_url": "http://127.0.0.1:11434",
     "api_endpoint": "/api/generate",
     "flask_host": "0.0.0.0",
     "flask_port": 5000,
     "model_config": {
       "model": "gemma2:2b",
       "stream": false,
       "temp": 0.3,
       "seed": -1,
       "role": "assistant"
     }
   }
   ```

## Ejecución

1. **Ejecuta la aplicación Flask:**

   ```bash
   python src/bot.py
   ```

   Esto iniciará el servidor Flask en `http://0.0.0.0:5000`, que estará listo para recibir solicitudes POST en la ruta `/consultar`.

2. **Hacer una solicitud POST:**

   Puedes utilizar Postman, `curl` u otro cliente HTTP para hacer una solicitud POST al bot. Aquí tienes un ejemplo utilizando `curl`:

   ```bash
   curl -X POST http://localhost:5000/consultar -H "Content-Type: application/json" -d '{"consulta": "hola, buenos dias"}'
   ```

   La respuesta será algo similar a:

   ```json
   {
     "response": "¡Hola! ¡Buenos días a ti también! 😊  ¿Cómo estás?"
   }
   ```

## Estructura del Proyecto

```
📦src
 ┣ 📜bot.py           # Código principal de la aplicación Flask
 ┗ 📜config.json      # Configuración del bot y la conexión a Ollama
```

## Personalización

- **Configuración del Modelo**: Puedes ajustar los parámetros del modelo en el archivo `config.json` bajo la clave `"model_config"`.
- **Endpoint y URL de Ollama**: Asegúrate de que la URL de Ollama y el endpoint estén correctamente configurados en el archivo `config.json`.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema
