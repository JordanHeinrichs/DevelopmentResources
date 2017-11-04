#!/usr/bin/env python

from http.server import SimpleHTTPRequestHandler, HTTPServer
import sys
import psutil
import json
from datetime import datetime

class SoarWebServer(SimpleHTTPRequestHandler):

    def do_POST(self):
        total_cpu = psutil.cpu_count()
        cpu_usage = psutil.cpu_percent()
        time = datetime.now().time()
        memory = psutil.virtual_memory()
        total_ram = "{0:.2f}".format(memory.total / pow(2, 30))
        used_ram = "{0:.2f}".format(memory.used / pow(2, 30))
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        json_str = json.dumps({'time': time.strftime("%H:%M:%S"), 'totalCpu': total_cpu,
                          'cpuUsage': cpu_usage, 'totalRam': total_ram, 'usedRam': used_ram})
        self.wfile.write(json_str.encode())

def main():
    if len(sys.argv) != 2:
        print("Server takes in a single argumenet of the port")
        print("Usage: python webserver.py <portnum>")
        return

    port = int(sys.argv[1])
    if port < 1024:
        print("Port number must be over 1024")
        return

    print('Starting server on port ' + str(port) + '...')

    server_address = ('', port)
    httpd = HTTPServer(server_address, SoarWebServer)
    httpd.serve_forever()

if __name__ == "__main__":
    main()
