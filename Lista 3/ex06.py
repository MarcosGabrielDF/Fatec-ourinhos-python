"""
6) Faça um script que leia o nome completo de uma pessoa e exiba o primeiro e o último nome somente.
"""

nome = input('Digite seu nome completo: ')
nome = nome.title()
nome_lista = nome.split()

nome_primeiro = nome_lista[0]
nome_ultimo = nome_lista[-1]

print(f"O seu nome é {nome}")
print(f"O seu primeiro nome é {nome_primeiro}")
print(f"O seu ultimo nome é {nome_ultimo}")
