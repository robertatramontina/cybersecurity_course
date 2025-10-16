lista_alerta = []
total_falhas = 0

while True: 
    alerta = input("Insira seu alerta ou digite sair para finalizar o programa: ")
    
    if alerta == "":
        print("O alerta não pode estar vazio. Tente novamente.")
        continue

    if alerta.lower() == "sair":
        break
    
    lista_alerta.append(alerta)

    total_falhas = 0
    for i in lista_alerta:
        i_normalizado = i.lower().replace(" ", "")
        if i_normalizado == "101" or "falha101" in i_normalizado:
            total_falhas += 1    

print(f"Lista de alertas registados: {len(lista_alerta)}") 
print(f"O total de falhas selecionado é de: {total_falhas}") 


