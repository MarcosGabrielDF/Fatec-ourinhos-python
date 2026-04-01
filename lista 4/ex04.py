"""
4. Ler dois números inteiros e verificar qual é o maior e qual é o
menor. Suponha sempre números diferentes;
"""
from sys import float_repr_style

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
    print(f'O numero {n1:g} é maior que o numero {n2:g}')
else:
    print(f'O numero {n2:g} é maior que o numero {n1:g}')
