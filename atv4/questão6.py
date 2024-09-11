soma = 0
num = int(input("Digite um número: "))

for contador in range (1,num):
    if num % contador == 0:
        soma += contador

if soma == num:
    print (f"{num} é um número perfeito.")

else:
    print (f"{num} é um número imperfeito.")