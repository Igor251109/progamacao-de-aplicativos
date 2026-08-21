def buscar_nome(lista, nome):
    if not lista:
        return None
    return nome in lista

def tem_senha_valida(senha):
    if len(senha) >= 8:
        return "senha permitida"
    else:
        return "senha não aceita"

assert buscar_nome(["igor", "carlos"], "igor") == True
assert buscar_nome([], "igor") == None
assert buscar_nome(["julio"], "julio") == True

assert tem_senha_valida("12345678") == "senha permitida"
assert tem_senha_valida("123456789") == "senha permitida"
assert tem_senha_valida("1234") == "senha não aceita"

print("certo")