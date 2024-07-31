# Crie um progra onde o usuario possa digitar sete valores numéricos e cadastr-os em uma lista única que mantenha 
# separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.

listaP =[]
impar = []
par = []
for i in range (0,7):
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        par.append(n)
    else: 
        impar.append(n)
listaP.append(sorted(par))
listaP.append(sorted(impar))
print(f'A lista com os números pares e impares em ordem crescente → {listaP}')
