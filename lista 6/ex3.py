"""
3. AVALIAÇÃO DE DESEMPENHO ESCOLAR
Receba duas notas de um aluno.
• Se a média for maior ou igual a 7, mostre "Aprovado".
• Se a média for maior ou igual a 5 e menor que 7, mostre "Recuperação".
• Caso contrário, mostre "Reprovado".
"""

#Captação dos dados
n1 = float(input("Digite sua nota do trabalho: "))
n2 = float(input("Digite sua nota da prova : "))

#Cálculo
media = (n1 + n2)/ 2

#Condicional e impreção do resultado.
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")