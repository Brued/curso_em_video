# crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e que mostre quantos dolares ela pode comprar.
# considere Uss 1,00 = R$ 3.27

real = float(input("Insira a quantidade de dinheiro R$: "))
dolar = real / 3.27 
print('_' * 40)
print(f'Tantos {real:.2f} equivalem a {dolar:.2f} dolares. ')