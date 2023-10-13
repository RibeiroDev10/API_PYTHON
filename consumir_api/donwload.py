import requests

url = ""

nome_arquivo = url.split("/")[-1]

response = requests.get(url)
