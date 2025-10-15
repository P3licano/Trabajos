from http.server import BaseHTTPRequestHandler, HTTPServer

LOGFILE = "user_agents.log"

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Capturar User-Agent de la petición
        ua = self.headers.get("User-Agent")
        with open(LOGFILE, "a") as f:
            f.write(f"{self.client_address[0]} - {ua}\n")
        
        # Responder al cliente
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK\n")

# Levantar servidor en localhost:8000
server = HTTPServer(("0.0.0.0", 8000), MyHandler)
print("Servidor escuchando en http://0.0.0.0:8000")
server.serve_forever()