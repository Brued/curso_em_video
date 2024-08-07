# crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhandte a função input() do python, 
# so que fazendo a validação para aceitar apenas um valor numérico

# ex
# n = leiaint('Digite um n')

def leiaint():
    n = input('Digite um número: ')
    if n.isdigit():
        n = int(n)
        print('   \033[0;31mOperação válida! Prossiga.\033[m')
    else:
        print('   Insira um número inteiro.')
    
        

#main
leiaint()

############### GUANABARA
# def leiaint(msg):
#     ok = False
#     valor = 0
#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor =  int()
#             ok = True
#         else:
#             print('   \033[0;31mOperação válida! Prossiga.\033[m')
#         if ok:
#             break
#         return valor
# #main
# n = leiaint('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')

