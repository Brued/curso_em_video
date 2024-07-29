# crie um prog que tenha um tupla com varias palavras (sem acentos). Depois disso, vc deve mostrar,
# para cada palavra, quais sao as suas vogais



    # Definir a tupla de palavras
tupla = ('computador', 'league','casa', 'fisica', 'deus', 'jesus', 'pai' )

for p in tupla:
    print(f'\nNa palavra {p.upper()} temos ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end =' ')

