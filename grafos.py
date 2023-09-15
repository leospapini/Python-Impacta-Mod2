#grafos - lista de vizinhanças

class Grafo:
    def __init__(self, numero_vertices):
        self.adj = [ [] for i in range(numero_vertices) ]
        self.V = numero_vertices
        self.E = 0 #    número de arestas

#   torna vizinhos no grafo os vértices 1 e 2

    def adiciona_aresta(self, vertice1, vertice2):
        self.adj[vertice1].append(vertice2)#    vertice 2 entra na lista de vizinhos do 1
        self.adj[vertice2].append(vertice1)#    vertice 1 entra na lista de vizinhos do 2
        self.E += 1

#   retorna lista com vizinhos do vértice v

    def vizinhos(self, v):
        return self.adj[v]
        
G = Grafo(3) #  3 vértices
G.adiciona_aresta(0, 1)
G.adiciona_aresta(0, 2)

# vértice 0 está conectado com 1 e 2, ou seja, 2 arestas

print('G tem', G.V, 'vértices e', G.E, 'arestas')

# (0)---(1)
#  | 
# (2)
#   representação do grafo acima de G

H = Grafo(7)
H.adiciona_aresta(0, 1)
H.adiciona_aresta(0, 2)
H.adiciona_aresta(1, 4)
H.adiciona_aresta(1, 3)
H.adiciona_aresta(3, 2)
H.adiciona_aresta(5, 4)
H.adiciona_aresta(5, 6)

# (0)---(1)---(4)---(5)
#  |     |           |   
# (2)---(3)         (6)
#   representação do grafo acima de H

print('H tem', H.V, 'vértices e', H.E, 'arestas')
print('No grafo H, os vizinhos do vértice 1 são:', H.vizinhos(1))
print('Vizinhos do vértice 3 no grafo H:')
for vertice in H.vizinhos(3):
    print(vertice)
