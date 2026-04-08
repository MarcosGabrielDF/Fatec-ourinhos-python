"""
6) Faça um algoritmo que leia uma variável e some 5, caso seja par
ou some 8 caso seja ímpar, imprimir o resultado desta operação.
"""

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'Número {numero} é par, somamos {numero} + 5 = {numero + 5:g}')
else:
    print(f'Número {numero} é impar, somamos {numero} + 8 = {numero + 8:g}')
