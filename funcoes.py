#Cadastro de dados

def cadastrarDado(lista):
    resp = "S"
    while resp =="S":
        tag = input("\n (✿) INFORME UMA TAG PARA CATALOGAR: (✿) ").upper()
        lista[tag] = [input("\n INFORME O EMAIL: "), input("\n SENHA: "), int(input("\n VALIDADE: "))]
        resp = input("DESEJA CADASTRAR MAIS UM DADO? ").upper()
 
#Exibicao dos dados

def exibirDados(lista):
    for tag, lista in lista.items():
        print("\n Tag: ", tag)
        print("\n Email: ", list[0])
        print("\n Senha: ", list[1])
        print("\n Validade: ", list[2])       
    tmp = input("\n PRESSIONE ENTER PARA CONTINUAR")
 
#Alterar Validade

def alterarValidade(lista):
    alteracao = input("\n INFORME A TAG PARA ALTERACAO DA VALIDADE: ").upper()
    if lista.get(alteracao) != None:
        lista = lista.get(alteracao)
        lista[alteracao] = [list[0], list[1], int(input("INFORME A VALIDADE: "))]
        lista = lista.get(alteracao)
        print("\n Email: ", list[0])
        print("\n Senha: ", list[1])
        print("\n Validade: ", list[2])
    else:
        print("ERROR 404 - NOT FOUND")
    tmp = input("\n PRESSIONE ENTER PARA CONTINUA")
 
#Deletar dados

def deletarDado(lista):
    deletar = input("\n INFORME A TAG A SER DELETADA: ").upper()
    if lista.get(deletar) != None:
        del lista[deletar]
    else:
        print("(◕︿◕✿) ERROR 404 - NOT FOUND (◕︿◕✿)")

#Buscar os dados catalogados

def buscarDado(lista):
    busca = input("\n INFORME A TAG DE BUSCA: ").upper()
    if lista.get(busca) != None:
        lista = lista.get(busca)
        print("\n Email: ", list[0])
        print("\n Senha: ", list[1])
        print("\n Validade: ", list[2])
    else:
        print("(◕︿◕✿) ERRO 404 - TAG NÃO ENCONTRADA (◕︿◕✿)")
    tmp = input("\n PRESSIONE ENTER PARA CONTINUAR")