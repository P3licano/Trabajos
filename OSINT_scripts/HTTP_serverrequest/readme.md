
## Descripción

Este script levanta un **servidor HTTP propio** en Python que captura las cabeceras de cada petición entrante, registrando especialmente la cabecera **`User-Agent`** en un archivo local `user_agents.log`.

Se puede usar para prácticas de **OSINT local**, pruebas de **seguridad de cabeceras** y registro de agentes de clientes en entornos controlados.

---

## Funcionalidades

- Escucha peticiones HTTP en un puerto configurable (por defecto `8000`).
    
- Captura información de cada petición:
    
    - Dirección IP del cliente
        
    - Método HTTP (`GET`, `POST`, etc.)
        
    - Path solicitado
        
    - Cabecera `User-Agent`
        
    - Todas las cabeceras recibidas
        
    - Tamaño del cuerpo de la petición
        
    - Timestamp UTC de la recepción
        
- Guarda cada petición como **una línea JSON** en `user_agents.log`.
    
- Responde con un mensaje simple `OK` al cliente.
    
- Multihilo: puede atender varias conexiones simultáneamente usando `ThreadingHTTPServer`.
    

---

## Requisitos

- Python 3.7 o superior.
    
- Librerías estándar de Python (`http.server`, `json`, `datetime`, `argparse`, `socket`).
    
- No requiere dependencias externas.
    

---

## Uso

1. Guardar el script como `ua_collector.py`.
    
2. Ejecutar:

```python
python3 ua_collector.py
```

3. Probar desde otro terminal o máquina:

```bash
curl -A "MiUserAgent/1.0" http://127.0.0.1:8000/
```

4. Revisar los logs:

```bash
cat user_agents.log
# o formateado
tail -n 10 user_agents.log | jq .
```

## Estructura del log (`user_agents.log`)

Debería verse de la siguiente manera

```json
{
  "timestamp_utc":"2025-10-15T20:00:00Z",
  "client_ip":"127.0.0.1",
  "method":"GET",
  "path":"/",
  "user_agent":"MiUserAgent/1.0",
  "headers":{
    "Host":"127.0.0.1:8000",
    "User-Agent":"MiUserAgent/1.0",
    "Accept":"*/*",
    "Connection":"keep-alive"
  },
  "body_size":0
}
```
