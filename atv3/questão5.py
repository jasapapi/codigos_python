hrs = float(input("Digite a sua carga horária: "))
valor = float(input("Digite quanto você ganha por hora: "))

if hrs > 40:
    print(f"Você receberá com um bônus: {(valor*40)+(((hrs-40)*valor)*0.5):.2f} reais.")

else:
    print(f"Você receberá {valor*hrs:.2f} reais.")