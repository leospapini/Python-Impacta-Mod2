#dicionários


x = {
    'data' : '25/12/1956',
    'estoque' : 122
}

x['operação'] = 'venda'

print(x)
print(x['estoque'])
print(hash('estoque') & (15)) #     hash mostra o valor do índice do dicionário, com um limite de números de 0 até 15
print(hash('data') & (15))
print(hash('operação') & (15))

#   python sempre começa com uma tabela de 16, ou até 15, dps ele dobra caso precise


