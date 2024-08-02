# Crie um prog que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou
# Depois vai ler a quantidade de gols feitos em dada partida. No final, tudo isso sera guardado em um dicionario incluindo o total de gols
# feitos durante o campeonato.

name = str(input('Name of the player: '))
number_games = int(input('How many games?'))
sum = 0
total_goals = []
data_player = {}
for i in range(number_games):
    goals_games = int(input(f'how many goals in {i} match ? '))
    total_goals.append(goals_games)
    sum += goals_games

data_player['Name'] = name.upper()
data_player['Matchs'] = number_games
data_player['Goals'] = total_goals
data_player['Total Goals'] = sum

print('=.'*20)
print(data_player)
print('=.'*20)

for i, jogador in data_player.items():
    print(f'{i} →→→ {jogador}')
print('=.'*20)

print(f'/The player {name} played {number_games}')
for i, goals in enumerate(total_goals):
    print(f'==> In match {i}, done {goals_games} goals')