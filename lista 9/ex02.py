"""
2) Leia 10 números e mostre quantos são pares e quantos são ímpares;
"""

par = 0
impar = 0

for i in range(10):
    n = int(input('numero: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Par: {par}')
print(f'impar: {impar}')
