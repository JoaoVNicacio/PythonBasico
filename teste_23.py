#chamando as ferramentas para horarios
from datetime import date, datetime, time, timedelta
#exibindo no padrão do inglês:
dataDeHoje= date.today()
print(dataDeHoje)
#exibindo no padrão do português:
print(dataDeHoje.strftime('%d/%m/%y'))
#com o ano completo:
print(dataDeHoje.strftime('%d/%m/%Y'))
#conferindo os tipos:
dataStr=dataDeHoje.strftime('%d/%m/%Y')
print(type(dataStr))
print(type(dataDeHoje))
#utilzando horarios:
def Hora ():
    horario = time(hour = 15, minute= 10, second = 37)
    return horario.strftime('%H:%M:%S')

#utilizando datetime e weekday:
def DataHoraAtual():
    horario=datetime.now()
    return horario.strftime('data: %d/%m/%Y hora: %H:%M:%S')

# usando weekday:
def DiaDeHoje():
    horario=datetime.now()
    dia= horario.weekday()
    tuplaDias=('Segunda','Terça','Quarta', 'Quinta','Sexta', 'Sábado','Domingo')
    return tuplaDias[dia]

def DataCompleta():
    horario=datetime.now()
    return horario.strftime('%c')

#trasnformando string em datas:
def TransformaData():
    dataStr='13/05/2022'
    conversao=datetime.strptime(dataStr,'%d/%m/%Y')
    return conversao

#utilizando timedelta:
def DiferencaData():
    horario=datetime.now()
    novaData= horario + timedelta(days=365,hours=5,minutes=15)
    return novaData

if __name__=='__main__':
    horario= Hora()
    print(horario)
    dataHora=DataHoraAtual()
    print(dataHora)
    dia=DiaDeHoje()
    print(dia)
    dataCompleta=DataCompleta()
    print(dataCompleta)
    dataConvertida=TransformaData()
    print(dataConvertida)
    dataDelta=DiferencaData()
    print(dataDelta)