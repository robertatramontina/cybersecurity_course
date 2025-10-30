from typing import Dict

def gerar_relatorio(contagem):
    
    print("Tentativas de login suspeitas: \n")
    for ip, tentativas in contagem.items():
        if tentativas >= 3:
            print(f"IP {ip} -> {tentativas} tentativas de login falhadas")