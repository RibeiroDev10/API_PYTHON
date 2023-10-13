# post_criar_aluno.py

import requests
from get_token import token
from requests_toolbelt import MultipartEncoder
from mimetypes import MimeTypes

mimetypes = MimeTypes()

nome_arquivo = "cadeira_nova.jpg"

mimetype_arquivo = mimetypes.guess_type(nome_arquivo)[0]

multipart = MultipartEncoder(
    fields={
        "aluno_id": "2",
        "foto": (nome_arquivo, open(nome_arquivo, "rb"), mimetype_arquivo),
    }
)

print("MULTIPART: ", multipart)
print()

url = "http://127.0.0.1:3001/fotos"

headers = {"Authorization": token, "Content-Type": multipart.content_type}

response = requests.post(url=url, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    # Recebi uma resposta de sucesso da minha API
    # Sucesso
    print(response.status_code)
    print(response.reason)

    response_data = response.json()

    print(response_data)

else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
