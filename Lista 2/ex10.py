"""
Exercício 10 – Consumo de combustível
Considere a função C(x) = 0.12x + 3
Entrada: O usuário deve digitar a quantidade de quilômetros percorridos.
Processamento: Calcular o consumo estimado.
Saída: Exibir o consumo total.
"""

# Entrada
print('===== Consumo de combustível =====')
print("")
km = float(input('Qual a quantidade de km percorridos: '))

# Cálculo
consumo_combustivel = 0.12 * km + 3

# Saída
print(f'Você consumiu um total de {consumo_combustivel:g} litros em {km:g} km rodados')