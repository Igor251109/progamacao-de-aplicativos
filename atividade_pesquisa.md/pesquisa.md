                    Parte 1 — Busca Sequencial

A busca sequencial (ou linear) verifica os elementos da lista um por um, começando pelo primeiro, até encontrar o valor procurado ou chegar ao final da lista.

Para encontrar o número 7 na lista [3, 1, 9, 7, 2], o Python faria as seguintes verificações:

Verifica 3, não é o 7.
Verifica 1, não é o 7.
Verifica 9, não é o 7.
Verifica 7, é o 7.
Portanto, o número 7 foi encontrado na 4ª verificação.

Lista com 1.000 registros
Em uma lista desordenada com 1.000 registros, no pior cenário o programa precisará verificar todos os 1.000 elementos.

Isso acontece quando:

o elemento procurado está na última posição; ou
o elemento não existe na lista.
Resposta: 1.000 verificações no máximo.



                PARTE 2 - Busca Binária (Binary Search)

1. Pré-requisito:
A lista precisa estar ordenada (em ordem crescente ou decrescente) para que a busca binária possa ser executada corretamente.

2. Estratégia "dividir para conquistar":
A busca binária verifica o elemento do meio da lista. Depois, compara esse elemento com o valor procurado:

Se o valor procurado for igual ao elemento do meio, a busca termina.
Se for menor, a busca continua apenas na metade esquerda.
Se for maior, continua apenas na metade direita.
Assim, a cada comparação, metade dos elementos é descartada, tornando a busca muito mais rápida.

3. Por que cerca de 10 comparações para 1.000 registros?
Porque a cada comparação a quantidade de elementos é reduzida pela metade:

1000 → 500 → 250 → 125 → 62 → 31 → 15 → 7 → 3 → 1

Como 
2
10
=
1024
, em aproximadamente 10 etapas é possível reduzir uma lista de 1.000 elementos a apenas um elemento.

Portanto, a busca binária possui complexidade O(log₂ n), enquanto a busca sequencial possui complexidade O(n).


                Conexão com o Banco de Dados SQLite:


A criação de uma Chave Primária (PRIMARY KEY) ou de um Índice permite que o SQLite organize os dados de forma que ele possa localizar um registro de maneira muito mais eficiente, sem precisar verificar todas as linhas.

Sem índice, o banco faz um Full Table Scan, ou seja, verifica os registros um por um:

Ana? → Não → Ana? → Não → Ana? → Sim...

Já com um índice, o SQLite mantém uma estrutura de dados organizada para facilitar a localização do valor. Assim, ele consegue descartar grandes partes dos dados a cada etapa, de forma semelhante à ideia da Busca Binária, em vez de analisar todos os registros.

Por exemplo, imagine uma tabela com 1.000.000 de alunos. Sem índice, no pior caso, o SQLite pode precisar verificar até 1.000.000 de linhas. Com um índice adequado, a busca pode exigir apenas algumas etapas de navegação pela estrutura do índice.

Em resumo: o índice funciona como um "guia" organizado que permite ao SQLite encontrar rapidamente onde está o registro. Por isso, consultas que utilizam colunas indexadas são muito mais rápidas, especialmente em tabelas grandes.

Observação: tecnicamente, o SQLite não precisa usar literalmente uma busca binária simples; seus índices são normalmente estruturas B-tree/B+tree, projetadas para buscas, inserções e consultas eficientes. A comparação com a busca binária é uma forma didática de entender por que o índice reduz drasticamente a quantidade de dados que precisa ser examinada.


                Ordenação Automática no SQLite (ORDER BY):


1. Bubble Sort

O Bubble Sort (Ordenação por Bolha) percorre uma lista comparando elementos vizinhos, dois de cada vez.

Imagine:

[5, 3, 8, 2]

Queremos ordenar do menor para o maior.

Primeiro:

5 e 3 → estão na ordem errada → troca

[3, 5, 8, 2]

Depois compara:

5 e 8 → ordem correta → não troca

[3, 5, 8, 2]

Depois:

8 e 2 → ordem errada → troca

[3, 5, 2, 8]

Percebe o que aconteceu? O maior número, 8, foi "empurrado" para o final.

O algoritmo então percorre a lista novamente:

[3, 5, 2, 8]

3 e 5 → não troca
5 e 2 → troca

[3, 2, 5, 8]

Mais uma passagem:

3 e 2 → troca

[2, 3, 5, 8]

Pronto.
A ideia central que você precisa guardar é:

Bubble Sort = compara vizinhos e troca quando estão na ordem errada.


2. E o Selection Sort?

Ele trabalha de outra maneira.

Imagine novamente:

[5, 3, 8, 2]

O Selection Sort procura o menor elemento da parte ainda não ordenada.

O menor é 2.

Então troca o 2 com o primeiro elemento (5):

[2, 3, 8, 5]

Agora o 2 já está definitivamente na posição correta.

Depois procura o menor entre:

[3, 8, 5]

É 3, que já está no lugar.

Depois procura o menor entre:

[8, 5]

É 5. Troca com 8:

[2, 3, 5, 8]

Ou seja:

Bubble Sort: faz várias comparações e trocas entre elementos vizinhos.

Selection Sort: procura o menor elemento disponível e o coloca diretamente na próxima posição correta.