import requests

api_key = "f768abe07d3f45dfb22211103252606"
url_api = "http://api.weatherapi.com/v1/current.json"

cidade = input("Digite a cidade: ")

# parametros no formato dict de acordo com a documentação da API (nesse caso da wheater API é assim)
parametros = {
    "key": api_key,
    "q": cidade,
    "lang": "pt"

}

resposta = requests.get(url_api, params= parametros)

# print(resposta) para verificar o status code

# se a requisição der certo transforma os dados em um JSON
if resposta.status_code == 200:
    dados = resposta.json()
    
temp = dados['current']['temp_c']
condicao = dados['current']['condition']['text']

print(f"Temperatura: {temp}°C")
print(f"Condição do tempo: {condicao}")