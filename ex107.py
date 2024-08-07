# : Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moedaa

p = float(input('Valor R$: ') )

print(f'A metade de R$ {p} é {moedaa.metade(p):.2f}')
print(f'O dobro de R$ {p} é {moedaa.dobro(p):.2f}')
print(f'Aumentando 10% => {moedaa.aumentar(p, 10):.2f}')
print(f'Diminuir 10% => {moedaa.diminuir(p, 10):.2f}')