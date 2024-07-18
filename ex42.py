# Refaça o Desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
# Equilatero se todos os lados iguais
# Isoceles dois lados iguais
# Escaleno se todos forem diferentes

x = int(input('Digite o valor do primeiro segmento de reta: '))
y = int(input('Digite o valor do segundo segmento de reta: '))
z = int(input('Digite o valor do terceiro segmento de reta: '))

if x + y > z and y + z > x and z + x > y :
    print(f"Com os valores {x}, {y} e {z} é possível formar um triangulo.")
    if x == y == z:
        print("Temos um triangulo EQUILÁTERO.")
    elif x == y != z or x == z != y or y == z != x :
        print("Temos um triangulo ISÓCELES.")
    else:
        print("Temos um triangulo ESCALENO.")
else:
   print(f"Com os valores {x}, {y} e {z} não é possível formar um triangulo.")