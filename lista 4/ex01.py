"""
1. Ler duas notas reais, calcular a média e verificar se a pessoa está
APROVADA (média >= 6) ou REPROVADA, caso contrário;
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print(f"Sua média foi de {media:g}, você foi aprovado!")
else:
    print(f"Sua média foi de {media:g}, você foi Reprovado :(")