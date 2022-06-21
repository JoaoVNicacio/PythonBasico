a=int(input('qual o número desejas saber se é impar ou par?'))
#checagem
if a % 2 == 0:
    print('{} é par'.format(a))
elif a % 2 == 1:
    print('{} é impar'.format(a))
else:
    print('houve um erro')