arquivo = open ('teste_22_extra.txt','a')
arquivo.write('primeira linha')
arquivo.write('\nsegunda linha')
arquivo.write('\nterceira linha')
arquivo.close()

#utilizando uma função
def Escrever_arquivo (texto) :
    arquivo = open ('teste_22_extra_2.txt','w')
    arquivo.write(texto)
    arquivo.close()

def Atualizar_arquivo (texto) :
    arquivo = open ('teste_22_extra_2.txt','a')
    arquivo.write(texto)
    arquivo.close()

def Ler_arquivo (nomeArquivo):
    arquivo = open(nomeArquivo,"r")
    texto=arquivo.read()
    print(texto)

#copiar e mover com shutil:
def Copiar_arquivo(nome):
    import shutil
    shutil.copy(nome)

def Mover_arquivo(nome):
    import shutil
    shutil.move(nome)

if __name__ =='__main__':
    Escrever_arquivo ('1a linha\n')
    for i in range (2,10):
        Atualizar_arquivo('{}a linha\n'.format(i))
    Ler_arquivo('teste_22_extra_2.txt')
    Copiar_arquivo('teste_22_extra_2.txt')
    Mover_arquivo('teste_22_extra.txt')


#utilizando diretorios
#exemplo com o desktop: 
#diretorio= 'C:\Users\(nome do usuario no windows)\Desktop\(nomearquivo)'
#open ('diretorio','w')

#batizando posteriormente o arquivo:
def Escrever_arquivo2 (nome,texto) :
    arquivo = open (nome,'w')
    arquivo.write(texto)
    arquivo.close()

def Atualizar_arquivo2 (nome,texto) :
    arquivo = open (nome,'a')
    arquivo.write(texto)
    arquivo.split('\n')
    arquivo.close()

if __name__ =='__main__':
    nomeArquivo=input('digite o nome do arquivo') 
    nomeArquivo=nomeArquivo +'.txt'
    Escrever_arquivo2 (nomeArquivo,'1a linha\n')
    for i in range (2,10):
        Atualizar_arquivo2(nomeArquivo,'{}a linha'.format(i))
    Ler_arquivo(nomeArquivo)

