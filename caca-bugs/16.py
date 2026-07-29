#            def menu(): 
#	            while True: 
#                    print("1. Cadastrar Aluno") 
#                    print("2. Sair") 
#                    opcao = input("Escolha: ") 
         
#                    if opcao == "1": 
#                        print("Cadastrando...") 
#                    elif opcao == "2": 
#                        print("Saindo do programa.") 
                    	# Por que o programa continua rodando e mostrando o menu mesmo digitando 2? 
#                       pass

#           RESOLUÇÃO:

def menu():
    while True:
        print("1. cadastrar aluno")
        print("2. sair")
        opcao = int(input("qual opção vai escolher?: "))

        if opcao == 1:
            print("cadastrando...")
            break
        elif opcao == 2:
            print("encerrando...")
            break