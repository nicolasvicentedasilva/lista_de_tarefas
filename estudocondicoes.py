def adicionar_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas): 

    print("*" * 50,)
    print("\nLista de Tarefas: ")
    print("-" * 50)
    n = 1
    for tarefa in lista_de_tarefas:
        print(f"{n} - {tarefa}")
        n += 1 
    print("*" * 50)

def deletar_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.pop((tarefa) - 1)
    return lista_de_tarefas

def exibir_menu():
    """Exibe o menu com opções para o usuário escolher."""
    print("Escolha uma opção: \n"
            "1 - Adicionar tarefa \n"
            "2 - Listar tarefas \n"
            "3 - Deletar tarefa \n" \
            "4 - Sair")

#Inicialização e variáveis de controle  
lista_de_tarefas = []  
continuar = True

#Cabeçalho do programa
print("*" * 50)
print("Bem-vindo ao gerenciador de tarefas!")
print("*" * 50)


#Loop principal do programa, onde o menu é exibido e as opções são processadas
while continuar:
    exibir_menu()
    opcao = input("Insira o que deseja fazer: ")

    if opcao == "1":
        tarefa = input('Insira uma nova tarefa: ') 
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)
    elif opcao == "3":
        #A validação verifica se o valor é numérico, se é menor que o limite da lista e se é maior do que zero
        tarefa = input ('Insira o número da tarefa que deseja deletar: ')
        if not tarefa.isnumeric():
            print("Número da tarefa é inválido, tente novamente.")
        elif int(tarefa) > len(lista_de_tarefas):
            print("Número da tarefa é inválido, tente novamente.")
        elif int(tarefa) <= 0:
            print("Número da tarefa é inválido, tente novamente.")
        else:
            deletar_tarefa(lista_de_tarefas, int(tarefa))
    elif opcao == "4": 
        continuar = False
    else: 
        print("Opção inválida, tente novamente.")
    print("\n")