"""
Exercício 9 – Valor de corrida
Considere a função valor = 5x + 10
Entrada: O usuário deve digitar a quantidade de quilômetros percorridos.
Processamento: Calcular o valor da corrida.
Saída: Exibir o valor total a pagar.
"""

# Entrada
print('========= Valor de Corrida =========')
print('')
qqp = float(input('Informe a quantidade de quilômetros percorridos: '))

# Cálculo
valor_total = 5 * qqp + 10

# Saída
print(f'O valor da corrida é {valor_total:g}')
