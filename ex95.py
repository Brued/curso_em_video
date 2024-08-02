c_ps = sum_idade = 0
dic = {}
lista = []

while True:
    nome = str(input('Nome: ')).strip()
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    while sexo not in 'MF':
        sexo = str(input('Sexo inválido! Digite novamente [M/F]: ')).strip().upper()

    idade = int(input('Idade: '))
    sum_idade += idade

    dic['Nome'] = nome
    dic['Sexo'] = sexo
    dic['Idade'] = idade
    lista.append(dic.copy())
    c_ps += 1 

    choice = str(input('Deseja continuar [S/N]?_')).upper().strip()
    while choice not in 'SN':
        choice = str(input('Deseja continuar [S/N]?_')).upper().strip()

    if choice == 'N':
        break

m_idd = sum_idade / c_ps

print()
print('*' * 30)
print('----- Resultados da Análise -----')
print()
print(f'=> Total de pessoas cadastradas: {c_ps}')
print(f'=> Média das idades: {m_idd:.2f}')
print('...... Mulheres cadastradas ......')
list_woman = []
for pessoa in lista:
    if pessoa['Sexo'] == 'F':
        list_woman.append(pessoa['Nome'])
print(f'=> {list_woman}')

print()
print('... Pessoas com idade acima da média ...')
list_age = []
for pessoa in lista:
    if pessoa['Idade'] > m_idd:
        list_age.append(pessoa)
for pessoa in list_age:
    print(f'=> Nome: {pessoa["Nome"]}, Sexo: {pessoa["Sexo"]}, Idade: {pessoa["Idade"]}')

print('*' * 30)
