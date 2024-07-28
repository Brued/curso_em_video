# crie uma tupla preenchida com os 20 primeiros colocado da tabela do campeonato brasileiro de futebol, 
# na ordem de colocação. Depois mostre:
# A) apenas os 5 primeiros colocados
# B) os ultimos 4 colocados da tabela
# C) uma lista com os times em ordem alfabetica
# D) em que posição na tabela esta o time do juventude

classif = ( 'Botafogo', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Cruzeiro', 'São Paulo', 'Bahia', 'Paranaense', 'Bragantino', 'Atletico/MG', 
            'Vasco', 'Criciúma', 'Juventude', 'Internacional', 'Corinthians', 'Cuiabá', 'Gremio', 'Vitória', 'Fluminense ', 'Atlético/Go')
# A) 
print(' ')
print(f">> OS cincos primeiros colocados são: {classif[0:5]}")
# B)
print(' ')
print(f">> Os quatro últimos colocados são: {classif[16:20]}")
# C)
print(' ')
print(f'>> Lista em ordem alfabética:{sorted(classif)} ')
# D)
print(' ')
print(f"A posição do juventude é {classif.index('Juventude')+1}")