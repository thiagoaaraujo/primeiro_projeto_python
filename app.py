import os

restaurantes = [{'nome':'Alameda', 'categoria':'comida de rua', 'ativo':False}, 
                {'nome':'DeCasa Delivery', 'categoria':'pizzaria', 'ativo':True}, 
                {'nome':'Meia-noite', 'categoria':'restaurante', 'ativo':False}]

def exibir_nome_do_programa():
    print('''
    ██████████████████████████████████████████████████████████████████████████
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
    ''')
def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar estado do Restaurante')
    print('4. Sair\n')

def retornar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    os.system('cls')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    os.system('cls')
    exibir_subtitulo('Encerrando programa...')

def opcao_invalida():
    print('Opção inválida\n')
    retornar_ao_menu_principal()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    retornar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Restaurantes cadastrados: ')

    print(f'Nome do restaurante'.ljust(22),'|Categoria'.ljust(22),'|Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativo' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    retornar_ao_menu_principal()

def alterar_estado_do_restaurante():
    exibir_subtitulo('Aterando estado do restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso.'
            print(mensagem)
    if restaurante_encontrado == False:
        print('O restaurante não foi encontrado. Por favor, cadastre o restaurante primeiro.')
    retornar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Selecione uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_estado_do_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
