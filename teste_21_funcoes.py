def Contador_Letras(listaPalavras):
    contador = []
    for x in listaPalavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

if __name__=='__main__':
    lista=['chimpanzé', 'orangotango','gorila']
    print(Contador_Letras(lista))

def Teste():
    return 'Olá, isso é um teste'