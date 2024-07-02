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
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato) # Chama a função de buscar os contatos da agenda.
    else:
        print("Agenda vazia")
def buscar_contato(contato): # Criando um metodo para buscar os contatos da agenda.
    try:
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
        print(50 * '-')
    except KeyError:
        print('Contato inexistente')
    except Exception as erro:
        print('Um erro inesperado ocoreu')
def incluir_editar_contato(contato): # Metodo de Incluir ou edtar os contatos.
    telefone = input(f'Digite o telefone do {contato}: ')
    email = input(f'Digite o email do {contato}: ')
    endereco = input(f'Digite o endereco do {contato}: ')
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }
    print(f'Contato {contato} adicionado/editado com sucesso!')

def exluir_contato(contato): # Metodo para excluir o contato
    try:
        AGENDA.pop(contato)
        print(f'Contato {contato} foi removido com sucesso!', sep='\n')
    except KeyError:
        print('Contato inexistente')
    except Exception as erro:
        print('Um erro inesperado ocoreu')

def exportar_contatos():
    try:
        with open('agenda.csv', 'w') as arquivo: # O parametro 'w' abre o arquivo em modo de escrita.
            arquivo.write('Nome,Telefone,Email,Endereco\n')
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato},{telefone},{email},{endereco}\n')
        print(f'Agenda exportada com sucesso')
    except Exception as erro:
        print('Algum erro ocoreu ao exportar contado')

def imprimir_menu(): # Metodo para imprimir o menu.
    print(50*'-')
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para CSV')
    print('0 - Fechar agenda')
    print(50 * '-')

while True:
    imprimir_menu()
    opcao = input('Digite sua opção: ')
    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    elif opcao == '3':
        contato = input('Digite o nome do contato: ')

        try: # Verificando se o contato já esxiste na Agenda, se exitir vai dar o erro de contato já existente.
            AGENDA[contato]
            print(f'O contato {contato} já exite')
        except: # Caso não exista o contato o código continua e adiciona o contato.
             incluir_editar_contato(contato)
    elif opcao == '4':
        contato = input('Digite o nome do contato: ')

        try:  # Verificando se o contato já esxiste na Agenda, se exitir vai editar o contato.
            AGENDA[contato]
            print(f'Editando o contato: {contato}')
            incluir_editar_contato(contato)
        except KeyError:
            print('Contato inexistente')
    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        exluir_contato(contato)
    elif opcao == '6':
        exportar_contatos()
    elif opcao == '0':
        print('Fechando o programa')
        break
    else:
        print('Opção inválida')