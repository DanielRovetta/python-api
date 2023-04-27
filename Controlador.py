from flask import Flask, jsonify, request
from Facades import PessoaFacades
from BusinessException import DadosNaoEncotrados


app = Flask(__name__)


def __obterJson(lista: list):
    lista_dicionario = []
    for item in lista:
        lista_dicionario.append(item.__dict__)
    return jsonify(lista_dicionario)


@app.route('/pessoas', methods=['GET'])
def obter_pessoa():
    try:
        id = request.args.get('id', default=None)
        if id is None:
            lista = PessoaFacades().getAll()
            return __obterJson(lista)

        id = int(id)
        lista = PessoaFacades().getById(id)
        return __obterJson(lista)

    except DadosNaoEncotrados as error:
        print(error)
        return jsonify(str(error))

    except (TypeError, ValueError) as error:
        print(error)
        return jsonify("Id informado Inválido: " + str(error))

    except Exception as error:
        print(error)
        return jsonify("Erro ao executar: " + str(type(error)) + ' ' + str(error))


@app.route('/pessoas', methods=['POST'])
def incluir_nova_pessoa():
    try:
        requisicao = request.get_json()

        if type(requisicao) == list:
            lista = []
            for item in requisicao:
                nova_pessoa = PessoaFacades().insert(item)
                lista.append(nova_pessoa[0])
            return __obterJson(lista)

        if type(requisicao) == dict:
            lista = PessoaFacades().insert(requisicao)
            return __obterJson(lista)

    except DadosNaoEncotrados as error:
        print(error)
        return jsonify(str(error))

    except Exception as error:
        print(error)
        return jsonify("Erro ao executar: " + str(error))


# # Editar
# @app.route('/livros/<int:id>', methods=['PUT'])
# def editar_livro_por_id(id):
#     livro_alterado = request.get_json()
#     for indice, livro in enumerate(livros):
#         if livro.get('id') == id:
#             livros[indice].update(livro_alterado)
#             return jsonify(livros[indice])
#
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
