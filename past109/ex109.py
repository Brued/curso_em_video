
import moeeda

p = float(input('Valor R$: ') )

print(f'A metade de R$ {moeeda.moeda(p)} é {moeeda.metade(p, True)}')
print(f'O dobro de R$ {moeeda.moeda(p)} é {moeeda.dobro(p, True)}')
print(f'Aumentando 10% => {moeeda.aumentar(p, 10, True)}')
print(f'Diminuir 10% => {moeeda.diminuir(p, 10, True)}')