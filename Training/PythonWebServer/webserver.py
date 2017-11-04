#!/usr/bin/env python

from http.server import SimpleHTTPRequestHandler, HTTPServer
import sys

class SoarWebServer(SimpleHTTPRequestHandler):

    def do_POST(self):
        self.wfile.write("Send your POST response here!")


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
