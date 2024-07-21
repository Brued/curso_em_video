# crie um prog que leia dois valores e mostre um menu na tela

# 1- somar
# 2 multiplicar
# 3 maior
# 4 novos numeros
# 5 sair do programa

# seu prog devera realizar a operacao solicitada em casa caso.

n1 = int (input('Digite um valor: '))
n2 = int (input('Digite o outro valor: '))

print('=.'*15)
print("""[1] → SOMAR
[2] → MULTIPLICAR
[3] → NOVOS NÚMEROS
[4] → SAIR DO PROGRAMA """)
print('=.'*15)

escolha = int(input('Qual a opção desejada? '))
print(' ')

if escolha == 1:
    n = n1 + n2
    print(f" → A soma de {n1} e {n2} é igual a {n}.")

if escolha == 2:
    nn = n1 * n2

    print(f" → A multiplicação de {n1} e {n2} é igual a {nn}")
if escolha == 3:
    while escolha == 3:
        n1 = int (input('Digite um valor: '))
        n2 = int (input('Digite o outro valor: '))
        escolha = int(input('Qual a opção desejada? '))

# if escolha == 4: