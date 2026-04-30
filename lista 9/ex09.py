"""
9) Leia um número entre 1 e 10, calcule e mostre a sua
tabuada;
"""

numero = int(input('Fale um número entre 1 e 10: '))
contador = 0

if numero <= 10 and numero >= 1:
    while contador < 11:
        print(f'{numero} x {contador} = {numero * contador}')
        contador += 1
else:
    print('Erro.')