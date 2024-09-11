qtd = 0

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

for contador in range (a,b):
    if contador % 7 == 0 and contador % 11 == 0:
        qtd += 1

print(f"Quantidade de números multiplos de 7 e 11 entre {a} e {b} é: {qtd}")