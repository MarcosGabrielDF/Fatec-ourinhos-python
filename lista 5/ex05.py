"""
5) Faça um programa em Python que leia a média de duas
avaliações (P1 e P2). Calcule e mostre a média final do aluno.
Calcule e mostre se o aluno foi APROVADO ou REPROVADO,
sabendo que a média para aprovação deve ser maior ou igual a 7.
"""

p1 = float(input('Digite a mota da 1° avaliação: '))
p2 = float(input('Digite a mota da 2° avaliação: '))

media = (p1 + p2) / 2

if media > 7:
    print(f'A sua média é {media:g}, você foi APROVADO!')
else:
    print(f'A sua média é {media:g}, você foi REPROVADO!')