from flask import Flask

class Server():
    def __init__(self):
        self.app = Flask(__name__)
    def run(self):
        self.app.run(
            debug=True,
            host='0.0.0.0'
        )
server = Server()