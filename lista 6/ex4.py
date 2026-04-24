"""
4. CONTROLE DE TEMPERATURA CORPORAL
Peça a temperatura corporal de uma pessoa.
• Se a temperatura for menor que 35 ou maior que 39, exiba "Procure um médico imediatamente!".
• Se estiver entre 37 e 38.9, mostre "Febre".
• Caso contrário, "Temperatura normal".
"""

#Captação
temperatura =  float(input("Informe a temperatura do seu corpo? "))

#Condicional
if temperatura < 35 or temperatura > 39:
    print('Procure um médico imediatamente!')
elif temperatura >= 37 and temperatura <= 38.9:
    print('Febre')
else:
    print('Temperatura normal')
