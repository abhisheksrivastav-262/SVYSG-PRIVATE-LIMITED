from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

class SPAHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        requested = Path(self.translate_path(self.path.split('?', 1)[0]))
        if not requested.exists() and not self.path.startswith('/src/'):
            self.path = '/index.html'
        return super().do_GET()

ThreadingHTTPServer(('127.0.0.1', 4173), SPAHandler).serve_forever()
