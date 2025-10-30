import ipaddress

def mask_ip(ip: str) -> str:
    """
    Mascara um IP substituindo os octetos do meio por ***.
    :param ip: Endereço IP (ex: "192.168.0.10")
    :return: IP mascarado ou "IP inválido"
    """
    try:
        ip_obj = ipaddress.ip_address(ip.strip())
        partes = str(ip_obj).split(".")
        return f"{partes[0]}.***.***.{partes[3]}"
    
    except:
        return "IP inválido"
