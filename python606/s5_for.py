ips = ["192.168.0.10", "192.168.0.11", "10.0.0.5", "172.16.0.3"]

for ip in ips:
    if ip.startswith("192.168."):
        print(f"{ip} pertence à rede interna.")
    else:
        print(f"{ip} é um acesso externo (verificar origem).")    