a=int(input('qual o número desejas saber se é impar ou par?'))
b=int(input('qual outro número desejas saber se é impar ou par?'))
#checagem
if a % 2 == 0 or b % 2 == 0:
    print('foi digitado um número par')
else:
    print('não foi digitado um número par')