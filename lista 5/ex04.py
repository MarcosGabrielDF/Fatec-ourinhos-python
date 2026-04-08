"""
4) Encontrar o dobro de um número caso ele seja positivo e o seu
triplo caso seja negativo, imprimindo o resultado.
"""

numero = float(input('Digite o número: '))

if numero > 0:
    print(f'O dobro de {numero:g} é {numero * 2:g}')
elif numero == 0:
    print('Número invalido')
else:
    print(f'O triplo de {numero:g} é {numero * 3:g}')
