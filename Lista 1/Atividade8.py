altura_pessoa = float(input("Insira sua altura em metros: "))
sombra_pessoa = float(input("Insira o seu comprimento da sua sombra em metros: "))
sombra_predio = float(input("Insira o seu comprimento da sombra do prédio em metros: "))
altura_predio = float(input("Insira a altura do predio em metros: "))

altura_predio = (sombra_predio * altura_pessoa) / sombra_pessoa

print(f"A altura do prédio é: {altura_predio:.2f} metros")
