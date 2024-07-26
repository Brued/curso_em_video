# Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o prog deverá perguntar
# se o usuario quer ou nao continuar.
# no final moestra:
# A) quantas pessoas tem mais de 18y
# B) quantos homens foram cadastrados
# C) quantas mulheres tem menos de 20 anos.

i= total = homem = mulher = 0
while True:
    print('='*20)
    idade = int(input("Qual a sua idade?"))
    if idade > 18:
        i +=1
    sexo= ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo? [M/F] ')).strip().upper()
    print('='*20)
    if sexo == 'M':
        homem +=1
    total += 1
    if sexo == 'F':
        if idade < 20:
            mulher += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('\033[31mQuer continuar?[S/N]\033[m')).strip().upper()
    if escolha == 'N':
        break

print('._'*22)
print(f'Colhemos {total} dados. Agora segue a estatística:')
print('._'*22)
print(f""">> Temos a informação de {i} maior(es) que 18 anos.
>> Total de homem(ns) cadastrado(s) de {homem}
>> Total de  {mulher} mulher(es) com menos de 20 anos""")