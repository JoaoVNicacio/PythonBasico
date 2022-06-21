#testando sets
num={1,3,5,7,9}
print(type(num))
print(num)
#testando add e funcionalidades
#sets não repetem itens!
num2={1,3,3,5,7,7,9}
print(num2)
num2.add(11)
print(num2)
#testando discard
num3={1,2,3,4,10}
num3.discard(1)
print(num3)
#testando union
numMix= num2.union(num3)
print(numMix)
#testando intersection
numCom=num2.intersection(num3)
print(numCom)
#testando difference
numDif=num2.difference(num3)
numDif2=num3.difference(num2)
print(numDif)
print(numDif2)
#teste com symmetric diference
numSimDif=num2.symmetric_difference(num3)
print(numSimDif)
#teste com subset
numSub=num.issubset(num2)
print(numSub)
numSub2=num2.issubset(num)
print(numSub2)
#teste com superset
numSup=num2.issuperset(num)
print(numSup)
numSup2=num.issuperset(num2)
print(numSup2)
#conversao para lista
animais1=['gato', 'cachorro', 'lontra']
animais2=set(animais1)
print(animais1)
print(animais2)