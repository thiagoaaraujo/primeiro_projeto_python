#Atividade 1
pessoas = {'nome':'João', 'idade':'19', 'cidade':'Patos de Minas'}

print(pessoas)

#Atividade 2
# def modificar_idade():
#     nome_pessoa = input('Digite o nome da pessoa para atualizar seus dados: ')
#     nome_encontrado = False

#     for pessoa in pessoas:
#         if nome_pessoa == pessoa['nome']:
#             idade_corrigida = input('Digite a idade atualizada: ')
#             pessoa['idade'] = idade_corrigida
#     if not nome_encontrado:
#         print('Pessoa não encontrada!')

# modificar_idade()

# print(pessoas)

# pessoas['profissao'] = 'Mecânico'

# del pessoas['cidade']

# print(pessoas)

#Atividade 3

# numeros_quadrados = {x: x**2 for x in range(1, 6)}
# print(numeros_quadrados)

#Atividade 4


# busca_chave = input("Digite a chave que deseja buscar: ")

# if busca_chave in pessoas:
#     print(f'A chave {busca_chave} existe')
# else:
#     print(f'A chave {busca_chave} não existe')

#Atividade 5

frase = "Python se tornou uma das linguagens de programação mais populares do do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)





