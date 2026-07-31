curso = input("você concluiu o curso de segurança?: ")
instrutor = input("o instrutor está na sala?: ")

if curso == "sim":
    if instrutor == "sim":
        print("operação iniciada.")
else:
    print("faça o curso primeiro")
