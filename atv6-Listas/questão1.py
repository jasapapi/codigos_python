lista = []

while True:
    valor = int(input("Digite um valor (negativo para encerrar): "))
    if valor < 0:
        break
    else:
        lista.append(valor)
print(lista)
print("encerrado")

for contador in lista:
    if contador % 2 == 0:
        lista.remove(contador)
print(lista)