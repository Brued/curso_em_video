# Crie um programa onde o usuário digite uma expressao quaquer que use parenteses. Seu aplicativo deverá analisar se a expressao
# passada esta com os parenteses abertos e fechado na ordem correta

exp = str(input('Digite uma expressão: '))
pilha = []
for simb in exp:
    if simb == '()':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressção está válida!')
else:
    print('Sua expressção está errada!')
    
    
    
