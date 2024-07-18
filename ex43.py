# Desenvolva uma logica que leia o peso a altura de uma pessoa. Calcule seu IMC e mostra seu status, de acordo com a tabela abaixo
# - abaixo de 18.5: abaixo do peso 
# - entre 18.5 e 25 peso ideal
# - 25 ate 30 sobrepeso
# - acima de 40 obesidade morbida
peso = float(input('Insira seu peso (kg): '))
altura = float(input('Insira sua altura (m): '))

imc = peso / altura**2
if imc < 18.5:
    print(f" Seu IMC é {imc:.2f} e você está ABAIXO do peso. ")
elif  18.5 <= imc < 25:
    print(f" Seu IMC é {imc:.2f} e você está com peso IDEAL" )
elif 25 <= imc < 30:
    print(f" Seu IMC é {imc:.2f} e você está SOBREPESO")
else:
    print(f" Seu IMC é {imc:.2f} e você está com OBESIDADE MORBIDA")

