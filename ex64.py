# crie um prog que leia varios numeros inteiros pelo tc. o programa so vai para qndo o usuario digitar o valor 999. q
#que é a condicao de parada. No final mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)

n= 0
cont = 0
s = 0
n = int(input('Digite um número inteiro \033[36m(p/ parar digite 999)\033[m:'))
while n != 999: 
        
        cont += 1
        s += n
        n = int(input('Digite um número inteiro \033[36m(p/ parar digite 999)\033[m:'))
else: n == 999
print(f' Foram digitados {cont} números e a soma entre eles é {s}')


################ guanabara
       
