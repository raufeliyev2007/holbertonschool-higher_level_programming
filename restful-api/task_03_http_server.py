#!/usr/bin/python3
"""
A simple HTTP server built using the http.server module.
Handles GET requests for specific endpoints and returns JSON or plain text.
"""
import http.server
import socketserver
import json

# Определяем порт
PORT = 8000

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    HTTP Request Handler to manage different API endpoints.
    """

    def do_GET(self):
        """
        Handles GET requests based on the URL path.
        """
        # Эндпоинт: Корень (/)
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Эндпоинт: /data (Возвращает JSON)
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # Эндпоинт: /status
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        # Эндпоинт: /info (Дополнительно из задания)
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode('utf-8'))

        # Обработка несуществующих эндпоинтов (404)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found")

def run_server():
    """
    Starts the HTTP server on the defined port.
    """
    # Позволяет повторно использовать порт сразу после закрытия сервера
    socketserver.TCPServer.allow_reuse_address = True

    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Serving at port {PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down the server.")
            httpd.server_close()

if __name__ == "__main__":
    run_server()
