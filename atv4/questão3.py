qtd = 0
qtde = 0


for contador in range (7): 
    temp = float(input(f"Digite a temperatura {contador + 1}: "))
    if temp >= 33.5:
        qtd += 1

    else:
        qtde += 1


print(f"Quantidade de temperatura iguais ou acima de 33.5 graus: {qtd}")
print(f"Quantidade de temperaturas abaixo de 33.5 graus: {qtde}")