import time
import getpass
import hashlib #criar hashes criptográficos


max_tentativas = 3
tentativas = 0

while tentativas < max_tentativas:
    utilizador = input("Digite seu utilizador: ") 
    password = getpass.getpass("Digite sua password: ")        #hash_input é variável que guarda o hash calculado da senha digitada para comparar com o hash armazenado 
                                                               #hashlib.sha256 aplica o algoritmo SHA-256 sobre os bytes da senha
    hash_input = hashlib.sha256(password.encode()).hexdigest() #password.encode() transforma o texto digitado em bytes
                                                                   
    if utilizador == "admin" and hash_input == "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4":
        print("Acesso permitido")
        break
    else:
        tentativas += 1
        restantes = max_tentativas - tentativas
        print(f"Credenciais incorretas: {restantes} tentativas restante")
        time.sleep(2)

        print("Excedeu todas as tentativas disponíveis. Sua conta foi BLOQUEADA!")
    

