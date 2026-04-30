"""
4) Mostre todos os números pares entre 1 e 100. E em seguida mostre a
sua soma;
"""

soma = 0
for i in range(2, 101, 2):
    soma += i
    print(i)

print(f'A soma de tudo fica: {soma}')
