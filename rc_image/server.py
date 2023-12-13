#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from math import sqrt

hostName = "0.0.0.0"
serverPort = 5050

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # curl http://<ServerIP>/index.html
        if self.path == "/":
            x = 0.001
            for i in range(0, 100000):
                x += sqrt(x)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            content = open('index.html', 'rb').read()
            self.wfile.write(content)
        else:
            self.send_response(404)
            return

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), Handler)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
    