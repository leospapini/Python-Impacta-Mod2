#BST = árvores binárias
# TODO NÓ TEM Q TER 2 FILHOS NO MÁXIMO, dai o nome binário

# leftson, rightson = filho esquerdo e filho direito
# todo nó precisa que:
# Seus descendentes à esquerda sejam menores
# Seus descendentes à direita sejam maiores


# Eficiência da busca binária em BST
# começando sempre pela raiz, a busca binária visita no máximo um nó de cada vez
# portanto, seu custo é proporcional à altura da árvore


class Arvore:
    def __init__(self, chave, filho_esquerdo = None, filho_direito = None):
        self.chave = chave
        self.fesq = filho_esquerdo
        self.fdir = filho_direito
        
    def exibir_pre_ordem(self):         #exibe em ordem de menor pro maior, mesmo q o menor seja um filho e não a raiz em sí
        if (self.fesq is not None):
            self.fesq.exibir_pre_ordem()
        print(self.chave)
        if (self.fdir is not None):
            self.fdir.exibir_pre_ordem()

    def exibir_in_ordem(self):         #exibe em ordem de de raiz, esquerda e direita
        print(self.chave)
        if (self.fesq is not None):
            self.fesq.exibir_pre_ordem()
        if (self.fdir is not None):
            self.fdir.exibir_pre_ordem()


x = Arvore(8, None, Arvore(11))
y = Arvore(7, Arvore(5), x)

# print('y é um nó que tem chave', y.chave)
# print('y tem como filho esquerdo', y.fesq)
# print('x é um filho direito de y', y.fdir)

print('Pré-ordem a seguir:')
y.exibir_pre_ordem()

print('In-ordem a seguir:')
y.exibir_in_ordem()

#   7
# 5   8
#       11


