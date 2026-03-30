"""
5) Faça um script que leia um nome (desconsidere acentos) e verifique quantas vezes aparece a letra A, qual
a primeira posição que a letra A aparece e qual a última posição também;
"""

import unicodedata

#Tranforma em maiuscula.
nome = input('Digite seu nome: ')
nome_maiuscula = nome.upper()

#Retira os acentos
sem_acentos = unicodedata.normalize('NFD', nome_maiuscula)
sem_acentos = ''.join(c for c in sem_acentos if unicodedata.category(c) != 'Mn')

#Pega a quantidade de A.
nome_quantidade = sem_acentos.count('A')

print(f"O seu nome tem {nome_quantidade} A")

#Pegar posição do primerio e ultimo A.

nome_primeira_posicao = nome_maiuscula.find('A')
print(f"O primerio A está na possição: {nome_primeira_posicao}")

nome_ultima_posicao = nome_maiuscula.rfind('A')
print(f"O ultimo A está na possição: {nome_ultima_posicao}")



