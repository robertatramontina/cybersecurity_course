import getpass
 

def validar_credenciais(user, password):
    return user == "admin" and password == "1234"

def verificar_tentativas(tentativas):
    if tentativas >= 3:
        return "Bloqueado"
    else:
        return "Permitido"
    
def main():
    tentativas = 0
    while tentativas < 3:
        user = input("Utilizador: ")
        password = input("Password: ")
        if validar_credenciais(user, password):
            #print("Acesso permitido")
            break
        else:
            tentativas += 1
            print(f"Tentativa {tentativas}/3 inválida.")
    print(verificar_tentativas(tentativas))

main()