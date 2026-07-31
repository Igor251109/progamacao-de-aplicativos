senha = input("qual a senha de segurança?: ")
tentativa = int(input("qual a tentativa atual?: "))
vip = input("tem ingresso vip?: ")

if senha == "admin123" and (tentativa % 3 == 0 or vip == "sim"):
    print(f"tentativa numero {tentativa}: acesso concedido.")
else:
    print(f"tentativa numero {tentativa}: ACESSO NEGADO POR PROTOCOLO.")