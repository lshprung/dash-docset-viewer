import http.server

from config import *

class MyServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "content-type")
        self.end_headers()
        output = exec(open("." + self.path).read())
        self.wfile.write(output.encode())


if __name__ == "__main__":
    webServer = http.server.HTTPServer((Config.hostName, Config.serverPort), MyServer)
    print("Server started http://%s:%s" % (Config.hostName, Config.serverPort))
    
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
