# faça um programa que tenha uma lista chamada numeros e duas funcoes chamadas sorteia() e somaPar(). A primeira funcao
# vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda funcao vai mostrar a soma entre todos os valores pares
# sorteados pela funcao anteriror.

from random import randint

numeros = list() 

def sorteia(lista):
    for _ in range(5):
        n = randint(0,10)
        lista.append(n)
    print(f'Números sorteados: {lista}')

def somaPar(lista):
    soma = 0
    for _ in lista:
        if _ % 2 == 0:
            soma += _
    print(f'Soma dos números pares: {soma}')
            

#main 
sorteia(numeros)
somaPar(numeros)