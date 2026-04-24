"""
10. VERIFICADOR DE CLIMA PARA VIAGEM
Solicite a temperatura e se está chovendo (sim ou não).
• Se estiver acima de 25 graus e não estiver chovendo, mostre "Dia perfeito para viajar!".
• Se estiver abaixo de 15 graus ou chovendo, mostre "Melhor ficar em casa".
• Caso contrário, "Talvez dê para viajar".
"""

print("VERIFICADOR DE CLIMA PARA VIAGEM")

print(
'''Está chovendo?
[S]: Sim
[N]: Não''')

# Captação
chuva = input("").lower()
temperatura = float(input("Qual a temperatura? "))

# Condicional
if temperatura > 25 and chuva == "n":
    print("Dia perfeito para viajar!")

elif temperatura < 15 or chuva == "s":
    print("Melhor ficar em casa")

else:
    print("Talvez dê para viajar")