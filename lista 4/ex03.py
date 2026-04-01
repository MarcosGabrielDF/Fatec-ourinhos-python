"""
3. Ler um número e verificar se é POSITIVO ou NEGATIVO. Suponha
que nunca irá digitar zero (0);
"""

numero = int(input('Digite um número: '))

if numero > 0:
    print('Esse numero é positivo')
elif numero < 0:
    print('Esse numero é negativo')
