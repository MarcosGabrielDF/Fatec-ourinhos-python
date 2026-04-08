"""
7) Tendo como dados de entrada a altura e o sexo de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as
seguintes fórmulas:
● para homens: (72.7 * h) – 58;
● para mulheres: (62.1 * h) – 44.7.
"""

#Captura de dados
h = float(input('Digite sua altura: '))
sexo = input('M ou F: ')

#Tratamento
sexo = sexo.upper()

if sexo == 'M':
    pi = (72.7 * h) - 58
    print(f'Seu pesso ideia é {pi:.2f} Kg.')
elif sexo == 'F':
    pi = (62.1 * h) - 44.7
    print(f'Seu pesso ideia é {pi:.2f} Kg.')
else:
    print('Erro, verifique os dados informados')
