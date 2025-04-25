#Atividade 8 
#Num dia de sol, você deseja medir a altura de um prédio, porém, a trena não é suficientemente longa. 
#Assumindo que seja possível medir sua sombra e a do prédio no chão, e que você lembre da sua altura, 
#faça um algoritmo para ler os dados necessários e calcular a altura do prédio.
altura_pessoa = float(input("Insira sua altura em metros: "))
sombra_pessoa = float(input("Insira o seu comprimento da sua sombra em metros: "))
sombra_predio = float(input("Insira o seu comprimento da sombra do prédio em metros: "))
altura_predio = float(input("Insira a altura do predio em metros: "))

altura_predio = (sombra_predio * altura_pessoa) / sombra_pessoa

print(f"A altura do prédio é: {altura_predio:.2f} metros")
