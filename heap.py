#heap - importância da ordem de chegada/prioridade

#   cada pai tem q ser maior q seus dois filhos
#     9
#  6     3
#4   5 2



heap = [9, 6, 3, 4, 5, 2] #     primeira a raiz, dps os filhos da raiz, dps os filhos dos filhos da raiz(folhas) da esquerda pra direita
#   maior elemento sempre será o índice 0

class Heap:
    def __init__(self):
        self.heap = []

#   retorna o índice que é pai de um determinado índice
    def pai(self, ind_filho):
        return (ind_filho-1)//2

#   retorna o índice do filho esquerdo do índice

    def fesq(self, ind_pai):
        return 2*ind_pai + 1

#   retorna o índice do filho direito do índice

    def fdir(self, ind_pai):
        return 2*ind_pai + 2

#   retorna o índice do maior filho de um elemento

    def maior_filho(self, ind_pai):
        fesq, fdir = self.fesq(ind_pai), self.fdir(ind_pai)
        if (fesq >= len(self.heap)):
            return None
        elif (fdir >= len(self.heap)):
            return fesq
        elif (self.heap[fesq] > self.heap[fdir]):
            return fesq
        else:
            return fdir

#   recebe dois índices do heap e troca o conteudo entre os dois EM QUALQUER LINGUAGEM
    def troca(self, i, j):
        aux = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = aux
        
#   recebe dois índices do heap e troca o conteudo entre os dois no python, mais eficaz

    def troca_python(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

#   retorna o maior elemento do heap (sem remover)
    def maximo(self):
        return self.heap[0]

#   insere um novo elemento no heap

    def insere(self, novo):
        self.heap.append(novo)
        ind_novo = len(self.heap) - 1
        while (ind_novo != 0 and self.heap[self.pai(ind_novo)] < self.heap[ind_novo]):
            self.troca(ind_novo, self.pai(ind_novo))
            ind_novo = self.pai(ind_novo)

#   remove o maior elemento do heap

    def remove(self):
        removido = self.maximo()
        self.troca(0, len(self.heap) - 1)
        self.heap.pop()
        i = 0
        while (self.maior_filho(i) is not None and self.heap[self.maior_filho(i)] > self.heap[i]):
            ind_filho = self.maior_filho(i)
            self.troca(i, ind_filho)
            i = ind_filho

h = Heap()
h.insere(3)
h.insere(5)
h.insere(9)
h.insere(6)
h.insere(4)
h.insere(2)

print('O máximo na árvore é:', h.maximo())
print('Removi', h.remove())
print('O máximo na árvore é:', h.maximo())
