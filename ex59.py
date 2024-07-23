# crie um prog que leia dois valores e mostre um menu na tela

# 1- somar
# 2 multiplicar
# 3 maior
# 4 novos numeros
# 5 sair do programa

# seu prog devera realizar a operacao solicitada em casa caso.


from time import sleep

n1 = int (input('Digite um valor: '))
n2 = int (input('Digite o outro valor: '))

escolha = 0 
while escolha != 5: 
    print('=.'*15)
    print("""    [1] → SOMAR
    [2] → MULTIPLICAR
    [3] → MAIOR
    [4] → NOVOS NÚMEROS
    [5] → SAIR DO PROGRAMA """)
    escolha = int(input('Qual a opção desejada? '))
    print('')
    print('=.'*15)
    sleep (2)

    print(' ')

    if escolha == 1:
        soma = n1 + n2
        print(f" → A soma de {n1} e {n2} é igual a {soma}.")

    elif escolha == 2:
        prod = n1 * n2
        print(f" → A multiplicação de {n1} e {n2} é igual a {prod}")

    elif escolha == 3:
        if n1 > n2:
            print(f'o primeiro → {n1}  é o maior. ')
        else:
            print(f' O segundo → {n2} é o maior. ')
    elif escolha == 4:
        print("<< Insira novamente >>")
        n1 = int (input('Digite um valor: '))
        n2 = int (input('Digite o outro valor: '))

    elif escolha == 5:
        print('Finalizando...')

    else:
        print('Algo deu errado ;(. Tente novamente')

print('Você saiu.')