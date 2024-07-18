# Escreva um programa para aprovar um emprestimo bancario para uma compra de uma casa. 
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
# Calculo o valor da prestação mensal sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.

valor = float( input('Qual o valor da casa? '))
salario = float( input('Qual o seu salário? '))
anos = float( input('Em quantos anos quer pagar? '))

meses= anos * 12
porcentagem_salario = salario * 3 / 10
valor_prestacao = valor / meses

# se porcentagem_salario < valor_prestacao 
# se porcentagem_ salario = valor_prestacao
# se porcentagem_ salario > valor_prestacao

if  porcentagem_salario > valor_prestacao :
    print(f"O valor mensal é de {valor_prestacao:.2f}: \033[31m Seu empréstimo \033[4mAPROVADO!\033[m")
elif porcentagem_salario == valor_prestacao: 
    print(f"O valor mensal é de {valor_prestacao:.2f}: \033[31m Seu empréstimo \033[4mAPROVADO!\033[m")
else: 
    print(f"O valor mensal é de {valor_prestacao:.2f}: \033[31m Seu empréstimo \033[4mNEGADO!\033[m")