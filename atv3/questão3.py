idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Criança")

if idade >= 12 and idade < 18:
    print("Adolescente")

if idade >= 18 and idade < 60:
    print("Adulto")

if idade > 60:
    print("Idoso")
