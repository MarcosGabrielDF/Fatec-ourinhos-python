"""
6) Faça um script que leia uma variável inteira e some 5, caso seja par ou some 8,
caso seja ímpar, imprimir o resultado desta operação.
"""

# Ler número inteiro
numero = int(input("Digite um número inteiro: "))

# Verificar se é par ou ímpar
if numero % 2 == 0:
    resultado = numero + 5
else:
    resultado = numero + 8

# Mostrar resultado
print("Resultado:", resultado)
