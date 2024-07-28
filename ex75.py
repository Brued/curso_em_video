# Desenvolva um prog que leia 4 valores pelo tc e guarde-os em uma tupla. no final moestre:
# a) quantas vezes apareceu o valor 9 (senao for digitado tbm fala)
# B) Em que posição foi digitado o primeiro valor 3 (senao for digitado tbm fala)
# C) quais foram os numeros pares.

# n1 = int(input('Digite o primeiro numero: '))
# n2 = int(input('Digite o segundo  numero: '))
# n3 = int(input('Digite o terceiro numero: '))
# n4 = int(input('Digite o quarto   numero: '))

# tp = (n1, n2, n3, n4)
# print(f"Você digitou os valores {tp}")

# #A)
# print('-.'*10)
# cont=0
# for numero in tp:
#     if numero == 9 :
#         cont +=1
# if cont > 0 :
#     print(f'>> Número 9 aparece {cont}' )  
# else:
#     print('>> O Número 9 não aparece nenhuma vez.')
# print('-.'*10)

# #B)
# print('-.'*15)
# if 3 not in tp:
#     print('>> Não tem o número 3 na tupla.')
# else:
#     print(f">> O Número 3 esta na {tp.index(3) + 1}ª posição. ")
# print('-.'*15)    

# #C)
# print('-.'*12)
# for numero in tp:
#     if numero % 2 == 0:
#         print(f'>> O número {numero} é par.')
#     else:
#         print(f'>> O número {numero} é ímpar.')
# print('-.'*12)

###################### guanabara
num = ( int(input('Digite o primeiro numero: ')), 
        int(input('Digite o segundo  numero: ')), 
        int(input('Digite o terceiro numero: ')),  
        int(input('Digite o quarto   numero: ')))

print(f"Você digitou os valores {num}")

print(f'O valor 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f" o Valor 3 apareceu na {num.index(3) + 1}ª posição")
else: 
    print('O valore 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 ==0:
        print(→ n , end='')
