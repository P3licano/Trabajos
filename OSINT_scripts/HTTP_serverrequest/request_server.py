import requests

url = "http://127.0.0.1:8000"  # tu servidor propio
headers = {"User-Agent": "MiCliente/1.0"}
r = requests.get(url, headers=headers)

print("Status:", r.status_code)
print("Cabeceras recibidas del servidor:", r.headers)
