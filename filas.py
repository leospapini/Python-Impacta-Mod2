# Fila

# especificações:
# *sequência arbitrária de dados

# operações fornecidas:
# criar estrutura
# inserir no fim da fila
# remover do inicio da fila
# saber o tamanho
# verificar quem é o primeiro da file sem remover

# ordem de operações:
# criar fila F
# inserir em F o elemento 41
# inserir em F o elemento 65
# inserir em F o elemento 29
# remover um elemento de F
# inserir em F o elemento 56
# verificar o tamanho de F
# verificar quem é o primeiro da fila (o mais antigo)

from collections import deque

class Fila:
    def __init__(self):
        self.fila = deque()
        
#estrutura criada
        
    def insere(self, novo):
        self.fila.append(novo)

#inserir no fim da fila

    def remove(self):
        return self.fila.popleft()

#remover do inicio

    def __len__(self):
        return len(self.fila)

#saber o tamanho

    def proximo(self):
        prox = self.fila.popleft()
        self.fila.appendleft(prox)
        return prox

#verificar quem e o primeiro da fila sem remover, pq? pq temos q resolver o primeiro
#e armazená-lo numa variável prox, dps retornamos ele no mesmo lugar da fila com o appendleft
#mas retornando o valor do prox verificado

F = Fila()
F.insere(41)
F.insere(85)
F.insere(29)
print(F.fila)
print('Removi o elemento', F.remove())
#removemos o elemento 41 pois no método remove utilizamos o popleft de acordo
#com a política FIFO(first in first out)
F.insere(56)
print('A fila tem tamanho', len(F))
print('O primeiro da fila é', F.proximo())
print(F.fila)
