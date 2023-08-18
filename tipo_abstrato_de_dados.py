# TAD = tipo abstrato de dados



# Queremos armazenar os seguintes dados:
#   nome
#   idade
#   altura
#   peso
#   tipo sanguíneo (se conhecido)
#   queixa no ps (se houver)
#   datas de consulta

# operações:
# alterar idade
# alterar peso
# alterar queixa
# adicionar data de consulta

class Paciente:
    def __init__(self, nome, idade, altura, peso, queixa=None, sangue=None):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.sangue = sangue
        self.peso = peso
        self.queixa = queixa
        self.consultas = []

    def altera_idade(self, nova_idade):
        self.idade = nova_idade

    def altera_altura(self, nova_altura):
        self.altura = nova_altura

    def altera_peso(self, novo_peso):
        self.peso = novo_peso

    def altera_sangue(self, tipo_sangue):
        self.sangue = sangue

    def add_queixa(self, queixa):
        self.queixa = queixa

    def adiciona_consulta(self, data_da_consulta):
        self.consultas.append(data_da_consulta)

p = Paciente('Leonardo', 27, 1.70, 70, 'dor de estômago', 'A+')
p.adiciona_consulta('18/08/2023')
p.adiciona_consulta('10/07/2023')
p.adiciona_consulta('09/06/2023')
print('Nome       :',p.nome)
print('idade:     :',p.idade)
print('altura:    :',p.altura)
print('peso:      :',p.peso)
print('queixa:    :',p.queixa)
print('sangue:    :',p.sangue)
print('consultas: :',p.consultas)
