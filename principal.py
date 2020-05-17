from funcoes import *
 
lista = {"CARLOS": ["carlos@fiap.com.br", "carlos", 1234], "FERNANDO": ["fernando@fiap.com.br", "skfkd", 999], "EMILIA": ["emilia@gmail.com", "senha123", 9827], "CLEITON": ["profcleiton.silva@fiap.com.br", "infraest", 666], "RUAN": ["ruan.bianco@fiap.com.br", "fraude", 999], "ANA": ["ana.cruz@fiap.com.br", "odeioampg",  989], "SANDRO": ["sandro.nakamura@fiap.com.br", "labdemac", 1923], "VITOR": ["vitor.lace@fiap.com.br", "cyber", 2019], "GABRIELE": ["gabriele.mitiue@fiap.com.br", "arrogancia", 9234], "STEPHANIE": ["stephanie.cardoso@fiap.com.br", "hail", 999], "TRUMP": ["president@environment.com", "passwd", 999], "SILVIO": ["silvio.giavaroto@fiap.com.br", "silvivnhosososososososososo", 999], "ALBERICO": ["alberico@fiap.com.br", "jesus", 999], "RAFAEL": ["rafael@fiap.com.br", "voutehackear", 909], "PINHO": ["pinho@fiap.com.br", "pinhosol", 02]}
resp = "S"
opcao = 0

while resp == "S":
    print("\n (✿) SISTEMA DE EXIBICAO DE DADOS PUG BEAR (✿)")
    print("\n 1 - CADASTRAR DADOS ")
    print("2 - EXIBIR DADOS ")
    print("3 - ALTERAR A VALIDADE ")
    print("4 - EXCLUIR EMAIL ")
    print("5 - BUSCAR EMAILS VAZADOS ")
    print("6 - SAIR (◕︿◕✿) ")

    opcao = int(input("SELECIONE UMA OPCAO PARA CONTINUAR \n"))

    if opcao == 1:
        cadastrarDado(lista)
    elif opcao == 2:
        exibirDados(lista)
    elif opcao == 3:
        buscarDado(lista)
    elif opcao == 4:
        alterarValidade(lista)
    elif opcao == 5:
        deletarDado(lista)
    elif opcao == 6:
        exit()
    else:
        print("\n (◕︿◕✿) ERROR 404 - OPCAO INVALIDA (◕︿◕✿)")