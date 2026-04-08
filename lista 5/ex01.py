"""
1) Faça um algoritmo que leia os valores A, B, C e imprima na tela
se a soma de A + B é menor que C.
"""

#Capturar dados
a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

#operação
soma = a + b

#Condiconal
if soma > c:
    print(f'A soma de  A: {a:g} e B: {b:g} é {soma:g}, então ela é maior que C: {c:g}')
elif soma == c:
    print(f'A soma de  A: {a:g} e B: {b:g} é {soma:g}, então ela é igual que C: {c:g}')
else:
    print(f'A soma de  A: {a:g} e B: {b:g} é {soma:g}, então ela é menor que C: {c:g}')
