

registos = [
    {"ip": "192.168.0.10", "utilizador": "ana", "sucesso": False},
    {"ip": "192.168.0.11", "utilizador": "bruno", "sucesso": True},
    {"ip": "192.168.0.10", "utilizador": "ana", "sucesso": False},
    {"ip": "192.168.0.12", "utilizador": "carlos", "sucesso": False},
    {"ip": "192.168.0.13", "utilizador": "diana", "sucesso": True},
    {"ip": "192.168.0.12", "utilizador": "carlos", "sucesso": False},
    {"ip": "192.168.0.12", "utilizador": "carlos", "sucesso": False}
    ]

"""
neste exercício utilizamos uma lista fictícia de ips e utilizadores 
para servir de informação à execução do script.
"""

contagem = {}

"""
O dicionário contagem{} foi incialmente posto dentro da função
contar_falhas_por_ips, no entanto, para que pudesse ser
utilizada nas demais funções, posteriormente foi colocada 
fora, tornando-se uma variável global.
"""

def contar_falhas_por_ip(registos):
        
    for registo in registos:
        if registo["sucesso"] == False:
            ip = registo["ip"]
            if ip not in contagem:
                contagem[ip] = 1
            else:
                contagem[ip] += 1

"""
O for percorre cada registo do dicionário que está dentro da lista registos,
identifica a chave Sucesso e lê o valor atribuido, se falso,
inicia um outro dicionário onde será contabilizado o número de tentativas de login
provenientes daquele mesmo IP.
"""

def gerar_relatorio():
    print("Tentativas de login suspeitas: \n")
    for ip, tentativas in contagem.items():
        if tentativas >= 3:
            print(f"IP {ip} -> {tentativas} tentativas de login falhadas")

"""
Para gerar o relatório, novamente utilizo o ciclo for percorrer as tentativas realizadas
por cada IP e imprimir o IP e a respectiva quantidade de tentativas falhadas se igual ou
maior que três.
"""

def main():
    contar_falhas_por_ip(registos)
    gerar_relatorio()

"""
A função main engloba e chama as demais função
a serem executadas na ordem desejada.
"""

main()

