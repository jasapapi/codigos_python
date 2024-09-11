mv = int(input("Informe o valor 1: "))

for contador in range (2, 6): 
    valor = int(input(f"Informe o valor {contador}: "))
    if valor > mv:
        mv = valor
    
print(f"O maior valor é: {mv}")