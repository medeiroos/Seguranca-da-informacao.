import re
import json
from urllib.request import urlopen

url = "http://ip-api.com/json/24.48.0.1"
resposta = urlopen(url)
dados = json.load(resposta)
ip = dados["query"]
cidade = dados["city"]
pais = dados["country"]
regiao = dados["region"]
org = dados["org"]
print("Detalhes do seu ip externo: "
      "\nIP:{}"
      "\nCIDADE: {}"
      "\nPAÍS: {}"
      "\nREGIÃO: {}"
      "\nORGANIZAÇÃO: {}".format(ip, cidade, pais, regiao, org))
