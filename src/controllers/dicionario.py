from flask import Flask, jsonify
from server.instance import Server, server

app = server.app

dict = {'guri' : 'gurista'}

@app.route('/dicionario')
def get():
    return jsonify(dict)
