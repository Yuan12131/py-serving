from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes('hello', 'utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes('Not Found', 'utf-8'))

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
