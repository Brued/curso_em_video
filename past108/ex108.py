# 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga 
# mostrar os números como um valor monetário formatado.

import moeeda

p = float(input('Valor R$: ') )

print(f'A metade de R$ {moeeda.moeda(p)} é {moeeda.moeda(moeeda.metade(p))}')
print(f'O dobro de R$ {moeeda.moeda(p)} é {moeeda.moeda(moeeda.dobro(p))}')
print(f'Aumentando 10% => {moeeda.moeda(moeeda.aumentar(p, 10))}')
print(f'Diminuir 10% => {moeeda.moeda(moeeda.diminuir(p, 10))}')