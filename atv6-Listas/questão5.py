lista = []
valor_max = 5
val = 0

while val < valor_max:
    valor = int(input(f"Digite um valor {val + 1}: "))
    val += 1
       
    lista.append(valor)
print(f"Lista completa: {lista}")

for contador in lista:
    if contador % 3 == 0:
        lista.remove(contador)
print(f"Lista somente com os divisíveis por 3: {lista}")