a = int(input("qual o valor de A?: "))
b = int(input("qual o valor de B?: "))

temp = a
a = b
b = temp
print(f"o valor de A é: {a}")
print(f"o valor de B é: {b}")