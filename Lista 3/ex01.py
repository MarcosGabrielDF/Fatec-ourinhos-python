"""
1) Faça um script que leia seu nome completo e exiba: todo em maiúsculo, todo em minúsculo, a
quantidade de letras que ele possui (sem os espaços em branco) e somente seu primeiro nome e sua
quantidade de letras;
"""

nome = input("Digite seu nome completo: ")

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
nome_quantidade_letras = len(nome.replace(' ', ''))
nome_primeiro = nome.split()[0]
nome_primerio_quantidade_letras = len(nome_primeiro.replace(' ', ''))

print(f"""
O seu nome é maiusculas é: {nome_maiusculo}.
O seu nome em Minusculas é:{nome_minusculo}.
Esse nome tem {nome_quantidade_letras} letras.
O seu primerio nome é: {nome_primeiro}.
E seu primeiro nome tem {nome_primerio_quantidade_letras} letras.
""")
