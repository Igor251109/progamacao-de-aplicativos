import json
import os

banco_de_dados = 'biblioteca.json'

def cadastrar_livros():
    try:
        print("\n ==== SISTEMA DE CADASTRAMENTO ====")

        if os.path.exists(banco_de_dados):
            with open (banco_de_dados, 'r') as a:
                livros = json.load(a)
        
        else:
            livros = []

        dados = {
            "nome_livro": input("digite o nome do livro: "),
            "autor": input("digite o nome do autor do livro: "),
            "ano": int(input("digite o ano do lançamento do livro: "))
        }

        livros.append(dados)

        with open(banco_de_dados, 'w', encoding='utf-8') as a:
            json.dump(livros, a, indent=4, ensure_ascii=False)

            print("livro adicionado com sucesso.")

    except ValueError:
        print("dados inválidos.")
        return
    
    except KeyboardInterrupt:
        print("voltando ao menu")
        return


def ver_livros():
    try:
        print("\n ==== VER LIVROS ====")

        if os.path.exists(banco_de_dados):
            with open(banco_de_dados, 'r') as a:
                livros = json.load(a)
            
        else:
            livros = []
        
        if not livros:
            print("não há registros")
            return
        
        n = 0
        for livro in livros:
            if livro == 0:
                print("não há nenhum cadastro.")
                return
            
            print(f"nome do livro: {livro['nome_livro']},")
            print(f"autor: {livro['autor']},")
            print(f"ano de lançamento: {livro['ano']}")

            n += 1

    except KeyboardInterrupt:
        print("voltando ao menu")
        return

def atualizar():
    try:
        if os.path.exists(banco_de_dados):
            with open(banco_de_dados, 'r') as a:
                livros = json.load(a)
        else:
            livros = []

            qual_mudar = input("digite o nome do livro que deseja atualizar: ").strip()
        
        dados = {
            "nome_livro": input("digite o nome do livro: "),
            "autor": input("digite o nome do autor do livro: "),
            "ano": int(input("digite o ano do lançamento do livro: "))
        }

        with open(banco_de_dados, 'w') as a:
            livros[qual_mudar] = dados
    except ValueError:
        print()