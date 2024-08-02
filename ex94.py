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
        list_age.append(pessoa['Nome'])
print(f'=> {list_age}')