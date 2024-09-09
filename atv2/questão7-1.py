valor = float (input("Insira o valor: "))
forma = int(input(" 1 - Pix, dinheiro ou débito, recebe 15% de desconto\n 2 - À vista no cartão de crédito, recebe 10% de desconto\n 3 - Em duas vezes, preço normal sem juros\n 4 - Em três vezes, preço normal mais juros de 10%\n Escolha a forma de pagamento: "))

if forma == "1":
    print(f"O valor total com desconto é de {valor-(valor * 0.15):.2f} reais.")

if forma == "2":
    print(f"O valor total com desconto é de {valor-(valor * 0.10):.2f} reais.")

if forma == "3":
    print(f"O valor é de duas vezes de {valor/2:.2f} reais.")

if forma == "4":
    print(f"O valor é de três vezes de {(valor/3)+((valor/3)*0.10):.2f} reais.")