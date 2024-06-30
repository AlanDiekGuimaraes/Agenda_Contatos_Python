AGENDA = {}  # Criando uma Agenda vazia.
AGENDA['Alan'] = {
    'telefone': '1193454-3030',
    'email': 'alan@alan.com',
    'endereco': 'Rua: visconde'
}
AGENDA['Brenda'] = {
    'telefone': '1193454-4040',
    'email': 'brenda@brenda.com',
    'endereco': 'Rua: Mende leal 154'
}
def mostrar_contatos(): # Criando um metodo para mostrar todos os contatos da agenda.
    for contato in AGENDA:
        buscar_contato(contato) # Chama a função de buscar os contatos da agenda.
def buscar_contato(contato): # Criando um metodo para buscar os contatos da agenda.
    print('Nome:', contato)
    print('Telefone:', AGENDA[contato]['telefone'])
    print('Email:', AGENDA[contato]['email'])
    print('Endereço:', AGENDA[contato]['endereco'])
    print(50 * '-')
def incluir_editar_contato(contato, telefone, email, endereco): # Metodo de Incluir ou edtar os contatos.
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }
    print()
    print(f'Contato {contato} adicionado/editado com sucesso!')
    print()
def exluir_contato(contato): # Metodo para excluir o contato
    AGENDA.pop(contato)
    print()
    print(f'Contato {contato} foi removido com sucesso!')
    print()
def imprimir_menu(): # Metodo para imprimir o menu.
    print(50*'-')
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('0 - Fechar agenda')
    print(50 * '-')

while True:
    imprimir_menu()
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        mostrar_contatos()
    elif opcao == 2:
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    elif opcao == 3 or opcao == 4:
        contato = input('Digite o nome do contato: ')
        telefone = input(f'Digite o telefone do {contato}: ')
        email = input(f'Digite o email do {contato}: ')
        endereco = input(f'Digite o endereco do {contato}: ')
    elif opcao == 5:
        contato = input('Digite o nome do contato: ')
        exluir_contato(contato)
    elif opcao == 0:
        print('Fechando o programa')
        break
    else:
        print('Opção inválida')