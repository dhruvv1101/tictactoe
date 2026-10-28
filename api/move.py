"""Vercel Python serverless function: POST /api/move  {"board":[...9], "ai":"X"|"O"}"""
import json, os, sys
from http.server import BaseHTTPRequestHandler
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tictactoe.engine import best_move, winner, is_full


class handler(BaseHTTPRequestHandler):
    def _send(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        try:
            data = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
            board, ai = data["board"], data["ai"]
            ok = (isinstance(board, list) and len(board) == 9
                  and all(c in ("X", "O", " ") for c in board) and ai in ("X", "O"))
            if not ok or winner(board)[0] or is_full(board):
                return self._send(400, {"error": "invalid board"})
            self._send(200, {"move": best_move(board, ai)})
        except Exception:
            self._send(400, {"error": "bad request"})
