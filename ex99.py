# faça um programa que tenha uma funcao chamada maior() que receba varios parametro com valores inteiros.
# seu prog tem que analisar todos os valores e dizer qual deles é maior. >>> desempacotamentos.

######## AULA #####
# def ct(* num):
      # EX1
      #     # for valor in num:
#     #     print(f' s{valor}', end = '')
#     # print()
        #EX2
#     # tam = len(num)
#     # print(f'Recebi os valores {num} e são ao todo {tam} numeros.')
# ct(2, 1, 7)
# ct(8, 0)
# ct(4, 4, 7, 6, 2)
#######################################

def maior(*valores):
    cont= mr =  0
    for v in valores:
        cont +=1
    #     print(f' {v}', end='')
    # print()
        if cont ==1:
            mr = v
        else:
            if v > mr:
                mr = v
    print('>> Com os valores fornecidos, temos:')
    print(f'Com os {valores} ao todo {len(valores)} => o maior valor é {mr}')

maior(2, 7, 2, 4)
print()
maior(2, 4, 6, 10)
print()
maior(-1, 2)