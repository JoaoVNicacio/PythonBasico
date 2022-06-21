# teste com funções e metodos
def soma(a, b):
    return a+b


def subtracao(a, b):
    return a-b


def multiplicacao(a, b):
    return a*b


def divisao(a, b):
    return a/b


# chamando as funções
print(soma(5, 4))
print(subtracao(5, 4))
print(multiplicacao(5, 4))
print(divisao(5, 4))


# teste com classe
class Calculadora:
    # inicializando a classe com init self
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def somar(self):
        return self.a + self.b

    def subtrair(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        return self.a / self.b


# definindo numa variavel e chamando
calculadora = Calculadora(9,7)
#exibindo no console
print(calculadora.somar())
print(calculadora.subtrair())
print(calculadora.multiplicar())
print(calculadora.dividir())
