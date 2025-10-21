log = "Tentativa de login falhada do utilizador admin"

if "falha" in log.lower():
    print("Alerta: possível tentativa de intrusão")

palavras = log.split() # Divisão e extração
print(palavras)

log_corrigido = log.replace("admin", "[oculto]")
print(log_corrigido)

