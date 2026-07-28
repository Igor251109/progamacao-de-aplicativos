import sqlite3 
 
def buscar_professor(id_prof): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
     
	# O Python reclama de "Incorrect number of bindings".  
	# Estamos passando a variável, por que ocorre o erro?           # aqui
    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof,)) # resposta: a falta da vírgula (,) depois do "id_prof"
    resultado = cursor.fetchone() 
    print(resultado) 
    conexao.close()