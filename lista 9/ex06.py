"""
6) Leia um número inteiro e mostre todos os seus divisores.
"""

numero = int(input('Fale um número: '))

for i in range(0, numero + 1):
    if i % 2 == 0:
        print(i)
