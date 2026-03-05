# Perguntas
valor_produto = float(input("Digite o valor do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

# Cálculo
desconto = (percentual_desconto / 100) * valor_produto
valor_final = valor_produto - desconto

# Resposta
print(f'O valor do desconto é {desconto:g}')
print(f'O valor final é {valor_final:g}')

# 1. Faça um script em Python que receba o valor de um produto e o
# percentual de desconto, e exiba o valor do desconto e o valor final do
# produto.