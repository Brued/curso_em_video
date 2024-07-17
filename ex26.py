# faça um programa ue leia uma frase pelo teclado e mostre:
# quantas x aparece a letra A
# em ue posicao ela aparece ela 1x
# em que posicao ela aparece a ultima

frase = str(input("Digite uma frase:")).strip().lower()

#contar
print(f"A letra 'a' aparece:", frase.count('a'))
#primeira vez
print(f"A letra 'a' aparece na posição: ", frase.find('a')+1)

print(f"A letra 'a' aparece na posição: ", frase.rfind('a')+1)