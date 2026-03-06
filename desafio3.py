codigo = int(input("qual o código?: "))
autorizacao = input("tem a altorização?: ")

if codigo == 999 or autorizacao == "s":
    print("correto")
else:
    print("erro 1: retornando a base")

bateria = int(input("qual o nivel de bateria?: "))
if bateria < 10:
    print("pouso de emergêngia autorizado!")

clima = input("qual o clima atual?: ")
vento = float(input("qual a velocidade do vento?: "))

if bateria >= 10 and clima == "ensolarado" and vento <= 30 or clima == "chuvoso" and vento < 11:
    print("pouso seguro autorizado.")
else:
    print("pouso não autorizado.")


