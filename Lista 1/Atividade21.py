salario_minimo = float(input("Digite o valor do salário mínimo: "))
salario_bruto = float(input("Digite o salário bruto do funcionário: "))

if salario_minimo <= 0 or salario_bruto <= 0:
    print("Erro: Os valores de salário mínimo e salário bruto devem ser maiores que zero.")
    exit()  

numero_salarios_minimos = salario_bruto / salario_minimo

# Mostrando o resultado
print(f"O funcionário ganha {numero_salarios_minimos:.2f} salários mínimos.")