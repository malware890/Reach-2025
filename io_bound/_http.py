import socket
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

def run_http():
    HOST = socket.gethostbyname(socket.gethostname())
    print(HOST)
    #HOST = "192.168.12.141"
    PORT = 8000

    server = HTTPServer((HOST, PORT), NeuralHTTP)
    print("Server now running...")
    server.serve_forever()
    server.server_close()
    print("Server stopped.")

#HTTP handling
class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Hello World!</h1></body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))

run_http()
