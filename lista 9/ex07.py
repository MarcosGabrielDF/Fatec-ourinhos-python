"""
7) Leia 10 números e mostre a média aritmética entre eles;
"""

soma = 0
for i in range(0, 10):
    numero = int(input('Número: '))
    soma += numero

media = soma / 10
print(f'A média é: {media:g}')
