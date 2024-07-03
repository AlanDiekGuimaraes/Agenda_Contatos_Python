AGENDA = {}  # Criando uma Agenda vazia.

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

def ler_detalhes_contatos():
    telefone = input(f'Digite o telefone do {contato}: ')
    email = input(f'Digite o email do {contato}: ')
    endereco = input(f'Digite o endereco do {contato}: ')
    return telefone, email, endereco


def incluir_editar_contato(contato, telefone, email, endereco): # Metodo de Incluir ou editar os contatos.

    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }
    salvar()
    print(f'Contato {contato} adicionado/editado com sucesso!')

def exluir_contato(contato): # Metodo para excluir o contato
    try:
        AGENDA.pop(contato)
        salvar()
        print(f'Contato {contato} foi removido com sucesso!', sep='\n')
    except KeyError:
        print('Contato inexistente')
    except Exception as erro:
        print('Um erro inesperado ocoreu')

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo: # O parametro 'w' abre o arquivo em modo de escrita.
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato},{telefone},{email},{endereco}\n')
        print(f'Agenda exportada com sucesso')
    except Exception as erro:
        print('Algum erro ocoreu ao exportar contado')

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo: # O parametro 'r' abre o arquivo em modo de leitura.
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, telefone, email, endereco)
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as erro:
        print('Algum erro inesperado ocoreu')

def salvar():
    exportar_contatos('database.csv')

def carregar():
    try:
        with open('database.csv', 'r') as arquivo: # O parametro 'r' abre o arquivo em modo de leitura.
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco
                }
        print(f'''Database carregado com sucesso.
{len(AGENDA)} contado(s) carregado(s).''')
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as erro:
        print('Algum erro inesperado ocoreu')

def imprimir_menu(): # Metodo para imprimir o menu.
    print(50*'-')
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para CSV')
    print('7 - Importar contatos para CSV')
    print('0 - Fechar agenda')
    print(50 * '-')


# Inicio do programa.
carregar()
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
            telefone, email, endereco = ler_detalhes_contatos()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '4':
        contato = input('Digite o nome do contato: ')

        try:  # Verificando se o contato já esxiste na Agenda, se exitir vai editar o contato.
            AGENDA[contato]
            print(f'Editando o contato: {contato}')
            telefone, email, endereco = ler_detalhes_contatos()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print('Contato inexistente')
    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        exluir_contato(contato)
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado ')
        exportar_contatos(nome_do_arquivo)
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado ')
        importar_contatos(nome_do_arquivo)
    elif opcao == '0':
        print('Fechando o programa')
        break
    else:
        print('Opção inválida')

