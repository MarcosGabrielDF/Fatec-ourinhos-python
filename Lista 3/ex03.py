"""
3) Faça um script que leia uma frase qualquer e verifique se ela começa com Ciências;
"""

frase = input('Digite uma frase: ')
lista = frase.lower().split()

if lista[0] == 'ciência':
    print('Correto')
else:
    print('Incorreto')
