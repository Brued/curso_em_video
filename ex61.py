# refaça o desafio 51 lendo o primeiro termo e a razao de uma pa  mostrando os 10 primeiros termos da progressao usando while

p = int( input('Qual o primeiro termo da  P.A.? '))
r = int( input( 'Qual a razão da P.A.? '))
s = 0 

c = p
print('=.'*20)
print(f'Os 10 primeiros P.A. de razão {r} e primeiro termo {p} serão: ')
while c < 10*r:
    c += r
    print(f' {c} ', end= '')

##################### guanabara

# termo = p
# cont = 1
# while cont < = 10:
#     print (f"{termo}")
#     termo += r 
#     cont + = 1
#  print (f" {termo}")