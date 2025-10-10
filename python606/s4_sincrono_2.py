login = "admin"
senha_admin = "1234"

login_input = int(input("Informe seu login: "))

senha_input = int(input("Informe a sua senha: "))

if login == login_input and senha_admin == senha_input:
    print("Acesso autorizado")
else:
    print("Acesso negado")