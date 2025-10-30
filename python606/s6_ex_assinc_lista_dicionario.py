import getpass

lista_senhas = []
count_senha = 1
dic_senhas = {
    "fracas": 0, 
    "fortes": 0
}

while len(lista_senhas) <= 4:
        senhas = getpass.getpass(f"Digite sua senha de número {count_senha}: ")
        lista_senhas.append(senhas)
        count_senha += 1
        
        if len(senhas) < 8:
            print("Senha Fraca")
            dic_senhas["fracas"] += 1
           
        else:
            print("Senha Forte")
            dic_senhas["fortes"] += 1

#print(lista_senhas)        
print(f"Foram registadas {dic_senhas['fracas']} senha(s) fraca(s) e {dic_senhas['fortes']} senha(s) fortes(s)")                           

###################################################  
acesso = "tentativa de acesso do utilizador root"
if "root" in acesso.lower():
    print("Acesso root identificado")
