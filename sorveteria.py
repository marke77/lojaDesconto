# Apresenta uma mensagem de boas-vindas da sorveteria.
print('Bem-vindo(a) a sorveteria do Marco Antonio Silva Fonseca')

# Apresenta o cardápio da sorveteria.
print('|-----------------------------------CARDÁPIO-----------------------------------|')
print('| Bolas  |  Sabor tradicional (tr)  | Sabor premium (pr) | Sabor Especial (es) |')
print('|   1    |       R$ 6,00           |       R$ 7,00      |        R$ 8,00       |')
print('|   2    |       R$ 11,00          |       R$ 13,00     |        R$ 15,00      |')
print('|   3    |       R$ 15,00          |       R$ 18,00     |        R$ 21,00      |')
print('|------------------------------------------------------------------------------|')

# O acumulador irá guardar o total do pedido.
acumulador = 0

# Inicia um loop para o cliente fazer seu pedido.
while True:
    # Solicita ao usuário que escolha um sabor.
    sabor = input('Entre com o sabor desejado. (tr/pr/es): ')
    sabor = sabor.upper()  # Converte a entrada para maiúsculas para padronizar a verificação.

    # Verifica se o sabor escolhido é válido.
    if sabor == 'TR' or sabor == 'PR' or sabor == 'ES':
        # Solicita ao usuário que escolha a quantidade de bolas.
        numBolas = input('Entre com o número de bolas de sorvete desejado. (1/2/3): ')

        # Verifica se a quantidade de bolas escolhida é válida.
        if numBolas != '1' and numBolas != '2' and numBolas != '3':
            print('Quantidade de bolas de sorvete inválida.')
            continue  # Volta ao início do loop.
        else:
            # Baseado na combinação de sabor e número de bolas, determina o valor a ser adicionado ao acumulador.
            if sabor == 'TR' and (numBolas == '1'):
                print('Você escolheu sabor tradicional com 1 bola.')
                acumulador += 6.00
            elif sabor == 'TR' and (numBolas == '2'):
                print('Você escolheu sabor tradicional com 2 bolas')
                acumulador += 11.00
            elif sabor == 'TR' and numBolas == '3':
                print('Você escolheu sabor tradicional com 3 bolas')
                acumulador += 15.00

            if sabor == 'PR' and numBolas == '1':
                print('Você escolheu sabor premium com 1 bola')
                acumulador += 7.00
            elif sabor == 'PR' and numBolas == '2':
                print('Você escolheu sabor premium com 2 bolas')
                acumulador += 13.00
            elif sabor == 'PR' and numBolas == '3':
                print('Você escolheu sabor premium com 3 bolas')
                acumulador += 18.00

            if sabor == 'ES' and numBolas == '1':
                print('Você escolheu sabor especial com 1 bola')
                acumulador += 8.00
            elif sabor == 'ES' and numBolas == '2':
                print('Você escolheu sabor especial com 2 bolas')
                acumulador += 15.00
            elif sabor == 'ES' and numBolas == '3':
                print('Você escolheu sabor especial com 3 bolas')
                acumulador += 21.00
    else:
        print('Sabor de sorvete inválido.')
        continue  # Volta ao início do loop.

    # Solicita ao cliente se ele deseja continuar ou finalizar o pedido.
    fechar_pedido = input('Você quer pedir outro sorvete? (S/N) ')
    if fechar_pedido == 'N' or fechar_pedido == 'n':
        break  # Finaliza o loop.

# Mostra o valor total do pedido ao cliente.
print(f'Total a pagar: R${acumulador:.2f}')
