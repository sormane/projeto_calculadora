#Método, Função e classes
#Método não retorna valor
#Função retorna um valor
#Classe

class Calculadora: #Por convenção o nome da classe começa com maisculo
    def __init__(self):
        pass
    #É possível fazer sem o método init

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora() #estanciando a classe package_calc
#print(package_calc.valor_b)
print(calculadora.soma(10,2))
print(calculadora.subtracao(2,1))
print(calculadora.multiplicacao(10,5))
print(calculadora.divisao(100,2))