import http.server
import logging
import socket
import socketserver
from pathlib import Path

PORT = 8000
ROOT = Path(__file__).parent.resolve()
HOST = "0.0.0.0"
LOG_FILE = ROOT / "mobile_server.log"

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
)


def get_local_ip() -> str:
    """Get the machine's local IPv4 address on the current network."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
        except OSError:
            return "127.0.0.1"


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)


if __name__ == "__main__":
    local_ip = get_local_ip()
    print("Serving the PC site for mobile access...")
    print(f"Open on this PC: http://127.0.0.1:{PORT}/index.html")
    print(f"Open on mobile: http://{local_ip}:{PORT}/index.html")
    print("Press Ctrl+C to stop the server.")

    logging.info("Starting mobile server")
    logging.info("Open on this PC: http://127.0.0.1:%s/index.html", PORT)
    logging.info("Open on mobile: http://%s:%s/index.html", local_ip, PORT)

    socketserver.TCPServer.allow_reuse_address = True
    try:
        server_class = getattr(http.server, "ThreadingHTTPServer", socketserver.TCPServer)
        with server_class((HOST, PORT), CustomHandler) as httpd:
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nServer stopped.")
                logging.info("Server stopped by user")
    except OSError as exc:
        error_msg = f"Failed to start server on {HOST}:{PORT}: {exc}"
        print(error_msg)
        print("확인: 포트 8000이 이미 사용 중인지, 관리자 권한이 필요한지 확인하세요.")
        logging.error(error_msg)
        raise
