a=int(input('1º bimestre'))
b=int(input('2º bimestre'))
c=int(input('3º bimestre'))
d=int(input('4º bimestre'))

#checagem de validade indivual
if a > 10 and a < 0:
    print('1ª nota inválida')
elif b > 10 and b < 0:
    print('2ª nota inválida')
elif c > 10 and c < 0:
    print('3ª nota inválida')
elif d > 10 and d < 0:
    print('4ª nota inválida')  
#exibição caso não haja erro
else:
    print('a média é de {} '.format(+(a+b+c+d)/4))