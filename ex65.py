# # crie um prog que leia varios numeros inteiros pelo tc.No final da execucao, mostre media entre todos os valores e
# qua foi o maior e o menor valores lidos, o prog deve perguntar ao usuario se ele quer ou nao consinuar a digitar mais valores.


# escolha = 'S'
# c = 0
# s = 0

# num = int(input('Digite um número: '))
# maior = menor = num


# while escolha == 'S':
#     num = int(input('Digite um número: '))
#     a = num
#     c += 1
#     s += num
#     escolha = str(input('Deseja continuar \033[35m[S/N]\033[m?')).strip().upper()[0]
#     if num > maior:
#          maior =num
#     if num < menor:
#          menor = num
#     while escolha not in ['S', 'N']:
#            print("Inseriu algo deu errado! Digite S → sim e N → não.")
#            escolha = str(input('Deseja continuar \033[35m[S/N]\033[m?')).strip().upper()[0]

# print(f""" A média entre eles → {s / c} 
# maior entre eles é {maior}
# menor entre eles é {menor}
#   """)
# # print(f' Foram digitados {c} e a soma deles é {s} com média {s/c}')
# # print(f'O maior número digitado foi {maior}')


# if escolha == 'S':
#     print('\033[7m >> Prossiga \033[m')
# elif escolha == 'N':
#     print('Parando...')


########### guanabara

resp = 'Ss'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int (input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else: 
        if num > maior:
              maior = num
        if num < menor:
              menor = num
    resp = str(input('Quer continuar? [S/N] '))
media = soma /quant
print(f'Voce digitou {quant} numeros e a media foi {media}')