numeros = []
numeros_decrescentes = []
lista_nomes = ['Maria', 'João', 'Roberto', 'Bento']
lista_ano_nascimento_e_ano_atual = [1992, 2024]

n = 1

while n <= 10:
    numeros.append(n)
    n += 1

# x = 10

# while x != 0:
#     numeros_decrescentes.append(x)
#     x -= 1

# print(numeros)
# print(numeros_decrescentes)

# for nome in lista_nomes:
#     print(nome)

# soma = 0

# for n in numeros:
#     if n % 2 == 0:
#         soma += n

# print(soma)

#Atividade 5
# numero = int(input('Digite um numero de 1 a 10: '))
# contador = 0

# while contador <= 10:
#     resultado = numero * contador
#     print(f'{numero} x {contador} = {resultado}')
#     contador += 1

# Atividade 6
# soma = 0

# for numero in numeros:
#     try:
#         soma += numero
#     except:
#         print('Valores incorretos!')

# print(soma)

#Atividade 7
media = 0
soma = 0
for numero in numeros:
    try:
        soma += numero
        media = soma / len(numeros)
    except:
        print('Lista vazia')

print(round(media, 2))