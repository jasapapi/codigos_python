meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
soma = 0 

temp = []

for i in range(12):
    while True:
        temperatura = float(input(f"Digite a temperatura média de {meses[i]}: "))
        temp.append(temperatura)
        soma+=temperatura
        mA = soma/12
        break
print(f"Média anual: {mA:.2f} \n")

print("Lista de meses que possuem a média maior que a média anual: ")

for contador in range(12):
    if temp[contador] > mA:
        print(f"{meses[contador]}: {temp[contador]:.2f} ºc")