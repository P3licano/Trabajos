

Repositorio de ejemplo para **capturar el User-Agent, IP y cabeceras básicas** de visitantes **únicamente si dan su consentimiento**.

---

## Contenido

- `app.py` - Aplicación Flask que muestra una página con botón de consentimiento y un endpoint `/log` que escribe registros en `visitors.jsonl`.
    
- `visitors.jsonl` - Archivo de salida (se crea automáticamente la primera vez que se registra una visita). Cada línea es un objeto JSON.
    

---

## Características

- Registro **solo con consentimiento explícito** (botón en la página).
    
- Guarda: `timestamp` (UTC), `ip`, `user_agent`, `accept`, `referer` y `host`.
    
- Formato de salida `JSONL` (una entrada JSON por línea) para facilitar procesado.
    
- Diseñado para pruebas locales y fines educativos.
    

---

## Requisitos

- Python 3.8+
    
- `pip`
    
- (Opcional) `ngrok` para exponer localmente el servidor a Internet de forma segura para pruebas.
    

---

## Instalación y ejecución

1. Clona o descarga este repositorio y sitúate en la carpeta del proyecto.
    
2. Crea y activa un entorno virtual (recomendado):
    

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. Instala dependencias:
    

```bash
pip install flask
```

4. Ejecuta la aplicación:
    

```bash
python app.py
```

La app se ejecutará en `http://0.0.0.0:5000` (puedes abrir `http://127.0.0.1:5000` en tu navegador).

---

## Uso con ngrok (opcional)

1. Descarga e inicia `ngrok` desde su página oficial.
    
2. En una terminal, expón el puerto 5000:
    

```bash
./ngrok http 5000
```

3. Ngrok te dará una URL pública (`https://xxxxxx.ngrok.io`). Abre esa URL en un navegador para ver la página de consentimiento.


---

## Formato de los registros

Cada línea de `visitors.jsonl` contiene un JSON similar a:

```json
{
  "timestamp": "2025-10-15T12:34:56.789012+00:00",
  "ip": "203.0.113.42",
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "referer": "",
  "host": "abcd-1234.ngrok.io"
}
```
