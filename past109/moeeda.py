def aumentar(n=0, porc=0, formato=False ):
    valor = n + n* (porc / 100)
    return valor if formato is False else moeda(valor)


def diminuir(n=0, porc=0, formato=False):
    valor = n - n*(porc / 100)
    return valor if formato is False else moeda(valor)


def dobro(n=0, formato=False):
    valor = n*2
    return valor if not formato else moeda(valor)


def metade(n=0, formato=False):
    valor = n/2
    return valor if not formato else moeda(valor)


def moeda(n=0, moeda = 'R$'):
    return f"{moeda}{n:.2f}".replace('.', ',')