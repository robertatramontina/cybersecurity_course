utilizador = {
    "nome": "admin", 
    "tentativas_falhas": 2,
    "ativo": True
}

#aceder a um valor
print(utilizador["nome"])

utilizador["tentativas_falhas"] += 1

utilizador["ultimo_login"] = "2025-10-16"

print(utilizador)

del utilizador["ultimo_login"]

print(utilizador)
