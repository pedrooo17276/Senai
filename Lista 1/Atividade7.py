moedas = {
moedas_1_centavo = int(input("Quantidade de moedas de 1 centavo: ")),
moedas_5_centavos = int(input("Quantidade de moedas de 5 centavos: ")),
moedas_10_centavos = int(input("Quantidade de moedas de 10 centavos: ")),
moedas_25_centavos = int(input("Quantidade de moedas de 25 centavos: ")),
moedas_50_centavos = int(input("Quantidade de moedas de 50 centavos: ")),
moedas_1_real = int(input("Quantidade de moedas de 1 real: "))
}
total = sum(valor * qtd for valor, qtd in moedas.items())
print(f"Valor total economizado: R$ {total}")

