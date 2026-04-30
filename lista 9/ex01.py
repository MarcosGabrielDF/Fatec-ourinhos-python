"""
1) Leia 5 números e mostra a soma entre eles;
"""

soma = 0
cont = 0
while cont < 5:
    valor = int(input("Digite um valor: "))
    soma += valor
    cont += 1

print(soma)
