"""
2) Escreva um script que leia três valores inteiros e diferentes e
mostre-os em ordem decrescente.
"""

# Ler três valores inteiros
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

# Colocar em ordem decrescente
valores = [n1, n2, n3]
valores.sort(reverse=True)

# Mostrar resultado
print("Valores em ordem decrescente:", valores)