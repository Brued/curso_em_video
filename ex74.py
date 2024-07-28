# crie um prog que vai gerar cinco numeros aleatorios e colocar em uma tupla. Depois disso,
# mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao na tupla.

from random import randint

from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print (f'Os valores sorteados foram {numeros}', end='')
print(f'\nO maior valor sorteado foi {max(numeros)} e o menor {min(numeros)}')

################
# # t = ()
# # for i in range (0,5):
# #     num = randint(0,10)
# #     t.append(num)
# #     print(num)
# # print(t)

# from random import randint

# # Gerar cinco números aleatórios e colocá-los em uma tupla
# num_tuple = tuple(randint(0, 10) for _ in range(5))

# # Mostrar a listagem dos números gerados
# print("Números gerados:", num_tuple)

# # Encontrar e mostrar o menor e o maior valor na tupla
# print("Menor valor:", min(num_tuple))
# print("Maior valor:", max(num_tuple))
