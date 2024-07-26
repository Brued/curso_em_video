# Faça um prog que jogue par ou impar com o pc. O jogo só será interrompido quando o jogador perder,
# mostrando o totl de vitorias consecutivas que ele conquistou no final do jogo.



# computador gera um núm
from random import randint
i= 0

while True:
    print("\033[36mPar ou ímpar? Vamos jogar!!!\033[m")
    numPC = randint(0,10)
    escolhaUS = int(input('Digite um número para jogarmos:'))
    soma = numPC + escolhaUS
    impar_parUS = ' '
    while impar_parUS not in 'PI':
        impar_parUS = str(input('Impar ou Par? [I/P]')).strip().upper()
    
    if soma % 2 == 0:
        resul = 'Par'
    else:
        resul = 'Impar'
    print('*'*50)
    print(f"Sua escolha → {escolhaUS}, escolha PC → {numPC}. A soma é {soma} deu {resul}")
    print('*'*50)

    if impar_parUS == 'P':
        if soma % 2 ==0: 
            print('você ganhou...jogue novamente')
            i += 1
        else:
            print("você perdeu! Até a próxima...")
            break
    elif impar_parUS == 'I':
        if soma % 2  ==1 :
            print('Você ganhou...jogue novamente')
            i += 1
        else:
            print("Você perdeu! Até a próxima...")
            break
    else: 
        print("Escolha inválida! Por favor, escolha 'I' para ímpar ou 'P' para par.")
    
        
print(f" ►►►► Seu total de vitórias foram {i}")

