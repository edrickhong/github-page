import http.server
import socketserver


def main():
    port = 8000
    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("",port),handler) as httpd:
        print("Serving at http://localhost:{}".format(port))
        httpd.serve_forever()
    return


if __name__ == "__main__":
    main()
