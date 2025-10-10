limite = 5
n_tentativas = int(input("Informe a quantidade de tentativas de login: "))

if n_tentativas < limite:
    restantes = limite - n_tentativas
    print("Você ainda tem", restantes, "tentativas de login.")
else:
    print("Conta bloqueada.")
