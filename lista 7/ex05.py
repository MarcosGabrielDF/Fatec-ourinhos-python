"""
5) Faça um script que leia a média de duas avaliações (P1 e P2). Calcule e mostre a
média final do aluno. Calcule e mostre se o aluno foi APROVADO ou REPROVADO,
sabendo que a média para aprovação deve ser maior ou igual a 7.
"""

# Ler notas
p1 = float(input("Digite a nota da P1: "))
p2 = float(input("Digite a nota da P2: "))

# Calcular média
media = (p1 + p2) / 2

# Mostrar média
print(f"Média final: {media:.2f}")

# Verificar situação
if media >= 7:
    print("Aluno APROVADO")
else:
    print("Aluno REPROVADO")
