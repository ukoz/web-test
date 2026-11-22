import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PAGE = b'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Web Test</title><style>body{margin:0;min-height:100vh;display:grid;place-items:center;background:#101827;color:#eef5ff;font:18px system-ui}main{max-width:540px;padding:40px}small{color:#6ee7b7;letter-spacing:2px}h1{font-size:48px;line-height:1.05}p{color:#b8c5d8;line-height:1.6}code{color:#6ee7b7}</style><main><small>CONTAINER ONLINE</small><h1>Hello, world.</h1><p>This simple web app is running. The container is serving HTTP successfully.</p><p><code>GET /health</code> returns a health check.</p></main></html>'''

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = b'OK\n' if self.path == '/health' else PAGE
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8' if self.path == '/health' else 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

HTTPServer(('0.0.0.0', int(os.environ.get('PORT', '8080'))), Handler).serve_forever()
