# faça um prog que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo o usuario.
# o prog sera interrompido quando o numero solicitado for negativo.




i = 0




###########- USANDO FOR  PARA TABUADA -###########

# while True:
#     n = int(input('Digite um numero para saber a tabuada dele: '))
#     if n < 0:
#         break
#     print(f'~~~Tabuada do {n}~~~~')
#     for i in range (0,11):
#         print(f'{n} x {i} = {n*i}')
#     print('~.'*6)
    
# print("Programa encerrado.")


########################################### USANDO WHILE
# i = 0
# while True:
#     n = int(input('Digite um numero para saber a tabuada dele: '))
#     if n < 0:
#             break
#     while i < 10:
#         i += 1
#         print(f'{n} x {i} = {n*i}')
#         c = 0
# print('Programa encerrado.')

while True:
    t = int(input('Digite um número inteiro que te daremos a sua tabuada: '))
    print('-'*20)
    if t < 0:
        break
    while i < 10:
        i += 1
        print(f'{t} * {i:2} = {t*i}')
    print('-'*20)
    i = 0 #para zerar o contador e poder inicar uma nova tabuada do 1 ao 10
print('Programa da tabuada encerrado.')