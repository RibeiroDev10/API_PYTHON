# get_token.py

token = "Bearer "

with open("token.txt", "r") as file:
    token = token + file.read()
