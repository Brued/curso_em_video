# Desenvolva um prg que pergunte a distancia de uma viagem em km.
# calcule o preco da passagem, cobrando .50 por km para viagens ate 200k e .45 para viagens mais londas

distancia = float(input("Insira a distancia da viagem em km: "))

if distancia <= 200:
    preco = 0.50*distancia
    print(f"Preço a pagar é R$ {preco:.2f}")
else:
    preco = 0.45*distancia
    print(f"Preço a pagar é R$ {preco:.2f}")