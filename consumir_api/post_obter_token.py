# post_obter_token.py

import requests

# from pprint import pprint

# _print = print
# print = pprint

url = "http://127.0.0.1:3001/tokens"

user_data = {
    "password": "123456",
    "email": "rafael@teste.com.br",
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Recebi uma resposta de sucesso da minha API
    # Sucesso
    print(response.status_code)
    print(response.reason)

    response_data = response.json()
    token = response_data["token"]

    with open("token.txt", "w") as file:
        file.write(token)

else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
