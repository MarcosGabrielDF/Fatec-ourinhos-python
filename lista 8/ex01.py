"""
1) Faça um script que leia o nome, o sexo e o estado civil de uma
pessoa. Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o
tempo de casada (anos).
"""

# Ler dados da pessoa
nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (M/F): ").upper()
estado_civil = input("Digite seu estado civil: ").upper()

# Verificar condição
if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Digite há quantos anos é casada: "))
    print(f"{nome} é casada há {tempo_casada} anos.")
else:
    print(f"Nome: {nome}")