# Crie um programa que leia, nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios 
# em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média.


c_ps = sum_idade = 0
dic = {}
list= []
while True:
    nome = str(input('Nome: ')).strip()
    sexo = str(input('Sexo[M/F]: ')).upper().strip()
    while sexo not in 'MF':
        sexo = str(input('Sexo inválido! Digite novamente [M/F]: ')).strip().upper()

    idade = int(input('Idade: '))
    sum_idade += idade

    dic['Nome'] = nome
    dic['Sexo'] = sexo
    dic['Idade'] = idade
    list.append(dic.copy())
    c_ps += 1 

    choice = str(input('Deseja continuar[S/N]?_')).upper().strip()
    while choice not in 'SN':
         choice = str(input('Deseja continuar[S/N]?_')).upper().strip()


    if choice == 'N':
         break
    
m_idd= sum_idade / c_ps
print()
print('*'*30)
print('-----Resultados da Análise-----')
print()
print(f'=> Total de pessoas cadastradas: {c_ps}')
print(f'=> Média das idades: {m_idd:.2f} ')
print('......Mulheres cadastradas......')
list_woman = []
for pessoa in list:
    if pessoa['Sexo'] == 'F':
        list_woman.append(pessoa['Nome'])
print(f'=> {list_woman}')

print()
print('...Pessoas idade acima da média...')
list_age = []

for pessoa in list:
    if pessoa ['Idade'] > m_idd:
        list_age.append(pessoa)
        for pessoa in list_age:
            print(f'=> Nome: {pessoa["Nome"]}, Sexo: {pessoa["Sexo"]}, Idade: {pessoa["Idade"]}')

# print(f'=> {list_age}')

# for p in galera:
#     if p['idade'] >= media:
#         print(' ')
#         for k, v in p.items():
#             print(f'{} = { }')
# print('Encerrado')

####
# galera = list()
# pessoa = dict()
# media = soma =0

# while True:
#     pessoa.clear()
#     pessoa['nome'] = str(input('Nome:')).strip()
    
#     while True:
#         pessoa['sexo'] = str(input('Sexo [M/F]:')).upper().strip()
#         if pessoa['sexo'] in 'MF':
#             break
#         print('Erro! Por favor, digite apenas M ou F.')
    
#     pessoa['idade'] = int(input('Idade:'))
#     soma +=pessoa['idade']
#     galera.append(pessoa.copy())
    
#     while True:
#         resp = str(input('Quer continuar? [S/N]')).upper().strip()
#         if resp in 'SN':
#             break
#         print('ERRO! Responda apenas S ou N.')
    
#     if resp == 'N':
#         break

# print('-=' * 30)
# print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
# media = soma / len(galera)
# print(f'A media de idade é de {media:5.2f} anos.')
# print('A mulheres cadastradas foram')
# for p in galera:
#     if p['sexo'] in 'Ff':
#         print(f'{p["nome"]}')

# print('Lista das pessoas acima da média')

# for p in galera:
#     if p['idade'] >= media:
#         print(' ')
#         for k, v in p.items():
#             print(f'{} = { }')
# print('Encerrado')