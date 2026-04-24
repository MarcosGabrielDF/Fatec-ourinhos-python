"""
9. CONTROLE DE ENTRADA EM FESTA
Peça a idade e se a pessoa está com convite (sim ou não).
• Se tiver 18 anos ou mais e tiver convite, mostre "Entrada permitida".
• Se for menor de idade e tiver convite, mostre "Entrada com responsável".
• Caso contrário, "Entrada negada".
"""

print("CONTROLE DE ENTRADA EM FESTA")

print(
'''Voê tem convite?
[S]: Sim
[N]: Não''')

#Captação
convite = input("").lower()
idade = int(input("Qual a sua idade? "))

#Condicional
if convite == "s" and idade >= 18:
    print('Entrada permitida')
elif convite == "s" or idade > 18:
    print("Entarda com responsável")
else:
    print("Entrada negada")
