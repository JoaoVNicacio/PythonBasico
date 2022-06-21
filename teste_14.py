for num in range(100): 
    #testagem se é primo
    div=0
    for x in range(1,num+1):
        resto=num % x
        if resto == 0:
            div+=1
        #exibição do resiltado
    if div==2:
            print(num)
        