qtd = 0

for contador in range(5):
    idade = int(input(f"informe a idade {contador + 1}: "))
    if idade >= 18:
        qtd += 1

print(f"Quantidade de pessoas com 18 anos ou mais: {qtd} ")