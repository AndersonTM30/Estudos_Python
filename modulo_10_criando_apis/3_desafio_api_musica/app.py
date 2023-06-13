from flask import Flask, jsonify, request
from mock_db import musicas

app = Flask(__name__)

@app.route('/cancoes', methods=['GET'])
def listar_musicas():
    return jsonify(musicas, 200)

@app.route('/cancoes/<int:indice>', methods=['GET'])
def listar_musicas_por_indice(indice):
    return jsonify(musicas[indice], 200)

@app.route('/cancoes', methods=['POST'])
def criar_musicas():
    musica = request.get_json()
    musicas.append(musica)
    return jsonify(musica, 200)

@app.route('/cancoes/<int:indice>', methods=['PUT'])
def atualizar_musica_por_indice(indice):
    musica = request.get_json()
    musicas[indice].update(musica)
    return jsonify(musicas[indice], 200)

@app.route('/cancoes/<int:indice>', methods=['DELETE'])
def deletar_musica_por_indice(indice):
    try:
        if musicas[indice] is not None:
            del musicas[indice]
            return jsonify(f'A música {musicas[indice]} foi excluída com sucesso!', 200)
    except:
        return jsonify('Música não encontrada!', 404)

app.run(port=5000, host='localhost', debug=True)