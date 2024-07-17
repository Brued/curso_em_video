# Escreva um programa que leia a velocidae de um carro.
# se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado
# a multa vai custr 7$ por cada km acima do limite.

velocidade = float(input("Qual a velocidade do carro? "))

if velocidade <= 80:
    print(f"Velocidade {velocidade} km/h adequada.")
else: 
    print(f"{velocidade} km/h excesso de velocidade! \n" 
          f"Valor de R$ 7,00 por cada Km acima do limite: R$ {(velocidade - 80)*7 :.2f} a pagar!")