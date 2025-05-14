hora_n = int(input("Quantas horas normais o trabalhador trabalhou? "))
hora_e = int(input("Quantas horas extras o trabalhador trabalhou? "))

hora_trabalhadas = hora_n * 10
hora_extra = hora_e * 15

salario_bruto = hora_trabalhadas + hora_extra

salario_liquido1 = 10*salario_bruto/100
salario_liquido2 = salario_bruto - salario_liquido1

print("O salario bruto desse trabalhador é igual á ", salario_bruto)
print("O salario liquido desse trabalhador é igual á ", salario_liquido2 )