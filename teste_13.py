num=int(input('digite um numero'))
#testagem se é primo
div=0
for x in range(1,num+1):
  resto=num%x
  if resto == 0:
      div=div+1

#exibição do resiltado
if div==2:
    print('{} é primo'.format(num))
else:
     print('{} não é primo'.format(num))