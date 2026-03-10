""""
Exercício 4 – Média de duas notas
Entrada: O usuário deve digitar duas notas.
Processamento: Somar as duas notas e dividir o resultado por 2.
Saída: Exibir a média das duas notas
"""

# Entrada
print('====== Vamos ver a média de duas notas ======')
print('')
numero1 = float(input('Digite o primeiro valor: '))
numero2 = float(input('Digite o segundo valor: '))

# Cálculo
media = (numero1 + numero2) / 2

# Saída
print(f'O valor da média de {numero1:g} e {numero2:g} é {media:g}')