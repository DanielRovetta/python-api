from flask import Flask, jsonify, request
from Facades import PessoaFacades


app = Flask(__name__)


# Consultar(todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    lista = PessoaFacades().getAll()
    lista_dicionario = []
    for item in lista:
        lista_dicionario.append(item.__dict__)
    return jsonify(lista_dicionario)


# Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    lista = PessoaFacades().getAll()
    for item in lista:
        if item.id == id:
            return jsonify(item.__dict__)


# # Editar
# @app.route('/livros/<int:id>', methods=['PUT'])
# def editar_livro_por_id(id):
#     livro_alterado = request.get_json()
#     for indice, livro in enumerate(livros):
#         if livro.get('id') == id:
#             livros[indice].update(livro_alterado)
#             return jsonify(livros[indice])
#
# # Criar
# @app.route('/livros', methods=['POST'])
# def incluir_novo_livro():
#     novo_livro = request.get_json()
#     livros.append(novo_livro)
#
#     return jsonify(livros)
#
# # Excluir
# @app.route('/livros/<int:id>', methods=['DELETE'])
# def excluir_livro(id):
#     for indice, livro in enumerate(livros):
#         if livro.get('id') == id:
#             del livros[indice]
#
#     return jsonify(livros)
app.run(port=5000, host='localhost', debug=True)

