def aumentar(n=0, porc=0 ):
    valor = n + n* (porc / 100)
    return valor


def diminuir(n=0, porc=0):
    valor = n - n*(porc / 100)
    return valor


def dobro(n=0):
    return  n*2 


def metade(n=0):
    return n/2


def moeda(n=0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')