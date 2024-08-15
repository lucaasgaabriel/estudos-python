import requests
import time

ceps = [''] #Digite aqui quais CEPs devem ser consultados

def busca_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'

    return requests.get(url).json()


for cep in ceps:
    response = busca_cep(cep)
    time.sleep(0.5) #Timeout entre uma consulta e outra para não sobrecarregar a API
    uf = response.get('uf')

    if uf == 'DF': #Teste de verificação se esse endereço está localizado no DF
        print(f'Esse CEP está localizado em {response.get('localidade')} - {response.get('uf')}')
    else:
        print(f'Esse CEP está localizado em {response.get('localidade')} - {response.get('uf')}')



