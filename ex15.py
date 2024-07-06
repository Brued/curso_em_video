# Escreva um programa que pergunte e aquantidade de km percorridos por um carro alugado e a quantidade de dias peloas quais po alugado.
# calcule o preco a pagar sabendo que o carro custa 60rs por dia e 0.15 por km rodado.

quant_km= float(input("Digite a quantidade de Km percorrido pelo carro alugado: "))
quant_dias = float( input( 'Digite a quantidade de dias em que ele foi alugado: '))
preco = quant_km * 60 + quant_dias * 0.15

print('+_'*30)
print(f'Por percorrer {quant_km:.2f} Km e alugar por {quant_dias} dias, pagará: R$ {preco:.2f}')
print('+_'*30)