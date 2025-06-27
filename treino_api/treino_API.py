import requests

# Configurações da API
api_key = "f768abe07d3f45dfb22211103252606"
url_api = "http://api.weatherapi.com/v1/current.json"

# Função para buscar dados da API para uma cidade
def buscar_dados(cidade):
    parametros = {
        "key": api_key,
        "q": cidade,
        "lang": "pt"
    }
    try:
        resposta = requests.get(url_api, params=parametros, timeout=5)
        resposta.raise_for_status()  # Lança erro para códigos 4xx/5xx
        return resposta.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados para {cidade}: {e}")
        return None

# Função para mostrar as informações da cidade
def mostrar_dados(cidade, dados):
    try:
        temp = dados['current']['temp_c']
        sensacao = dados['current']['feelslike_c']
        condicao = dados['current']['condition']['text']
        vento = dados['current']['wind_kph']

        print(f"\n--- {cidade} ---")
        print(f"Temperatura: {temp}°C")
        print(f"Sensação térmica: {sensacao}°C")
        print(f"Condição do tempo: {condicao}")
        print(f"Vento: {vento} km/h")
    except (KeyError, TypeError):
        print(f"Erro ao exibir dados para {cidade}.")

# Função para comparar temperaturas entre as cidades
def comparacao(cidade1, dados1, cidade2, dados2):
    try:
        temp1 = dados1['current']['temp_c']
        temp2 = dados2['current']['temp_c']

        print("\n--- Comparação ---")
        if temp1 > temp2:
            print(f"🔥 {cidade1} está mais quente ({temp1}°C) que {cidade2} ({temp2}°C).")
        elif temp1 < temp2:
            print(f"🔥 {cidade2} está mais quente ({temp2}°C) que {cidade1} ({temp1}°C).")
        else:
            print(f"🌡️ {cidade1} e {cidade2} estão com a mesma temperatura: {temp1}°C.")
    except (KeyError, TypeError):
        print("Erro ao comparar temperaturas.")

# Entrada do usuário
cidade1 = input("Digite a primeira cidade: ")
cidade2 = input("Digite a segunda cidade: ")

# Buscar e exibir dados
dados1 = buscar_dados(cidade1)
dados2 = buscar_dados(cidade2)

if dados1 and dados2:
    mostrar_dados(cidade1, dados1)
    mostrar_dados(cidade2, dados2)
    comparacao(cidade1, dados1, cidade2, dados2)
else:
    print("\nNão foi possível obter os dados de uma ou ambas as cidades.")
