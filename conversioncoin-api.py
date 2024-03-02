import requests

url = "https://economia.awesomeapi.com.br/json/"

def converte_moeda():
    print("Moedas para conversao: BRL, USD, EUR, BTC")
    moeda_ori = str(input("Digite a moeda origem de conversao: ")).upper()
    moeda_dest = str(input("Digite a moeda destino de conversao: ")).upper()
    valor = float(input("Digite o valor a ser convertido: "))

    try:
        moedas = f"last/{moeda_ori}-{moeda_dest}"
        response = requests.get(url+moedas).json()
    except:
        converte_moeda()
    finally:
        data_find = f"{moeda_ori}{moeda_dest}"
        data = response.get(data_find)
        
        high = data.get('high')
        low = data.get('low')

        avr = (float(high) + float(low)) / 2
        conversion = round(valor * avr, 2)

        return f"\nA conversão realizada foi {data.get('name')} resultando o valor de {conversion} {data.get('codein')}.\nCotação realizada baseada na data {data.get('create_date')}"
   
