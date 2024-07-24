# melhore o df 61 perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disse que quer 0 termos.

p = int( input('Qual o primeiro termo da  P.A.? '))
r = int( input( 'Qual a razão da P.A.? '))


# print('=.'*20)
# print(f'\033[31m Os 10 primeiros P.A. de razão {r} e primeiro termo {p} serão: \033[m')
# c = 1
# termo = p
# n = 11
# while c < n:
#     termo += r
#     c += 1
#     print(f' {p} ', end= '')
#     if c == n:
#         s = int(input('\nQuantos termos a mais deseja ver? ou digite 0 para sair... '))
#         n += s 

############# guababara

termo = p
cont = 1
n = 0
s = 10
while s !=0:
    n += s
    while cont <= n :
        print (f"{termo}  ", end= '')
        print(' → ' if cont <= 9 else ' ', end = '')
        termo += r 
        cont += 1
    print('\nPause')
    s = int(input('Quantos termos a mais você quer? '))
print('Fim')


    


