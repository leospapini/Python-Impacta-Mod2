#buscas em listas#

import time

estudantes = ['Artur', 'Bianca', 'Daiane', 'Fabio', 'Joana', 'Lucio', 'Thais']

print('Fabio está na turma? ', 'Fabio' in estudantes)

def busca_linear(lista, alvo):
    for elemento in lista:
        if (elemento == alvo):
            return True
    return False

def busca_binaria(lista, alvo):
    ini = 0
    fim = len(lista) - 1
    while(ini <= fim):
        meio = (ini+fim)//2
        if (lista[meio] == alvo):
            return True
        elif (lista[meio] > alvo):
            fim = meio - 1
        else:
            ini = meio + 1
    return False



alvo = (input('Qual o nome buscado? linear: '))
print('busca linear feita', busca_linear(estudantes, alvo))

alvo = (input('Qual o nome buscado? binária: '))
print('busca linear feita', busca_binaria(estudantes, alvo))

L1 = list(range(1000000))
L2 = list(range(2000000))

t1 = time.process_time()
busca_binaria(L1, 1000000)
t2 = time.process_time()

print('O tempo de execução foi', (t2-t1))

t1 = time.process_time()
busca_binaria(L2, 2000000)
t2 = time.process_time()

print('O tempo de execução foi', (t2-t1))
