id = int(input("qual seu id?: "))
temperatura = int(input("qual a temperatura da maquina?: "))
tempo_de_uso = int(input("qual o tempo de uso continuo da maquina?: "))

if (id  % 3 == 0 and temperatura > 40) or tempo_de_uso > 8:
    print(f"funcionário {id}, você foi designado para a limpeza da máquina hoje.")
else:
    print(f"funcionario {id}, suas máquinas operam dentro dos padrões.")