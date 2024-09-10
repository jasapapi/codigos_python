valor = float (input("Digite o  valor da sua compra: "))
par = float(input("Digite a quantidade de parcela (1 a 24): "))

if par > 12:
    print(f"O valor de cada parcela é de {6+(valor/par)} reais e o valor total é de {((6+(valor/par))*par)+((6+(valor/par))*par)*0.015} reais.")

else:
    print(f"O valor de cada parcela é de {valor/par} reais e o valor total é de {valor} reais.")