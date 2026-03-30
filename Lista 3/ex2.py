"""
2) Faça um script que leia um número de 4 dígitos e informe a quantidade de milhar, centena, dezena e
unidade;
"""
from os.path import join

numero = input('Escreva um número de 4 digítos: ')

if len(numero) != 4:
    print('Erro.')
else:
    print(f'Milhar: {numero[0]}')
    print(f'Centena: {numero[1]}')
    print(f'Dezena: {numero[2]}')
    print(f'Unidade: {numero[3]}')
