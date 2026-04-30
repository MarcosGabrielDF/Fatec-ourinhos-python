"""
5. Faça um script que leia 3 números reais e verifique se eles
formam um triângulo. Para ser um triângulo, um dos seus lados (a,
b ou c) devem ser menores que as soma dos outros dois.
"""

# Ler três números reais
a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

# Verificar se forma triângulo
if a < b + c and b < a + c and c < a + b:
    print("Os valores formam um triângulo.")
else:
    print("Os valores NÃO formam um triângulo.")