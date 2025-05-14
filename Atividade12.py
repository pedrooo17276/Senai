#Atividade 12
#Faça um algoritmo que receba dois números, calcule e mostre a divisão do primeiro número pelo segundo. 
#Sabe-se que o segundo número não pode ser zero, portanto não é necessário se preocupar com validações.
soma = 0 
n = 3 

for i in ranger (1, n + 1):
    numero = float(input(f"Digite o {i}:" ))
    soma += numero

multiplicacao = soma / n 

print("A média dos números digitados é:", multiplicacao)



