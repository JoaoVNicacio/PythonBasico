#Criando erros personalizados:
class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        nota= int(input('Digite uma nota de 0 a 10: '))
        print(nota)
        if nota > 10:
            raise InputError('O número não pode ser maior que 10')
        elif nota < 0:
            raise InputError('O número não pode ser menor que 0')
        break

    except ValueError:
        print('Digite um valor que seja um número.')
    except InputError as ex:
        print(ex)