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
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def retornar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    os.system('cls')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
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
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    retornar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Restaurantes cadastrados: ')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        situacao = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {situacao}')
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
                print('Ativar Restaurante')
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
