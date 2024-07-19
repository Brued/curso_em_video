# crie um programa que faça o computador jogar jokenpo com vc

from random import randint
from time import sleep

comp_list = ( 'Pedra', 'Papel',  'Tesoura')
escolhaPC = randint(0,2)

print(f'{" Escolha ":=^40}')

print("""Faça sua escolha:
      1 - PEDRA
      2 - PAPEL
      3 - TESOURA """)
print(' ')

escolha = int(input("Qual a sua Escolha? "))


print('*-' *5)
print('\033[35mJO\033[m')
sleep(1)
print('\033[35mKEN\033[m')
sleep(1)
print('\033[35mPÔ!\033[m')
sleep(1)
print('*-'*5)
print(' ')
# Pedra == Pedra empate
# Pedra > Tesoura  0 > 2
# Tesoura == Tesoura empate
# Tesoura > Papel 2 > 1
# Papel == Papel empate
# Papel > Pedra 1 > 0

print('_:' *13)
print(f"O computador jogou \033[31m{comp_list[escolhaPC]}\033[m")
print(f"Você jogou \033[31m{comp_list[escolha]}\033[m")
print('_:' *13)

if escolhaPC == 0:
      if escolha == 0:
            print('Empatou! Jogue novamente!')
      elif escolha == 1: 
            print('Você \033[32mPERDEU!\033[m')
      elif escolha == 2:
            print('Você \033[32mGANHOU!\033[m')
      else: 
            print("Hum! Algo deu errado!")

elif escolhaPC == 1:   
      if escolha == 0:
            print('Você \033[32mGANHOU!\033[m')
      elif escolha == 1:
            print('Empatou! Jogue novamente!')
      else:
            print('Você \033[32mPERDEU!\033[m')

    
elif escolhaPC == 2:
      if escolha == 0: 
            print('Você \033[32mPERDEU!\033[m')
      elif escolha == 1:
            print('Você \033[32mGANHOU!\033[m')
      else:
            print('Empatou! Jogue novamente!')
      
             

