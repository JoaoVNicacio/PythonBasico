#obtenção de valores
a=int(input('digite o primeiro valor '))
b=int(input('digite o segundo valor '))
c=int(input('digite o terceiro valor '))

#checara se a é o maior
if a>b and a>c:
    print('{} é maior que {} e {}'.format(a,b,c))
#checara se b é o maior
elif b>c and b>c:
    print('{} é maior que {} e {}'.format(b,a,c))
#checara se c é o maior
elif c>b and c>a:
    print('{} é maior que {} e {}'.format(c,a,b))
#checara se todos são iguais
elif a==b and b==c:
    print('{} é igual a {} e {}'.format(a,b,c))
#em caso de erro
else:
    print('ocorreu um erro')
