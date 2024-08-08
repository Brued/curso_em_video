def aumentar(n=0, porc=0, formato=False ):
    ''' 
    :parametro n: define a entrada do valor
    :parametro porc: define a porcentagem do aumento
    :parametro formato: define a forma de saida com ou sem formato.
    :retorn: o valor reajustado, com ou sem formato.
    
    '''
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


def resumo(n, tax_aum =0, tax_red=0):
    print('-'*33)
    print(f'{"Resumo do valor":^30}')
    print('-'*33)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{tax_aum}% de aumento: \t \t{aumentar(n, tax_aum, True)}')
    print(f'{tax_red}% de redução: \t \t{diminuir(n, tax_red, True)}')
    print('-'*33)