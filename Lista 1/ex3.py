# Perguntas
distancia_percorrida = float(input('Informe qual foi a distância percorrida pelo carro: '))
litros_consumidos = float(input('Informe quantos litros foram consumidos pelo carro: '))
nova_distancia = float(input('Informe qual a nova distância do carro: '))

# Cálculo
regra_de_tres = (litros_consumidos * nova_distancia) / distancia_percorrida

# Resposta
print(f'Você irá gastar um total de {regra_de_tres:g} litros nessa nova viagem')

# 3. Faça um script em Python que receba a distância percorrida por um carro,
# a quantidade de litros consumidos nessa distância e uma nova distância
# a ser percorrida, e exiba quantos litros serão necessários para percorrer
# essa nova distância.