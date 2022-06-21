import requests
response = requests.get('https://viacep.com.br/ws/01001000/json/')
print('O código HTTP é: {} '.format(response.status_code))
print(response.text)
dadosCep=response.json
print(dadosCep['logradouro'])