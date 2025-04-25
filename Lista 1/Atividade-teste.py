# Inicialização do estoque como um dicionário vazio
estoque = {}

print("Bem-vindo(a) conferidor(a) de estoque! Espero que esteja bem! Meu nome é Vitor. Vamos começar a conferência?\n")
print("_______________________________________________________________________")

while True:  # Loop principal para permitir múltiplas operações
    while True:
        operacao = input("Você deseja registrar uma 'entrada' ou uma 'saida'? ").strip().lower()
        if operacao in ['entrada', 'saida']:
            break
        print("Operação inválida. Digite 'entrada' ou 'saida'.")

    nome_produto = input("Digite o nome do produto: ").strip().lower()  # Normaliza o nome

    while True:
        try:
            quantidade = float(input(f"Digite a quantidade de {nome_produto}: "))
            if quantidade <= 0:
                raise ValueError("A quantidade deve ser um número positivo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}")

    if operacao == 'entrada':
        # Atualiza o estoque com a nova quantidade de entrada
        estoque[nome_produto] = estoque.get(nome_produto, 0) + quantidade
        print(f"{quantidade} unidades de {nome_produto} adicionadas ao estoque.")

    elif operacao == 'saida':
        # Verifica se há estoque suficiente para a saída
        if nome_produto in estoque and estoque[nome_produto] >= quantidade:
            estoque[nome_produto] -= quantidade
            print(f"{quantidade} unidades de {nome_produto} removidas do estoque.")
            if estoque[nome_produto] == 0:
                del estoque[nome_produto]  # Remove o produto se o estoque zerar
        else:
            print("Estoque insuficiente ou produto não encontrado.")

    # Pergunta se o usuário deseja realizar outra operação
    resposta = input("Deseja realizar outra operação? (sim/não): ").strip().lower()
    if resposta != 'sim':
        break  # Encerra o loop se a resposta for 'não'

print("_______________________________________________________________________")
print("Estoque atualizado:")
if estoque:
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade} unidades")
else:
    print("O estoque está vazio.")
print("Obrigado(a) pela conferência de hoje! Tenha um bom dia! Aguardamos você amanhã! 👋😉")
print("_______________________________________________________________________")