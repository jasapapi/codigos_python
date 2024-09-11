qtd = 0
soma = 0

for contador in range (8): 
    list = int(input(f"Digite o número {contador + 1}: "))
    if list < 0:
        qtd += 1
    
    if list > 0:
        soma += list
        

print(f"Quantidade de números negativos: {qtd}")
print(f"Soma dos números positivos: {soma}")
