"""
1) Faça um script que leia os valores A, B, C e imprima na tela se a soma de A + B
é menor que C.
"""

#Entrada
a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

#Conta
soma = a + b

if soma < c:
    print(f'A + B: {soma} é menor que C: {c}')
elif soma == c:
    print(f'A + B: {soma} é igual a C: {c}')
else:
    print(f'C: {c} é menor que A + C:{soma}')