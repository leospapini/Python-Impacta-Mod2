#merge sort
#intercalação

def intercala(lst, ini, meio, fim):
    aux = []
    esq = ini
    dir = meio + 1
    while (esq <= meio and dir <= fim):
        if (lst[esq] <= lst[dir]):
            aux.append(lst[esq])
            esq += 1
        else:
            aux.append(lst[dir])
            dir += 1
    while (esq <= meio):
        aux.append(lst[esq])
        esq += 1
    while (dir <= fim):
        aux.append(lst[dir])
        dir += 1
    lst[ini:fim+1] = aux
    return lst

print(intercala([2, 4, 6, 1, 3, 5, 7], 0, 2, 6))

# neste exemplo acima, já tínhamos fornecido uma lista com a primeira metade ordenada
# e a segunda metade tbm, no exemplo abaixo criamos a função merge sort para descobri
# o meio automáticamente e já utilizar a função intercala para intercalar

def mergesort(lst, ini, fim):
    if (fim <= ini):        #base da recursão, lista tem 1 elemento ou menos? pare
        return
    meio = (ini+fim)//2
    mergesort(lst, ini, meio)
    mergesort(lst, meio+1, fim)
    intercala(lst, ini, meio, fim)

exemplo = [6, 4, 2, 7, 5, 3, 1]

mergesort(exemplo, 0, 6)
print(exemplo)
    
