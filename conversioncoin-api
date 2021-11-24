import requests

url = 'https://api.exchangerate-api.com/v6/latest'

req = requests.get(url)

if req == '200':
  valor_reais = float(input('Informe o valor em reais a ser convertido: \n'))
  cotacao = dados['rates']['BRL']
  print(f'R${valor_reais} em dólar valem US${(valor_reais / cotacao):.2f}')
