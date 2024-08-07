# : Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

p = float(input('Valor R$: ') )

print(f'A metade de R$ {p} é {moeda.metade(p):.2f}')
print(f'O dobro de R$ {p} é {moeda.dobro(p):.2f}')
print(f'Aumentando 10% => {moeda.aumentar(p, 10):.2f}')
print(f'Diminuir 10% => {moeda.diminuir(p, 10):.2f}')