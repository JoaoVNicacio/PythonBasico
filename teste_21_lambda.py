contadorLetras = lambda lista: [len(x) for x in lista]
listaPessoas=['Pedro','José']
print(contadorLetras(listaPessoas))

#operações com lambda
soma = lambda a,b: a+b
subtracao= lambda a,b: a-b
multiplicacao = lambda a,b: a*b
divisao = lambda a,b: a/b
print(soma(9,7))
print(subtracao(9,7))
print(multiplicacao(9,7))
print(divisao(9,7))

#unindo varias funções anônimas em uma só variável
calculadora = {
    'soma' : lambda a,b: a+b,
    'subtracao' : lambda a,b: a-b,
    'multiplicacao' : lambda a,b: a*b,
    'divisao' : lambda a,b: a/b
}
print(type(calculadora))
som = calculadora['soma']
subtr = calculadora['subtracao']
multi = calculadora['multiplicacao']
divi = calculadora['divisao']
print(som(3,5))
print(subtr(3,7))
print(multi(9,11))
print(divi(8,3))
