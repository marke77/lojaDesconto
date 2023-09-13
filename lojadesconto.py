# Imprime a mensagem de boas-vindas da minha loja
print('Bem-vindo(a) a loja do Marco Antonio Silva Fonseca')

# Pede o valor do produto ao usuário e armazena na variável "preco"
preco = float(input('Digite o valor do produto: '))

# Pede a quantidade de produtos ao usuário e o armazena na variável "qtd"
qtd = int(input('Digite a quantidade de produto: '))

# Calcula o preço com a quantidade
preco_total = preco * qtd

# Se a quantidade do produto é menor que 200
if qtd < 200:
    print(f'O valor SEM desconto será R${preco_total:.2f}')

# Se a quantidade do produto é maior ou igual a 200 e menor que 1000
elif qtd >= 200 and qtd < 1000:
    print(f'O valor SEM desconto será R${preco_total:.2f}')
    # Calcula o valor do desconto de 5% e o armazena na variável 'desc'
    desc = (preco_total * (1 - 5 / 100))
    print(f'O valor COM desconto será R${desc:.2f}')

# Se a quantidade do produto é maior ou igual a 1000 e menor que 2000
elif qtd >= 1000 and qtd < 2000:
    print(f'O valor SEM desconto será R${preco_total:.2f}')
    # Calcula o valor do desconto de 10% e o armazena na variável 'desc'
    desc = (preco_total * (1 - 10 / 100))
    print(f'O valor COM desconto será R${desc:.2f}')

# Se a quantidade do produto é maior ou igual a 2000
else:
    print(f'O valor SEM desconto será R${preco_total:.2f}')
    # Calcula o valor do desconto de 15% e o armazena na variável 'desc'
    desc = (preco_total * (1 - 15 / 100))
    print(f'O valor COM desconto será R${desc:.2f}')
