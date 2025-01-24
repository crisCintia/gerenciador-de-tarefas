'''
Criar um código de gerenciador de tarefas, organizando-o com funções:

1 - Criar uma função adicionar_tarefa(lista, tarefa) que adiciona uma tarefa à lista.
2 - Criar uma função listar_tarefas(lista) que exibe todas as tarefas.
3 - Criar uma função remover_tarefa(lista, indice) que remove uma tarefa pelo índice.
'''

print('='*140)
print('** GERENCIADOR DE TAREFAS **')
print('='*140)

lista_de_tarefas = []

def adicionar_tarefa(lista, tarefa):
    lista.append(tarefa)
    return tarefa

def listar_tarefa(lista):
    if not lista:
        return 'A Lista de Tarefas está vazia!'
    return '\n'.join(f'Tarefa {i + 1}: {tarefa}' for i, tarefa in enumerate(lista))

def remover_tarefa(lista, indice):
    if 0<= indice < len(lista):
        return lista.pop(indice)
    return None

while True:
    print('\n\nEscolha uma opção:')
    print('1 - Adicionar tarefa')
    print('2 - Listar Tarefa')
    print('3 - Remover Tarefa')
    print('4 - Sair\n')

    try:
        opcao = int(input('Digite a opção desejada: '))
        print()
    except ValueError:
        opcao == int(input('Resposta Inválida. Selecione uma opção entre 1, 2, 3 e 4: '))
        continue

    if opcao == 1:
        print('\n\n** ADICIONAR TAREFA **\n')
        nova_tarefa = input('Digite a nova tarefa: ')
        tarefa_adicionada = adicionar_tarefa(lista_de_tarefas, nova_tarefa)
        print(f'\n A Tarefa "{tarefa_adicionada}" foi adicionada com sucesso!\n')
    
    elif opcao == 2:
        print('\n\n ** LISTAR TAREFAS **\n')
        print(listar_tarefa(lista_de_tarefas))
    
    elif opcao == 3:
        print('\n\n** REMOVER TAREFA **\n')

        if lista_de_tarefas:
            print(listar_tarefa(lista_de_tarefas))
            
            try:
                indice_tarefa = int(input('\nDigite o número do item da lista de tarefas que deseja remover: '))-1
                tarefa_excluida = remover_tarefa(lista_de_tarefas, indice_tarefa)

                if tarefa_excluida:
                    print(f'\nTarefa "{tarefa_excluida}" excluída com sucesso!\n')
                else:
                    print('\nNúmero Inválido!!!')
            except ValueError:
                print('\nEntrada Inválida!!! Digite um número válido.')
        else:
            print('\nA lista de tarefas está vazia!!\n')
    
    elif opcao == 4:
        print('\n ** SAINDO DO PROGRAMA **')
        print('Até Logo =D\n\n')
        break

    else:
        print('\n** Opção Inválida!!! Por favor, selecione uma opção entre 1, 2, 3 e 4!')

