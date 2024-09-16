import random
num = 0

nA = random.randint(1, 100)

ten_max = 5
ten = 0

while ten < ten_max:
    num = int(input(f"Digite o palpite {ten + 1}: "))
    ten += 1
    if num > nA:
        print(f"{num} é maior que o número aleatório.")
    elif num < nA:
        print(f"{num} é menor que o número aleatório.")
    elif num == nA:
        print(f"{num} é igual ao número aleatório.")

print(f"O número aleatório é {nA}")