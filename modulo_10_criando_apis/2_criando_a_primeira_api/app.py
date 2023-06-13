from flask import Flask, jsonify, request
from mock_db import postagens

app = Flask(__name__)

#rota padrão
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

# consulta por id
# Exemplo: http://localhost:5000/postagens/1
@app.route('/postagens/<int:indice>', methods=['GET'])
def obter_postagem_por_id(indice):
    return jsonify(postagens[indice], 200)

# Executando o servidor
app.run(port=5000, host='localhost', debug=True)