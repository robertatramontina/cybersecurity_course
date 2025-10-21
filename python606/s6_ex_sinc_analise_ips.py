ips_suspeitos = ["192.168.10.5", "192.168.20.6", "10.10.10.10", "172.16.20.30"]

for i in ips_suspeitos:
    if i.startswith("10"):
        print(i)

utilizador = {
    "nome": "admin",
    "tentativas": 3, 
    "bloqueado": False 
}

if utilizador["tentativas"] >= 3:
    utilizador["bloqueado"] = True
    print(utilizador["nome"])
    print(utilizador["tentativas"])
    print(utilizador["bloqueado"])

log = "Tentativa de login do utilizador admin falhada"

if "falha" in log.lower():
    print("Palavra falha identificada")
    
    



        