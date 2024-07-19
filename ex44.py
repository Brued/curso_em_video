# elabore um programa que calcule o valor a ser pago por um produto considerando o seu prço normal
# e condição de pagamento:
# - a vista dinheiro/cheque: 10% de desconto
# - a vista no cartao 5% de desconto
# - em ate 2x o cartao: preço normal
# - 3x ou mais no cartao: 20% de juros

preco_normal = float(input("Qual o valor da compra? "))
print("""Formas de pagamento:
      1 - à vista dinheiro/cheque; 
      2 - à vista no cartão 
      3 - 2x cartão
      4 - 3x ou mais no cartão """)

forma = int(input("Insira uma opção para o pagamento: "))

# parcela = int(input("Insira em quantas parcelas quer efetuar o pagamento: "))

if forma == 1:
    final = preco_normal - preco_normal/10
elif forma == 2 :
    final = preco_normal - preco_normal*5/100
elif forma == 3: 
    final = preco_normal
    x = preco_normal/2
    print(f"Sua compra foi parcelada em 2x de R$ {x:.2f} sem juros.")
    
elif forma >= 3: 
    final = preco_normal + preco_normal*2/10
    quantas_parc = int(input("Em 3 ou mais, quantas parcelas? "))
    x = final / quantas_parc
    print(f"Sua compra foi parcelada em {quantas_parc}x de R$ {x:.2f}.")
else:
    print("Insira uma forma valida, tente novamente!")

print(f"Sua compra de R$ {preco_normal:.2f} ficará R$ {final:.2f}")



