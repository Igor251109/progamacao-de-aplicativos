from banco import conectar

def verReservas():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()

        cursor.execute("SELECT * FROM laboratorios")
        dados = cursor.fetchall()

        if not dados:
            print("não há nenhuma reserva.")
            return
        
        else:
            for reservas in dados:
                print(reservas)
    
    finally:
        if conexao:
            conexao.close()