# crie um prog que tenha um tupla com varias palavras (sem acentos). Depois disso, vc deve mostrar,
# para cada palavra, quais sao as suas vogais



    # Definir a tupla de palavras
tupla = ('computador', 'league','casa', 'fisica', 'deus', 'jesus', 'pai' )

for palavra in tupla:
    vogais_encontradas = ()
    for letra in palavra:
        if letra in vogais:
            vogais_encontradas.add(letra)

print(f"Na palavra '{palavra}' as vogais encontradas são: {', '.join(vogais_encontradas) if vogais_encontradas else 'nenhuma'}")