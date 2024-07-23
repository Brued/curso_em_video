# faça um prog que leia um num qlqr e mostre seu fatorial

num = int(input('Insira um número: '))

f = 1
c = num
print(f'Calculando {num}! = ', end = '')
while c > 0:
    print(f'{c}', end ='')
    print('.' if c > 1 else ' = ', end = '')
    f *= c
    c -=1
   
print(f"O fatorial de {num} é igual {f}")


################ FOR 
# f =1 
# for n in range (num, 0 , -1):
#     print(n, end = '')
#     f *= n
# print(f)