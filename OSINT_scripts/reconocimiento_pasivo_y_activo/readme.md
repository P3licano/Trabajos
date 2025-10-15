
## ¿Qué hace este programa?

Es un script interactivo enfocado a OSINT (pasivo y activo).
Pregunta al usuario por el dominio/URL objetivo y ejecuta los módulos:

 - **whois**
 
 - **crt.sh**
 
 - **Wayback CDX**
 
 - **sugerencias de Google Dorks (no automatizadas)**
 
 - **probe HTTP (cabeceras, título)**
 
 - **extracción de cabeceras de seguridad**
 
 - **Wappalyzer (opcional si está instalado)**
 
Guarda resultados en tu directorio con el nombre de "recon_nom_dominio.json"


## ¿Cómo se usa?

1. Guarda como `interactive_recon.py`.

 2. Ejecuta: `python interactive_recon.py`

3. Introduce el dominio o la URL cuando te lo pida (ej. `example.com` o `https://example.com`).

4.  Confirma con `s` para ejecutar el OSINT.

5. Se generará un archivo `recon_<dominio>_YYYYMMDDTHHMMSSZ.json` con todos los resultados.


## Puntos a tener en cuenta y limitaciones

- El script **no** automatiza Google Dorking (solo sugiere dorks para uso manual) — evitarás bloqueos y cumplimiento de TOS.

- Para Shodan, FOFA u otras fuentes que requieren API keys puedes implementar al script pasando las claves por variables de entorno o argumentos CLI.
