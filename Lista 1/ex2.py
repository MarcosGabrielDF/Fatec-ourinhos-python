# Perguntas
salario = float(input('Informe o seu salário: '))
percentual = float(input('Informe a porcentagem: '))

# Cálculo
valor_adcional = (percentual / 100) * salario
novo_salario = salario + valor_adcional

# Resposta
print(f'O valor acrescido no novo salário é de {valor_adcional:g} e, somando o antigo salário: {salario:g} + o acréscimo: {valor_adcional:g}, resultará em: {novo_salario:g}')

# 2. Faça um script em Python que receba o salário de um funcionário e o
# percentual de aumento, e exiba o valor do aumento e o novo salário.