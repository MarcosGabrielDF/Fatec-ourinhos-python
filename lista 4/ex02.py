"""
2. Ler um número inteiro e verificar se é PAR ou ÍMPAR;
"""

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é impar')