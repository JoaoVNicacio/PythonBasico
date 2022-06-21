numeros = [8, 9, 10]
animais = ['lontra', 'cachorro']
print(numeros)
print(animais)
print(numeros[1])
print(animais[0])

# exibição de todos os elementos individualmente
for i in numeros:
    print(i)

# min e max com numeros
print(max(numeros))
print(min(numeros))

# min e max com strings
print(max(animais))
print(min(animais))

#procura dentro de um array/list
if 'lobo' in animais:
    print('há um lobo na lista')
else:
    print('não há um lobo na lista')

#procura dentro de um array/list e adiciona caso não haja 
novoAnimal= input('Digite um animal')
if novoAnimal in animais:
    print('há um {} na lista'.format(novoAnimal))
else:
    print('não há um {} na lista, vamos adicionar'.format(novoAnimal))
    animais.append(novoAnimal)
    print(animais)

#multiplicação de qtdade
numerosNovo= numeros*2
print(numerosNovo)

#teste com pop
novaLista=[1,2,3,4]
novaLista.pop()
novaLista.pop(0)
print(novaLista)

#teste com remove
animais.remove('cachorro')
print(animais)

#teste com sort
numerosNovo.sort()
print(numerosNovo)

#teste com reverse
numerosNovo.reverse()
print(numerosNovo)