# numero = int(input('Escolha um numero: '))
# divisor = 2

# if numero % divisor == 0:
#     print('Seu numero é par')
# else:
#     print('Seu numero é impar')

# Atividade II

# idade = int(input('Digite sua idade: '))

# if 0 <= idade <= 12:
#     print('Criança')
# elif 12 < idade  <= 18:
#     print('Adolescente')
# else:
#     print('Adulto')

# Atividade III

# usuario = 'Thiago'
# senha = 12345

# usuario_input = input('Digite seu usuario: ')
# senha_input = int(input('\nDigite sua senha: '))

# if usuario_input == usuario and senha_input == senha:
#     print('Autenticação com sucesso')
# else:
#     print('Senha e/ou usuario incorretos')

#Atividade IV

x = int(input('Valor de x: '))
y = int(input('Valor de y: '))

if x > 0 and y > 0:
    print('Primeiro quadrante')
elif x < 0 and y > 0:
    print('Segundo quadrante')
elif x < 0 and y < 0:
    print('Terceiro quadrante')
elif x > 0 and y < 0:
    print('Quarto quadrante')
else:
    print('O ponto está localizado no eixo ou origem')
