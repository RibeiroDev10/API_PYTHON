# post_criar_aluno.py

import requests
from get_token import token

# from pprint import pprint

# _print = print
# print = pprint

url = "http://127.0.0.1:3001/alunos"

headers = {"Authorization": token}

aluno_data = {
    "nome": "Rafael 2",
    "sobrenome": "Ribeiro 2",
    "email": "rafael@avodh.com",
    "idade": "20",
    "peso": "90.10",
    "altura": "1.87",
}

response = requests.post(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    # Recebi uma resposta de sucesso da minha API
    # Sucesso
    print(response.status_code)
    print(response.reason)

    response_data = response.json()

else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
