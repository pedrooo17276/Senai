numero = int(input("Digite um número para ver sua tabuada: "))
# Cálculo e exibição da tabuada
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)