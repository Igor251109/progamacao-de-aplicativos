1. Alunos em ordem alfabética pelo nome

        SELECT * FROM alunos
        ORDER BY nome ASC;

ASC significa ascendente. Para texto, isso corresponde, de forma geral, à ordem alfabética A → Z.

Inclusive, ASC é o padrão, então isto também funciona:

            SELECT * FROM alunos
            ORDER BY nome;

2. Alunos da maior idade para a menor

        SELECT * FROM alunos
        ORDER BY idade DESC;

DESC significa decrescente, então se tivermos:

16, 18, 15, 17

o resultado será:

18, 17, 16, 15

Então guarda essa lógica:

ORDER BY coluna ASC → crescente
ORDER BY coluna DESC → decrescente

E isso você provavelmente vai usar bastante com SQLite. Por exemplo, no Python:

        cursor.execute("""
            SELECT * FROM alunos
            ORDER BY idade DESC
            """)

            alunos = cursor.fetchall()

O fetchall() já recebe os registros na ordem determinada pelo SQLite. Você não precisa buscar tudo e depois criar um for para ordenar.