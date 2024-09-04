name = (input("Informe seu nome: "))
sexo = (input("Informe seu sexo (F ou M): "))
est = (input("Informe seu estado civil: "))



if sexo=="F" and est=="Casada":
    tempo = (input ("Tempo de casada: "))
    input (f"{name} seu tempo de casada é de {tempo}.")
else:
    input(f"Obrigada {name} e até a próxima!")