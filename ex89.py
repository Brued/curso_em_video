# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, 
# mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente.

import random

def generate_random_numbers(count, start, end):
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(start, end))
    return numbers

# Generate 10 random numbers between 1 and 100
random_numbers = generate_random_numbers(10, 1, 100)
print("Random numbers:", random_numbers)
