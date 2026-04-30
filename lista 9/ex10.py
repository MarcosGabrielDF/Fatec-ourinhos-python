"""
10) Leia a idade de 10 pessoas e mostre quantos são
menores de idade e quantos são maiores de idade e a média
de idades digitadas;
"""

lista_idade = []
for i in range(10):
    idade = int(input('Digite sua idade: '))
    lista_idade.append(idade)

lista_idade.sort()

lista_maior_idade = []
lista_menor_idade = []
for i in lista_idade:
    if i >= 18:
        lista_maior_idade.append(i)
    elif i < 18:
        lista_menor_idade.append(i)

print('')
print(lista_maior_idade)
print(f'Tem um total de {len(lista_maior_idade)} pessoas que são maiores de idade.')
print('')
print(lista_menor_idade)
print(f'Tem um total de {len(lista_menor_idade)} pessoas que são menores de idade.')
print('')
print(f'A média é de {sum(lista_idade)/10}')
