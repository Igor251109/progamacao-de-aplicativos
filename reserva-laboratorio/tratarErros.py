import sqlite3

def tratarErrosFuncoes(funcao):
    try:
        funcao()
    except ValueError:
        print("dados invalidos.")
        return
    except KeyboardInterrupt:
        print("programa encerrado.")
        return
    except sqlite3.IntegrityError:
        print("erro de intregidade no banco de dados.")
        return
    except sqlite3.OperationalError:
        print("erro operacional no banco de dados.")
        return