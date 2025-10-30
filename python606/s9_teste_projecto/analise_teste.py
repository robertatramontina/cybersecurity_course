from typing import Dict, List, TypedDict

"""
O dicionário contagem{} foi incialmente posto dentro da função
contar_falhas_por_ips, no entanto, para que pudesse ser
utilizada nas demais funções, posteriormente foi colocada 
fora, tornando-se uma variável global.
"""

def contar_falhas_por_ip(registos):
 
    contagem =  {}    
    for registo in registos:
        if registo["sucesso"] == False:
            ip = registo["ip"]
            if ip not in contagem:
                contagem[ip] = 1
            else:
                contagem[ip] += 1
    
    return contagem