calcular_total(moedas):

moedas = ('moedas_5_centavos') * 0.05 +
moedas = ('moedas_10_centavos') * 0.10 +
moedas = ('moedas_25_centavos') * 0.25 +
moedas = ('moedas_50_centavos') * 0.50 +
moedas = ('moedas_1_real') * 1.00 + 

moedas = {
moedas_1_centavo = int(input("Quantidade de moedas de 1 centavo: ")),
moedas_5_centavos = int(input("Quantidade de moedas de 5 centavos: ")),
moedas_10_centavos = int(input("Quantidade de moedas de 10 centavos: ")),
moedas_25_centavos = int(input("Quantidade de moedas de 25 centavos: ")),
moedas_50_centavos = int(input("Quantidade de moedas de 50 centavos: ")),
moedas_1_real = int(input("Quantidade de moedas de 1 real: "))
}
total = calcular_total(moedas):
print(f"Valor total economizado: R$ {total:.2f}")

