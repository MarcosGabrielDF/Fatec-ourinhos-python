"""
Exercício 2 – Dobro de um número
Entrada: O usuário deve digitar um número.
Processamento: Multiplicar o número digitado por 2 utilizando o operador *.
Saída: Exibir o dobro do número informado
"""

# Pergunta
print('====== Vamos dobrar ======')
print('')
numero = float(input('Informe o valor: '))

# Cálculo
dobro = numero * 2

# Saída
print(f'O dobro de {numero:g} é {dobro:g}')