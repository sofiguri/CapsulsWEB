import http.server
import socketserver
import os

PORT = 80
DIR_PATH = "C:\\Users\\kosta\\OneDrive\\Рабочий стол\\ГРафик"


class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if not self.path.endswith('/'):
            self.path += '/'
        try:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(open(os.path.join(DIR_PATH, self.path[1:], 'index.html'), 'rb').read()))
        except Exception as e:
            print(f"Error: {str(e)}")


# Запуск сервера
httpd = socketserver.TCPServer(('127.0.0.1', 8000), MyRequestHandler)
httpd.serve_forever()

# Запуск в браузере - http://127.0.0.1:8000/
