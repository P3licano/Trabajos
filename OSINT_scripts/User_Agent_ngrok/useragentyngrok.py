#!/usr/bin/env python3
# app.py
from flask import Flask, request, render_template_string, jsonify
from datetime import datetime, timezone
import json
import os

app = Flask(__name__)

DATA_FILE = "visitors.jsonl"  # cada línea es un JSON

CONSENT_PAGE = """
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>Prueba de captura (con consentimiento)</title>
  <style>
    body{font-family:system-ui,-apple-system,Segoe UI,Roboto,"Helvetica Neue",Arial;margin:2rem}
    .card{border:1px solid #ddd;padding:1.2rem;border-radius:8px;max-width:720px}
    button{padding:.6rem 1rem;border-radius:6px;border:0;cursor:pointer}
  </style>
</head>
<body>
  <div class="card">
    <h1>Prueba de captura de User-Agent</h1>
    <p>Este servidor captura <strong>solo</strong> el <em>User-Agent</em>, IP y algunas cabeceras
       <strong>si y solo si</strong> aceptas. Esta prueba es para uso educativo/testing en tu propio servidor.</p>
    <p>Al pulsar <strong>Aceptar</strong> consientes que el navegador envíe esta información al servidor.</p>
    <button id="accept">Aceptar y registrar</button>
    <button id="decline">No, gracias</button>
    <p id="status"></p>
  </div>

  <script>
    document.getElementById('accept').addEventListener('click', async () => {
      const res = await fetch('/log', { method: 'POST', headers: { 'Content-Type': 'application/json' }});
      const json = await res.json();
      document.getElementById('status').textContent = json.message || 'Hecho';
    });
    document.getElementById('decline').addEventListener('click', () => {
      document.getElementById('status').textContent = 'No se registró nada. Gracias.';
    });
  </script>
</body>
</html>
"""

def safe_append_jsonl(obj, path=DATA_FILE):
    # Crear directorio si hace falta
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    line = json.dumps(obj, ensure_ascii=False)
    # Apertura en modo append (no locking cross-platform aquí; suficiente para pruebas locales)
    with open(path, "a", encoding="utf-8") as f:
        f.write(line + "\n")

@app.route("/", methods=["GET"])
def index():
    # Muestra la página de consentimiento; NO se registra nada hasta que el usuario haga POST a /log
    return render_template_string(CONSENT_PAGE)

@app.route("/log", methods=["POST"])
def log_visit():
    # Aquí se captura la info: se usa solo con consentimiento explícito (botón)
    ua = request.headers.get("User-Agent", "")
    now = datetime.now(timezone.utc).isoformat()
    # IP: request.remote_addr es suficiente para pruebas; con ngrok verás la IP de la conexión a ngrok
    ip = request.remote_addr
    # Algunas cabeceras útiles (no sensibles)
    accept = request.headers.get("Accept")
    referer = request.headers.get("Referer")
    host = request.host

    entry = {
        "timestamp": now,
        "ip": ip,
        "user_agent": ua,
        "accept": accept,
        "referer": referer,
        "host": host
    }

    try:
        safe_append_jsonl(entry)
        return jsonify({"status": "ok", "message": "Información registrada correctamente (solo pruebas)."})
    except Exception as e:
        return jsonify({"status": "error", "message": f"No se pudo guardar: {e}"}), 500

if __name__ == "__main__":
    # Ejecutar en 0.0.0.0 para que ngrok pueda enlazarlo
    app.run(host="0.0.0.0", port=5000, debug=True)