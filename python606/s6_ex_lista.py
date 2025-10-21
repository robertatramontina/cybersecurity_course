ips_bloqueados = ["192.168.0.10", "10.0.0.5", "172.16.0.2"]

print(ips_bloqueados[0]) #aceder a elementos da lista

ips_bloqueados.append("8.8.8.8") #adicionar um novo elemento

ips_bloqueados.remove("10.0.0.5") #remover um ip da lista

ips_bloqueados.sort() #ordenar IPs aqui cuidado

print(ips_bloqueados)
