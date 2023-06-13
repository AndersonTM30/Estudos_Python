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

# criar uma nova postagem
@app.route('/postagens', methods=['POST'])
def criar_postagem():
    postagem = request.get_json()
    postagens.append(postagem)
    return jsonify(postagem, 200)

# atualizar uma postagem existente
@app.route('/postagens/<int:indice>', methods=['PUT'])
def atualizar_postagem_por_indice(indice):
    postagem = request.get_json()
    postagens[indice].update(postagem)

    return jsonify(postagens[indice], 200)

# deletear uma postagem por id
@app.route('/postagens/<int:indice>', methods=['DELETE'])
def excluir_postagem(indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice]
            return jsonify(f'Postagem {postagens[indice]} foi excluída com sucesso!', 200)
    except:
        return jsonify('Não foi possível encontrar a postagem para exclusão', 404)

# Executando o servidor
app.run(port=5000, host='localhost', debug=True)
