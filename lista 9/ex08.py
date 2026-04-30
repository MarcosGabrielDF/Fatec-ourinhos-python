"""
8) Leia 10 números e mostre o maior e menor número
digitado;
"""

lista_numeros = []
for i in range(10):
    numero = int(input('Número: '))
    lista_numeros.append(numero)

lista_numeros.sort()

primeiro = lista_numeros[0]
ultimo = lista_numeros[-1]

print(f'O menor é {primeiro} e o maior é {ultimo}')
