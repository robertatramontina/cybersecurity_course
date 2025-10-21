def calcular_risco(tentativas):
    if tentativas >= 3:
        return "Conta bloqueada"
    else:
        return "Conta ativa"

n_tentativas = int(input("Informe o número de tentativas:"))

print(calcular_risco(n_tentativas))