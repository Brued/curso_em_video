# crie um prog que mostre na tela todos os numeros pares que estao no intervalo (1,50)
print('*-'*15)
for i in range(1,50,2):
    print(i+1)
print('São os números pares.')

# modo 2

print(f'{"x":=^20}')
for i in range(1,51):
    if i%2==0:
        print(i)
print('São os números pares.')