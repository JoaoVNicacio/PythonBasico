# teste com classe
class Calculadora:
    # inicializando a classe com init self
    def __init__(self):
        pass

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a,  b):
        return a / b


# definindo numa variavel e chamando
calculadora = Calculadora()
#exibindo no console
print(calculadora.somar(int(input('digite 1o o valor da adição ')),int(input('digite 2o o valor '))))
print(calculadora.subtrair(int(input('digite 1o o valor subtração ')),int(input('digite 2o o valor '))))
print(calculadora.multiplicar(int(input('digite 1o o valor da multiplicação ')),int(input('digite 2o o valor '))))
print(calculadora.dividir(int(input('digite 1o o valor da divisão ')),int(input('digite 2o o valor '))))