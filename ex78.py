# faça um prog que leia 5 valores numericos e guardeos numa lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = list()
for i in range (0,5):
    n = int(input('Digite um número: '))
    numeros.append(n)
print(f'{numeros}')
print('-'*45)
print(f'O maior número digitado foi {max(numeros)} e na posição {numeros.index(max(numeros))+1}')
print(f'O menor número digitado foi {min(numeros)} e na posição {numeros.index(min(numeros))+1}')
print('-'*45)


########

# maior = 0
# menor = 0
# if i ==0:
#     maior = menor = numeros[i]
# else:
#     if numeros[i]> maior:
#         maior = numeros [i]
#     if numeros[i]< menor:
#         menor = numeros[i]