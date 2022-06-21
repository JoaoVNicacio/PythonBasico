#teste 3 de classe
#ventilador: 
class Ventilador:

    def __init__(self):
        self.ligado = False
        self.potencia = 1
    
    def ligar(self):
        if self.ligado:
            self.ligado = False
        else:
            self.ligado = True

    def aumentar(self):
        if self.ligado:
            self.potencia += 1

    def diminuir(self):
        if self.ligado:
            self.potencia -= 1


#testando as funções
vent=Ventilador()
print('O aparelho está ligado? {}'.format(vent.ligado))
vent.ligar()
print('O aparelho está ligado? {}'.format(vent.ligado))
print('qual a potência? {}'.format(vent.potencia))
vent.aumentar()
print('qual a potência? {}'.format(vent.potencia))
vent.aumentar()
print('qual a potência? {}'.format(vent.potencia))
vent.diminuir()
print('qual a potência? {}'.format(vent.potencia))



