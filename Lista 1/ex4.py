# Perguntas
total_vendas = float(input('Informe o total de vendas: '))
percentual_de_comissao = float(input('Informe o percentual de comissão: '))

# Cálculo
receber_comisssao = total_vendas * (percentual_de_comissao / 100)

# Resposta
print(f'Sua comissão será de {receber_comisssao:g}')

# 4. Faça um script em Python que receba o valor total de vendas realizadas
# por um vendedor e o percentual de comissão, e exiba o valor da comissão
# a ser recebida.