#selection sort ordenação por seleção

import time

valores = [2, 3, 8, 6, 5, 1, 9, 7]

# calcula quem é o mínimo na região de i até o fim da lista
def selection(lista):
    i = 0
    while (i < len(lista) - 1):
        minimo = lista[i]
        ind_minimo = i
        for j in range(i+1, len(lista)):
            if (lista[j] <  minimo):
                minimo = lista[j]
                ind_minimo = j
        lista[ind_minimo] = lista[i]
        lista[i] = minimo
        i += 1
    return lista


selection(valores)
print(valores)



l1 = list(range(3000, 0, -1))
l2 = list(range(6000, 0, -1))

t1 = time.process_time()
selection(l1)
t2 = time.process_time()

print('O tempo de execução foi', (t2-t1))

t1 = time.process_time()
selection(l2)
t2 = time.process_time()

print('O tempo de execução foi', (t2-t1))
