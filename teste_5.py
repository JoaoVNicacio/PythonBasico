
a=int(input('digite o primeiro valor '))
b=int(input('digite o segundo valor '))
if a>b:
    print('{} é maior que {}'.format(a,b))
elif a<b:
    print('{} é maior que {}'.format(b,a))
elif a==b:
    print('{} é igual a {}'.format(a,b))
else:
    print('ocorreu um erro')
