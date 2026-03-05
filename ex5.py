# Perguntas
consumo_anterior = float(input('Informe o consumo em kWh do mês anterior: '))
percentual_de_reducao = float(input('Informe o percentual de redução: '))

# Cálculo
reducao = (percentual_de_reducao / 100) * consumo_anterior
novo_consumo = consumo_anterior - reducao

# Resposta
print(f'Você teve uma redução de {reducao:g} kWh em relação ao mês passado; o seu consumo deste mês é {novo_consumo:g} kWh')

# 5. Faça um script em Python que receba o consumo de energia elétrica de
# uma residência (em kWh) no mês anterior e o percentual de redução no
# consumo, e exiba a quantidade de energia economizada e o novo
# consumo.