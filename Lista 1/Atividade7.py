moedas = {
0.01: int(input("Moedas de 1 centavo: ")),
0.05: int(input("Moedas de 5 centavos: ")),
0.10: int(input("Moedas de 10 centavos: ")),
0.25: int(input("Moedas de 25 centavos: ")),
0.50: int(input("Moedas de 50 centavos: ")),
1.00: int(input("Moedas de 1 real: "))
}
total = sum(valor * qtd for valor, qtd in moedas.items())
print(f"O valor total economizado em reais é de: R${total}")