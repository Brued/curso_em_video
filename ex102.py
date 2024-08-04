# crie um programa que tenha uma função fatorial que receba dois paramentros: o primeiro que indique o numero a calcular e
# o outro chamado show que será uma valor lógico(opcional) indicando se será mostrado ou nao na tela o processo de calculo 
# do fatorial.

def fatorial(n, show = False):
    f=1
    for i in range(n, 0, -1):
        if show:
            print(i, end ='')
            if i > 1:
                print('.', end = '')
            else:
                print(' = ', end = '')
        f *= i
    return f
    
print(fatorial(3, True))
