# import socket
# import time
# import json
# from http.server import HTTPServer, BaseHTTPRequestHandler

# def run_http():
#     HOST = socket.gethostbyname(socket.gethostname())
#     print(HOST)
#     #HOST = "192.168.12.141"
#     PORT = 8000

#     server = HTTPServer((HOST, PORT), HTTP)
#     print("Server now running...")
#     server.serve_forever()
#     server.server_close()
#     print("Server stopped.")

# #HTTP handling
# class HTTP(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header("Content-type", "text/html")
#         self.end_headers()

#         self.wfile.write(bytes("<html><body><h1>Hello World!</h1></body></html>", "utf-8"))

#     def do_POST(self):
#         self.send_response(200)
#         self.send_header("Content-type", "application/json")
#         self.end_headers()

#         date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
#         self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))

#         # Read incoming data
#         content_length = int(self.headers.get("Content-Length", 0))
#         post_data = self.rfile.read(content_length)

#         # Log the data (optional)
#         print(f"Received POST data: {post_data.decode('utf-8')}")

#         # Send a response
#         self.send_response(200)
#         self.send_header("Content-type", "application/json")
#         self.end_headers()

#         response = {"status": "success", "received": post_data.decode("utf-8")}
#         self.wfile.write(bytes(json.dumps(response), "utf-8"))


# run_http()

import socket
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

class HTTP(BaseHTTPRequestHandler):
    request_count = 0  # Track the number of requests
    max_requests = 10000  # Set the maximum number of requests to process

    def do_GET(self):
        HTTP.request_count += 1
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Hello World!</h1></body></html>", "utf-8"))

        self.check_stop_condition()

    def do_POST(self):
        HTTP.request_count += 1
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Read incoming data
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)

        # Log the data (optional)
        print(f"Received POST data: {post_data.decode('utf-8')}")

        # Send a response
        response = {"status": "success", "received": post_data.decode("utf-8")}
        self.wfile.write(bytes(json.dumps(response), "utf-8"))

        self.check_stop_condition()

    def check_stop_condition(self):
        # Stop the server if the max_requests is reached
        if HTTP.request_count >= HTTP.max_requests:
            print("Max requests reached. Shutting down the server.")
            threading.Thread(target=self.server.shutdown).start()  # Shutdown in a separate thread

def run_http():
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 5000
    print(f"Server running at {HOST}:{PORT}")

    server = HTTPServer((HOST, PORT), HTTP)
    print("HTTP Server now running...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server interrupted.")
    finally:
        server.server_close()
        print("Server stopped.")
