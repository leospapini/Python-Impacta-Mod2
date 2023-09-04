#chamadas recursivas


#base da recursão
def cont_regressiva(n):
    if (n < 0):
        return      # se o número for menor q 0, não faz nada
    print(n)
    cont_regressiva(n-1)
    

cont_regressiva(3)

# 5! = 5*4*3*2*1 = 5*(4!) = 120
# 4! = 4*3*2*1 = 4*(3!) = 24
# 3! = 3*2*1 = 3*(2!) = 6
# 2! = 2*1 = 2*(1!) = 2
# 1! = 1*(0!)
# 0! = 1

# Em geral: N! = N*(N-1)!

def fatorial(N):
    if (N == 0):
        return 1
    return N*fatorial(N-1)

print('5! = ', fatorial(5))
print('6! = ', fatorial(6))
print('7! = ', fatorial(7))
