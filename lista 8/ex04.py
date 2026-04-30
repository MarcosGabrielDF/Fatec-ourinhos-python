"""

4) Escreva um script que leia o número de identificação, as 3 notas
obtidas por um aluno nas 3 verificações e a média dos exercícios
que fazem parte da avaliação, e calcule a média de aproveitamento,
usando a fórmula:
MA = (nota1 + nota 2 * 2 + nota 3 * 3 + ME)/7

A atribuição dos conceitos obedece a tabela abaixo. O script deve
escrever o número do aluno, suas notas, a média dos exercícios, a
média de aproveitamento, o conceito correspondente e a

mensagem 'Aprovado' se o conceito for A, B ou C, e 'Reprovado' se
o conceito for D ou E.

Média de aproveitamento Conceito
>= 90 A
>= 75 e < 90 B
>= 60 e < 75 C
>= 40 e < 60 D
< 40 E

"""

# Ler dados do aluno
numero = input("Digite o número do aluno: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
me = float(input("Digite a média dos exercícios: "))

# Calcular média de aproveitamento
ma = (nota1 +(nota2 * 2) +(nota3 * 3) + me) / 7

# Verificar conceito
if ma >= 90:
    conceito = "A"
elif ma >= 75:
    conceito = "B"
elif ma >= 60:
    conceito = "C"
elif ma >= 40:
    conceito = "D"
else:
    conceito = "E"

# Verificar situação
if conceito in ["A", "B", "C"]:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

# Mostrar resultados
print("\n===== RESULTADO =====")
print("Número do aluno:", numero)
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Média dos exercícios:", me)
print(f"Média de aproveitamento: {ma:.2f}")
print("Conceito:", conceito)
print("Situação:", situacao)
