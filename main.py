try:
    import Controlador
except Exception as erro:
    print(erro)


# import Facades
#
# lista = Facades.PessoaFacades().getAll()
# lista_dicionario = []
# for item in lista:
#     lista_dicionario.append(item.__dict__)
#     print(item.__dict__)

#
# import DAO
#
# valores = ('Daniel Rovetta', '12000/06/12', '580805877017', 'Masculino', 1.71, 52)
# dao = DAO.PessoaDAO().insert(valores)
#
# print(dao)
