# refaça o desafio 009 mostrando a tabuada de um numero que o usuario escolher usando for

num = int(input('Insira um numero: '))

print(f" Tabuada do {num}")
for i in range(1,11):
    print(f"{num} x {i} = {num* i}")

