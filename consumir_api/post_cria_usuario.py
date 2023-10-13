# post_criar_usuario.py

import requests

# from pprint import pprint

# _print = print
# print = pprint

url = "http://127.0.0.1:3001/users"

user_data = {
    "nome": "Rafael Ribeiro",
    "password": "123456",
    "email": "rafael@teste.com.br",
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Recebi uma resposta de sucesso da minha API
    # Sucesso
    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
