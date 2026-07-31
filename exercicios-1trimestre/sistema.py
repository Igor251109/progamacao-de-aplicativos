nome = input("qual seu nome?: ")
codigo = int(input("qual o codigo de segurança?: "))
usuario = "admin"
codigo_seguranca = 999

if nome == usuario and codigo == codigo_seguranca:
    print("ecesso autorizado.")
else:
    print("acesso negado. Alerta de segurança ativado!")