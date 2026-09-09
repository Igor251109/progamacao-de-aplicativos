import sqlite3

def tratar_erros_funcoes(funcao):
    try:
        return funcao()
    except ValueError as e:
        print("\n dados inválidos", e)
        return
    except sqlite3.OperationalError as e:
        print("\n erro operacional no banco de dados:", e)
        return
    except sqlite3.IntegrityError as e:
        print("\n erro d integridade no banco de dados:", e)
        return
    except KeyboardInterrupt:
        print("\n programa encerrado pelo usuério.")
        return
    except sqlite3.Error as e:
        print("erro no banco de dados.", e)
