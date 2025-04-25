#Atividade 6
#A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: lata de 350 ml, garrafa de 600 ml e garrafa de 2 litros. 
#Se um comerciante compra uma determinada quantidade de cada formato, faça um algoritmo para calcular quantos litros de refrigerante ele comprou.
latas = int(input("Quantas latas de 350ml você comprou?: "))
garrafas = int(input("Quantas garrafas de 600ml você comprou?: "))
litros = int(input("Quantas garrafas de 2 litros você comprou?: "))

lata_ml = latas*350
garrafa_ml = garrafas*600
garrafa_litro = litros*2000

soma = lata_ml + garrafa_ml + garrafa_litro
print(f"Ele comprou {soma}ml de refigerante")