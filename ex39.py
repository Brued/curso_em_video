# Faça um prog que leia o ano de nascimento de um jovem e infome de acordo com sua idade:
# - se ele ainda vai se alistar ao serviço militr
# - se é a hora de se alistr 
# - se ka passou do tempo do alistamento
##
# seu programa tambem devera mostrar o tempo que falta ou passou do prazo

idade = int(input('Insira a sua idade: '))

if idade < 18 :
    print(f"Ainda \033[31mnão está no prazo\033[m para se alistar, faltam {18-idade} para se alistar!")
elif idade == 18 :
    print(f"Que ótimo, \033[31mjá está no tempo\033[m! VAMOS SE ALISTAR?")
else: 
    print(f"Hum, \033[31mjá passou {idade -18} do prazo\033[m para se alistar!")

    