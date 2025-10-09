idade1 = int(input("Informe a primeira idade: "))

idade2 = int(input("Informe a segunda idade: "))

if idade1 >= 18 and idade2 >= 18:
    print("Acesso autorizado a ambos utilizadores")
elif idade1 >= 18 or idade2 >= 18:
    print("Acesso autorizado a apenas um utilizador")
else:
    print("Acesso negado a ambos utilizadores")


"""
Linguagem natural:

O programa recebe duas idade
Se ambas as idades forem maiores que 18 anos, concede acesso a ambos utilizadores,
se apenas uma das idades for maior ou igual a 18, concede acesso a apenas um utilizador,
ou então, se ambas forem menores que 18 anos, nao concede acesso aos utilizadores.

Pseudo-código:

INICIO
    Ler idade1
    Ler idade2

    SE idade1 >= 18 E idade2 >= 18 ENTÃO
        Escrever("Acesso concedido a ambos utilizadores")

    SENÃO SE idade1 >= 18 OU idade2 >= 18 ENTÃO
        Escrever("Acesso concedido a apenas um utilizador")

    SENÃO
        Escrever("Acesso negado a ambos os utilizadores")
FIM
"""