"""
Exercício 6 – Função do primeiro grau com coeficientes
Considere a função f(x) = ax + b
Entrada: O usuário deve digitar os valores de a, b e x.
Processamento: Calcular o valor da função.
Saída: Exibir o valor calculado de f(x).
"""

# Pergunta
print('====== Vamos calcular f(x) = ax + b ======')
print('')
a = float(input('Digite o valor de a: '))
x = float(input('Digite o valor de x: '))
b = float(input('Digite o valor de b: '))

# Cálculo
f_de_x = a * x + b

# Saída
print(f'O valor de f({x:g}) = {a:g} * {x:g} + {b:g} é igual a {f_de_x:g}')
