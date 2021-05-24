import os, sys
from http.server import BaseHTTPRequestHandler
from cowpy import cow
from Pillow import Image, ImageChops, ImageEnhance

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        # img1 = Image.open(r"headon2.png")
        # img2 = Image.open(r"sidetableshadow.png")
        # diff = ImageChops.difference(img2, img1)
        # diff.save("enhanced443.png")
        message = cow.Cowacter().milk('Hello from Python from a Serverless Function!')
        self.wfile.write(message.encode())
        return