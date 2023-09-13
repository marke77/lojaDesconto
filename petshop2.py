# Apresenta uma mensagem de boas-vindas do PetShop.
print('Bem-vindo(a) ao PetShop do Marco Antonio Silva Fonseca')


# Função que calcula o preço baseado no peso do cachorro.
def cachorro_peso():
    while True:  # Mantém um loop até receber uma entrada válida.
        try:
            # Solicita o peso do cachorro ao usuário.
            peso = float(input('Qual o peso do seu cachorro?: '))

            # Estrutura de decisão que define o preço baseado no peso.
            if (peso < 3):
                return 40
            elif (peso >= 3 and peso < 10):
                return 50
            elif (peso >= 10 and peso < 30):
                return 60
            elif (peso >= 30 and peso < 50):
                return 70
            else:
                print('Infelizmente não aceitamos cachorros tão grandes.')
        # Verifica erros de digitação, como quando o usuário não inserir um número.
        except ValueError:
            print('Por favor, entre com o peso do cachorro novamente.')


# Função que calcula o valor extra baseado no tipo de pelo do cachorro.
def cachorro_pelo():
    while True:  # Mantém um loop até receber uma entrada válida.
        # Solicita ao usuário o tipo de pelo do cachorro.
        pelo = input('c - Pelo Curto \n' +
                     'm - Pelo Médio \n' +
                     'l - Pelo Longo \n' +
                     'Escolha o tipo de pelo: \n' +
                     '>>').lower()  # Transforma a entrada em minúsculas.

        # Estrutura de decisão que define o valor extra de acordo com o tipo de pelo.
        if pelo == 'c':
            return 1.00
        elif pelo == 'm':
            return 1.50
        elif pelo == 'l':
            return 2.00
        else:
            print('Opção inválida.')


# Função que adiciona custos extras para serviços adicionais.
def cachorro_extra():
    total_extra = 0  # O total_extra irá guardar e acumular o total do pedido.
    while True:  # Mantém um loop até receber uma entrada válida.
        # Solicita ao usuário se deseja adicionar mais algum serviço.
        extra = input('Deseja adicionar mais algum serviço? \n' +
                      '1 - Corte de Unhas - R$ 10,00 \n' +
                      '2 - Escovar os Dentes - R$ 12,00 \n' +
                      '3 - Limpeza de Orelhas - R$ 15,00 \n' +
                      '0 - Não desejo mais nada. (encerrar pedido) \n' +
                      '>>')

        # Estrutura de decisão que adiciona os custos dos serviços extras escolhidos.
        if extra == '1':
            total_extra += 10
        elif extra == '2':
            total_extra += 12
        elif extra == '3':
            total_extra += 15
        elif extra == '0':
            return total_extra
        else:
            print('Opção inválida.')


# Calcula o total do pedido e imprime o valor final.
peso = cachorro_peso()
pelo = cachorro_pelo()
extra = cachorro_extra()
total = peso * pelo + extra
print(f'Total do pedido R${total:.2f} (Peso: {peso} * Pelo: {pelo} + Adicional(is) {extra}) ')
