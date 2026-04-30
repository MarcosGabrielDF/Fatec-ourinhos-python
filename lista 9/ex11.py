"""
11) Ler um número inteiro e verificar se ele é PRIMO ou NÃO PRIMO;
"""

numero = int(input("Digite um número: "))
divisores = 0

# Vamos contar quantos divisores o número tem no intervalo de 1 até ele mesmo
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

# Verificação final
if divisores == 2:
    print(f"O número {numero} é PRIMO.")
else:
    print(f"O número {numero} NÃO É PRIMO.")
