"""
5. DESCONTO EM LOJA DE ELETRÔNICOS
Peça o valor da compra e o método de pagamento ("cartão" ou "dinheiro").
• Se o pagamento for em dinheiro e o valor for acima de 500, aplique 10% de desconto.
• Se for no cartão e o valor for acima de 800, aplique 5% de desconto.
• Caso contrário, informe que não há desconto.
"""

#Captação
valor = float(input('Coloque o valor da compra: '))

print(
"""Dígite

[1] para Dinheiro
[2] para Cartão 
""")

M_pagamento = input('')

if M_pagamento == '1' and valor > 500:
    desconto = valor * 0.10
    valor_final = valor - desconto
    print(f'O desconto vai ser de {desconto:g}, seu produto final custara {valor_final:g}')
elif M_pagamento == '2' and valor > 800:
    desconto = valor * 0.05
    valor_final = valor - desconto
    print(f'O desconto vai ser de {desconto:g}, seu produto final custara {valor_final:g}')
else:
    print('Não tem desconto')
