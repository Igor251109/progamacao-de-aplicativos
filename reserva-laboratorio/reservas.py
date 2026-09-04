from banco import conectar

def adicionarReservas():
    conexao = None
    cursor = None

    try:
        conexao, cursor = conectar()

        print("\n ==== SISTEMA DE CADASTRAMENTO DE RESERVAS ====")
        print("preencha as informações abaixo: ")

        dados = {
            "nomeLaboratorio": input("qual laboratório deseja fazer uma reserva?: "),
            "dataDesejada": input("qual a dat desejada da reserva?: (escreva no formato 00/00/0000)"),
            "horarioDesejado": input("qual o horário desejado?: (escreva no formato 00:00) "),
            "nomeSolicitante": input("qual o nome do solicitante?: ")
        }

        cursor.execute("SELECT nome_laboratorio, datas, horario, nome_solicitante FROM laboratorios WHERE nome_informatica = ?, datas = ?, horario = ?, nome_solicitante = ?", (dados["nomeLaboratorio"], dados["dataDesejada"], dados["horarioDesejado"], dados["nomeSolicitante"]))
        reserva = cursor.fetchone()

        if reserva:
            print("dados já existentes! reserva cancelada.")
            return
        
        else:
            cursor.execute('''INSERT INTO laboratorios (nome_laboratorio, datas, horario, nome_solicitante) VALUES (?, ?, ?, ?)''', (dados["nomeLaboratorio"], dados["dataDesejada"], dados["horarioDesejado"], dados["nomeSolicitante"]))
            conexao.commit()
        
    finally:
        if conexao:
            conexao.close()