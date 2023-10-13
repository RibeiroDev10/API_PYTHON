# post_criar_aluno.py

import requests
from get_token import token

# from pprint import pprint

# _print = print
# print = pprint

url = "http://127.0.0.1:3001/alunos"

headers = {
    #    "Authorization": token
}

aluno_data = {
    #     "nome": "Rafael",
    #     "sobrenome": "Ribeiro",
    #     "email": "rafael@teste.com",
    #     "idade": "20",
    #     "peso": "90.10",
    #     "altura": "1.87",
}

response = requests.get(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    # Recebi uma resposta de sucesso da minha API
    # Sucesso
    print(response.status_code)
    print(response.reason)

    response_data = response.json()

    for aluno in response_data:
        print(aluno["nome"])
        print(aluno["sobrenome"])

else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
