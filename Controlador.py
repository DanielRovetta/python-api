from flask import Flask, jsonify, request
from Facades import PessoaFacades, ClienteFacades
from BusinessException import DadosNaoEncotrados


app = Flask(__name__)


def __obterJson(lista: list):
    lista_dicionario = []
    for item in lista:
        lista_dicionario.append(item.__dict__)
    return jsonify(lista_dicionario)


def __obterJsonCliente(lista: list):
    lista_dicionario = []
    for item in lista:
        item.pessoa = item.pessoa.__dict__
        lista_dicionario.append(item.__dict__)
    return jsonify(lista_dicionario)


@app.route('/pessoa', methods=['GET'])
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


@app.route('/cliente', methods=['GET'])
def obter_cliente():
    try:
        id = request.args.get('id', default=None)
        if id is None:
            lista = ClienteFacades().getAll()
            return __obterJsonCliente(lista)

        id = int(id)
        lista = ClienteFacades().getById(id)
        return __obterJsonCliente(lista)

    except DadosNaoEncotrados as error:
        print(error)
        return jsonify(str(error))

    except (TypeError, ValueError) as error:
        print(error)
        return jsonify("Id informado Inválido: " + str(error))

    except Exception as error:
        print(error)
        return jsonify("Erro ao executar: " + str(type(error)) + ' ' + str(error))


@app.route('/pessoa', methods=['POST'])
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


@app.route('/pessoa', methods=['PUT'])
def editar_pessoa_por_id():
    try:
        requisicao = request.get_json()

        if type(requisicao) == list:
            lista = []
            for item in requisicao:
                nova_pessoa = PessoaFacades().uptade(item)
                lista.append(nova_pessoa[0])
            return __obterJson(lista)

        if type(requisicao) == dict:
            lista = PessoaFacades().uptade(requisicao)
            return __obterJson(lista)

    except DadosNaoEncotrados as error:
        print(error)
        return jsonify(str(error))

    except Exception as error:
        print(error)
        return jsonify("Erro ao executar: " + str(error))


# Excluir
@app.route('/pessoa', methods=['DELETE'])
def excluir_pessoa():
    try:
        requisicao = request.get_json()

        if type(requisicao) == list:
            lista = []
            for item in requisicao:
                nova_pessoa = PessoaFacades().delete(item)
                lista.append(str(nova_pessoa))
            return jsonify(lista)

        if type(requisicao) == dict:
            lista = PessoaFacades().delete(requisicao)
            return jsonify(lista)

    except DadosNaoEncotrados as error:
        print(error)
        return jsonify(str(error))

    except (TypeError, ValueError) as error:
        print(error)
        return jsonify("Id informado Inválido: " + str(error))

    except Exception as error:
        print(error)
        return jsonify("Erro ao executar: " + str(type(error)) + ' ' + str(error))


app.run(port=5000, host='localhost', debug=True)
