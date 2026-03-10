"""
Exercício 3 – Cálculo de desconto
Entrada: O usuário deve digitar o preço de um produto e o percentual de desconto.
Processamento: Calcular o valor do desconto e subtrair do preço original.
Saída: Exibir o valor do desconto e o preço final do produto.
"""

# Pergunta
print('====== Vamos calcular o desconto ======')
print('')
preco_produto = float(input('Qual é o preço do produto? '))
percentual_desconto = float(input('Qual é o percentual de desconto? '))

# Cálculo
desconto = (preco_produto * percentual_desconto) / 100
preco_final = preco_produto - desconto

# Saída
print(f'O desconto é de {desconto:g}. O valor do produto era {preco_produto:g}, mas agora fica {preco_final:g}')