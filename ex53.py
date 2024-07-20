# crie um prog que leia uma frase qlqr e dig se ela é um palindromo, desconsiderando os espços


frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split() # sseparar
junto = ''.join(palavras)
# print(junto)

inverso = ''
for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]

# print(junto, inverso)
if inverso == junto :
    print("Temos um palíndromo.")
else:
    print("Temos um palíndromo.")
