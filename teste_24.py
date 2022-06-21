#utlizando try
try:
    divisao=10/0
except ZeroDivisionError:
    print('Não é possivel dividir por 0')

#versao mais geral   
try:
    divisao=10/0
except ArithmeticError:
    print('Houve um erro aritimético')

# outro exemplo
colecao=[1,2,3]
try:
    print(colecao[4])
except IndexError:
    print('A posição pedida não existe')

#desconhecido:
try:
    print(colecao[4])
except Exception as ex:
    print('Erro desconhecido. Erro: ({})'.format(ex))

#teste com else:
try:
    print(colecao[2])
except Exception as ex:
    print('Erro desconhecido. Erro: ({})'.format(ex))
else:
    print('É executado com sucesso')
#pt 2
try:
    print(colecao[5])
except Exception as ex:
    print('Erro desconhecido. Erro: ({})'.format(ex))
else:
    print('É executado com sucesso')

#finally sempre executa algo:
try:
    arquivo= open('teste_22_extra.txt','r')
    texto=arquivo.read()
    print(colecao[5])
    arquivo.close() # <---- não será executado
except Exception as ex:
    print('Erro desconhecido. Erro: ({})'.format(ex))
else:
    print('É executado com sucesso')
finally:
    print(texto)
    print('O arquivo está sendo fechado')
    arquivo.close() # <---- será executado