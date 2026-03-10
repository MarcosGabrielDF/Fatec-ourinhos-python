"""
Exercício 8 – Distância percorrida
Considere a função d = vt + s
Entrada: O usuário deve digitar velocidade, tempo e posição inicial.
Processamento: Calcular a distância final.
Saída: Exibir a distância calculada.
"""

# Entrada
print('===== Vamos calcular a distância percorrida =====')
print('')
velocidade = float(input('Informe a velocidade em km/h: '))
tempo = float(input('Informe o tempo em horas: '))
PI = float(input('Informe a posição inicial em km: '))

# Cálculo
DP = (velocidade * tempo) + PI  # DP = Distância percorrida

# Saída
print(f'A distância percorrida é {DP:g}')