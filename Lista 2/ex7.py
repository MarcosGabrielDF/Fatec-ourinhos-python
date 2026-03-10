"""
Exercício 7 – Salário com bônus
Entrada: O usuário deve digitar o salário base e o percentual de bônus.
Processamento: Calcular o bônus e somar ao salário base.
Saída: Exibir o valor do bônus e o salário final.
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
