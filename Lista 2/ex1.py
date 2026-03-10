"""
Exercício 1 – Soma de dois números
Entrada: O usuário deve digitar dois números.
Processamento: Calcular a soma dos dois valores utilizando o operador +.
Saída: Exibir o resultado da soma dos dois números.
"""

# Pergunta
print('====== Vamos somar ======')
print('')
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

# Cálculo
soma = numero1 + numero2

# Resposta
print(f'A soma de {numero1:g} e {numero2:g} é igual a {soma:g}')