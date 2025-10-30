import time
import ipaddress

l_ips = []
l_black = ["10.10.10.10", "192.168.10.10", "172.31.10.10"]
report_black = []
report_clear = []

def obter_lista_ips():
    while len(l_ips) <= 4: 
        ips = input("Digite o IP que deseja consultar (Exemplo: 10.0.0.0): ")
        if ips == "":
            print("IP não foi digitado. Tente outra vez")
            time.sleep(1)
            continue

        try:
            ipaddress.ip_address(ips)  # Valida o formato do IP
            l_ips.append(ips)
        except ValueError:
            print("IP inválido! Digite no formato correto (ex: 192.168.0.1).")
            time.sleep(1)

def verificar_bloqueio(l_ips, l_black):
    for ip in l_ips:
        if ip in l_black:
            report_black.append(ip)
        else:
            report_clear.append(ip)

def gerar_relatorio(report_black, report_clear):
    if not report_black:
        report_black = "Nenhum dos IPs consultados encontra-se bloqueado."
    if not report_clear:
        report_clear = "Nenhum dos IPs consultados encontra-se autorizado."
    print()    
    print("*************************************")
    print("Relatório de IPs bloqueados: ")
    print(report_black)
    print("*************************************")
    print("Relatório de IPs autorizados: ")
    print(report_clear)
          
def main():
    obter_lista_ips()
    verificar_bloqueio(l_ips, l_black)
    gerar_relatorio(report_black, report_clear)

main()
    
        
