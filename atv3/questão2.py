ano = int(input("Digite um ano: "))

if ano % 400 == 0 or ano % 4 == 0 or ano % 100 == 1:
    print (f"Esse ano é bissexto.")

else:
    print (f"Esse ano não é bissexto.")