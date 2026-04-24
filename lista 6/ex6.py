"""
6. CADASTRO PARA DOAÇÃO DE SANGUE
Solicite a idade e o peso de uma pessoa.
• Se a idade for entre 18 e 69 e o peso for maior ou igual a 50 kg, mostre "Apto para doar sangue".
• Caso contrário, "Não apto para doação".
"""


#Captação
idade = int(input('Digite sua idade: '))
peso = float(input('Digite o seu peso: '))

#COndicional
if idade >= 18 and idade <= 69 and peso > 50:
    print("Apto para doar sangue")
else:
    print("Não apto para doar sangue")

