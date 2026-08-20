"""Mock courier endpoint for Part B. Listens on http://127.0.0.1:8001.

Logs every shipment request to stdout and to shipments.log, returns 200 for a
valid shipment and 422 for a missing order_id.
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

LOG = "shipments.log"


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            data = {}
        with open(LOG, "a") as f:
            f.write(json.dumps({"path": self.path, "payload": data}) + "\n")
        print(f"[courier] POST {self.path} {data}")
        if not data.get("order_id"):
            self.send_response(422)
            self.end_headers()
            self.wfile.write(b'{"error": "missing order_id"}')
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"ok": true}')

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    print("mock courier listening on http://127.0.0.1:8001")
    HTTPServer(("127.0.0.1", 8001), Handler).serve_forever()
