#Atividade 1 
#A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo, uma fatia de presunto e uma rodela de hambúrguer. 
#Sabendo que cada fatia de queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, 
#faça um algoritmo em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades (em quilos) de queijo, presunto e carne necessários para compra.

sanduiches = int(input("Quantidade de sanduíches: "))
queijo = (sanduiches * 2 * 50) / 1000
presunto = (sanduiches * 1 * 50) / 1000
hamburguer = (sanduiches * 1 * 100) / 1000
print(f"Queijo: {queijo}kg, Presunto: {presunto}kg, Hambúrguer: {hamburguer}kg")
