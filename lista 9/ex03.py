"""
3) Leia 10 números e mostre quantos são positivos, quantos são
negativos e quantos são neutros;
"""

neutro = 0
positivo = 0
negativo = 0

for i in range (10):
    n = int(input('numero: '))
    if n > 0:
        positivo += 1
    elif n < 0:
        negativo += 1
    else:
        neutro += 1

print(positivo)
print(negativo)
print(neutro)
