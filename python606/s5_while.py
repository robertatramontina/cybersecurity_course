import time

tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    utilizador = input("Utilizador: ")
    password = input("Password: ")

    if utilizador == "admin" and password == "C!b3r@123":
        print("Acesso permitido ")
        break
    else:
        print("Acesso negado ")
        tentativas += 1
        print(f"Tentativas restantes: {max_tentativas - tentativas}")
        time.sleep(2) #atraso para mitigar força bruta

if tentativas == max_tentativas:
    print("Conta bloqueada por excesso de tentativas!")
