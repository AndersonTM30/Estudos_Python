from flask import Flask, jsonify, request
from mock_db import postagens

app = Flask(__name__)

#rota padrão
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

# Executando o servidor
app.run(port=5000, host='localhost', debug=True)
