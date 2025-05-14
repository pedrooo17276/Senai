print(100*"-")
salario = float(input("Insira seu salário fixo: "))
vendas = int(input("Insira o total de vendas realizadas: "))

porcentagem = (4 / 100) * salario
comissao = porcentagem * vendas
vt = salario + comissao
print("-"*100)
print(f"O valor total com as comissões foi de {vt }")
print(f"O valor da comissão foi de: {comissao}")
print("-"*100)