#Função com retorno

def somar( num1, num2):
    resultado = num1 + num2
    return resultado #devolvendo o valor para quem chamou a função

print(somar(20,6))

#Função sem retorno
def multiplicar (valor1, valor2):
    resultado = valor1 * valor2
    print(resultado)

multiplicar(6,8)