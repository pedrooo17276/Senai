#Atividade 9 
#Um tonel de refresco é feito com 8 partes de água mineral e 2 partes de suco de maracujá. 
#Faça um algoritmo para calcular quantos litros de água e de suco são necessários para se fazer X litros de refresco (informados pelo usuário).
litros_água = float(input("Insira a quantidade de litros de água que você deseja: "))
litros_suco = float(input("Insira a quantidade de litros de suco que você deseja: "))

proporcao_agua = 8 / 10
proporcao_suco = 2 / 10
litros_agua = litros_refresco * proporcao_agua
litros_suco = litros_refresco * proporcao_suco

total = (litros_agua * litros_suco) / litros_refresco

print(f"A quandidade nescessarias para fazer o refresco é de: {total:.2f}")