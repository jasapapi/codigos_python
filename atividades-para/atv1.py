soma = 0 #Estamos inicializando a variável com o valor zero
total_pares = 0 # será responsável por contar todos os valores

for contador in range(50,71):
    if contador % 2 == 0:
        soma = soma + contador # soma += contador
        total_pares = total_pares + 1

print(f"A soma dos valores pares é {soma}")
print(f"A média dos pares é {soma/total_pares}")
print(f"O total de valores pares é {total_pares}")