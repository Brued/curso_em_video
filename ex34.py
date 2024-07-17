# Escreva um prog que pergunte o salario de um funcionario e calcule seu valor de aumento
# para salarios superiores a 1.250 calcule 10% de aumento
# para inferios ou iguais, aumento de 15%

salario = float( input("Digite seu salário R$: "))

if salario > 1250:
    aumento = salario/10
    print(f"O seu aumento é de: {aumento:.2f}")
if salario <= 1250:
    aumento = salario*15/10
    print(f"O seu aumento é de: { aumento:.2f}")
    