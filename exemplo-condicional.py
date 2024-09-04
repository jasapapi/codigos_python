valor = int(input("Informe um valor numérico: "))

if valor>20:
    print(f"O número {valor} é maior que 20 \n")
elif valor>=10 and valor<=20:
    print(f"O número {valor} está entre 10 e 20 \n")
else:
    print(f"O número {valor} é menor que 10 \n")