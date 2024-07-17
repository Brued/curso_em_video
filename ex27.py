
# faça o programa que leia o nome completo de uma pessoa
# mostrando em seguida o 1 e o ultimo nome separadamente

nome = str(input("Digite seu nome completo:")).strip().lower()
sp= nome.split()
print(f"Primeiro nome =", sp[0])
print(f"Último nome =", sp[len(sp)-1])