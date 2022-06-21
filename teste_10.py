a=int(input('1º bimestre'))
b=int(input('2º bimestre'))
c=int(input('3º bimestre'))
d=int(input('4º bimestre'))

#checagem de validade
if a<= 10 and a >= 0 and b<= 10 and b >= 0 and c<= 10 and c >= 0 and d<= 10 and d >= 0:
    print('a média é de {} ' .format(+(a+b+c+d)/4))
else:
    print('foi informada alguma nota inválida')