"""This module contains a simple HTTP server example."""

import http.server
import socketserver

PORT = 8000

class TestMe:
    """A simple server class with methods to return a number and port."""

    def take_five(self):
        """Return the integer five."""
        return 5

    @property
    def port(self):
        """Return the server port."""
        return PORT

def run_server():
    """Run a simple HTTP server on the specified port."""
    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
