def verificar_idade(idade):
    if idade >= 18:
        print("Acesso permitido")
    else:
        print("Acesso negado")

idade_utilizador = int(input("Indique sua idade: "))

verificar_idade(idade_utilizador)
