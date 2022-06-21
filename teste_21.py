# testando imports
from teste_20 import Ventilador
from teste_19 import Calculadora
from teste_21_funcoes import Contador_Letras, Teste

#exibindo no codigo atual
if __name__ == '__main__' :
    ventilador=Ventilador()
    print('O aparelho está ligado? {}'.format(ventilador.ligado))
    ventilador.ligar()
    calculadora =Calculadora(5,4)
    print(calculadora.somar())
    print(calculadora.subtrair())
    print(calculadora.multiplicar())
    print(calculadora.dividir())
    listaLocal=['Lontra','ariranha','doninha']
    print('a quantidade de letras na lista é: {}, respectivamente'.format(Contador_Letras(listaLocal)))
    print(Teste())
