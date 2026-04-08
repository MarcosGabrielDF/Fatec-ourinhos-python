"""
3) Faça um algoritmo que leia dois valores inteiros A e B se os
valores forem iguais deverá se somar os dois, caso contrário
multiplique A por B. Ao final de qualquer um dos cálculos deve-se
atribuir o resultado para uma variável C e mostrar seu conteúdo na
tela.
"""

#CAptura dos dadoss

a = float(input('Informe o valor de A: '))
b = float(input('Informe o valor de B: '))

if a == b:
    c = a + b
    print(f'A soma é {c:g}')
else:
    c = a * b
    print(f'A multiplicação é {c:g}')

