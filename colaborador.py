# Lista vazia para armazenar os colaboradores
lista_colaboradores = []
# ID global para identificação dos colaboradores
id_global = 0


# Função para cadastrar um novo colaborador
def cadastrar_colaborador():
    # Acesso à variável global id_global para atualização
    global id_global
    print('Bem-vindo(a) ao menu de Cadastro de Colaborador')
    # Incrementando o ID global para o novo colaborador
    id_global += 1
    print(f'Id do colaborador: {id_global}')
    # Solicita as informações do colaborador
    nome = input('Entre com o nome: ')
    setor = input('Entre com o setor: ')
    pagamento = float(input('Entre com o pagamento R$: '))
    # Armaze as informações no dicionário
    dicionario_colaborador = {'id': id_global,
                              'nome': nome,
                              'setor': setor,
                              'pagamento': pagamento}
    # Adiciona o dicionário do colaborador na lista de colaboradores
    lista_colaboradores.append(dicionario_colaborador.copy())


# Função para consultar colaboradores cadastrados
def consultar_colaborador():
    print('Bem-vindo(a) ao menu de Consultar Colaborador')
    while True:
        # Menu de opções para consulta
        opcao_consulta = input('Escolha a opção desejada: \n' +
                               '1 - Consultar todo(s) os Colaborador(es) \n' +
                               '2 - Consultar Colaborador(es) por Id \n' +
                               '3 - Consultar Colaborador(es) por Setor \n' +
                               '4 - Retornar ao Menu \n' +
                               '>>')
        # Opção para mostrar todos os colaboradores
        if opcao_consulta == '1':
            for colaborador in lista_colaboradores:
                for key, value in colaborador.items():
                    print(f'{key}: {value}')
                print('')

        # Opção para consultar colaborador pelo Id
        elif opcao_consulta == '2':
            consultar = int(input('Entre com o Id desejado: '))
            for colaborador in lista_colaboradores:
                if colaborador['id'] == consultar:
                    for key, value in colaborador.items():
                        print(f'{key}: {value}')
                    print('')

        # Opção para consultar colaborador pelo setor
        elif opcao_consulta == '3':
            consultar = input('Entre com o Setor desejado: ')
            for colaborador in lista_colaboradores:
                if colaborador['setor'] == consultar:
                    for key, value in colaborador.items():
                        print(f'{key}: {value}')
                    print('')

        # Opção para voltar ao menu principal
        elif opcao_consulta == '4':
            return
        # Caso o usuário digite uma opção inválida
        else:
            print('Opção inválida. Tente novamente!')


# Função para remover um colaborador da lista
def remover_colaborador():
    print('Bem-vindo(a) ao menu de Remover Colaborador')
    # Pede o Id do colaborador que irá ser removido
    consulta = int(input('Entre com o Id do Colaborador que deseja remover: '))
    for colaborador in lista_colaboradores:
        if colaborador['id'] == consulta:
            lista_colaboradores.remove(colaborador)
            print('Colaborador removido com sucesso!')


# Menu principal do programa
print('Bem-vindo(a) ao Controle de Colaboradores do Marco Antonio Silva Fonseca')
print('')
while True:
    # Menu de opções principais
    opcao_principal = input('Escolha a opção desejada: \n' +
                            '1 - Cadastrar Colaborador \n' +
                            '2 - Consultar Colaborador(es) \n' +
                            '3 - Remover Colaborador \n' +
                            '4 - Sair \n' +
                            '>>')
    # Direciona para a opção de cadastro do novo colaborador
    if opcao_principal == '1':
        cadastrar_colaborador()
    # Direciona para a opção de consulta de colaborador
    elif opcao_principal == '2':
        consultar_colaborador()
    # Direciona para a opção de remoção de colaborador
    elif opcao_principal == '3':
        remover_colaborador()
    # Finaliza o programa
    elif opcao_principal == '4':
        print('Finalizando, obrigado!')
        break
    # Caso o usuário digite uma opção inválida
    else:
        print('Opção inválida. Tente novamente!')
