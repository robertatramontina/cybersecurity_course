max_tentativas = 5
n_tentativas = int(input("Informe a quantidade de tentativas de login: "))

if n_tentativas >= max_tentativas:
    print("Conta bloqueada.")
else:
    restantes = max_tentativas - n_tentativas
    print("Você ainda tem", restantes, "tentativa(s) de login.")
