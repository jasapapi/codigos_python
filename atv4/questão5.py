import random

quant1 = 0
quant2 = 0
quant3 = 0
quant4 = 0
quant5 = 0
quant6 = 0


for contador in range(10):
    num = random.randint(1, 6)
    print(f"{num}")
    
    if num == 1:
        quant1 += 1

    if num == 2:
        quant2 += 1

    if num == 3:
        quant3 += 1

    if num == 4:
        quant4 += 1

    if num == 5:
        quant5 += 1

    if num == 6:
        quant6 += 1

print(f"Quantidade de vezes que o número 1 foi sorteado: {quant1}")
print(f"Quantidade de vezes que o número 2 foi sorteado: {quant2}")
print(f"Quantidade de vezes que o número 3 foi sorteado: {quant3}")
print(f"Quantidade de vezes que o número 4 foi sorteado: {quant4}")
print(f"Quantidade de vezes que o número 5 foi sorteado: {quant5}")
print(f"Quantidade de vezes que o número 6 foi sorteado: {quant6}")
