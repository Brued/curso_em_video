# faça um prog que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo o usuario.
# o prog sera interrompido quando o numero solicitado for negativo.




i = 0




###########- USANDO FOR  PARA TABUADA -###########

while True:
    n = int(input('Digite um numero para saber a tabuada dele: '))
    if n < 0:
        break
    print(f'~~~Tabuada do {n}~~~~')
    for i in range (0,10):
        print(f'{n} x {i} = {n*i}')
    print('~.'*6)
    
print("Programa encerrado.")


########################################### USANDO WHILE

# while True:
#     n = int(input('Digite um numero para saber a tabuada dele: '))
#     while i <= 10:
#         print(f'{n} x {i} = {n*i}')
#         i += 1
#         if n < 0:
#             break
