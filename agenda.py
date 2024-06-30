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
        print(50*'-')

def buscar_contato(contato): # Criando um metodo para buscar os contatos da agenda.
    print('Nome:', contato)
    print('Telefone:', AGENDA[contato]['telefone'])
    print('Email:', AGENDA[contato]['email'])
    print('Endereço:', AGENDA[contato]['endereco'])


def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }
    print(f'Contato {contato} adicionado/editado com sucesso!')

