"""
7. VERIFICAÇÃO DE HORA DE PICO NO TRÂNSITO
Peça a hora atual (em formato 24h).
• Se for entre 7 e 9 ou entre 17 e 19, mostre "Hora de pico".
• Caso contrário, "Trânsito tranquilo".
"""

#Captação
hora = int(input("Qual a hora é agora, sem os minutos? "))

if hora >= 7 and hora <= 9 or hora >= 17 and hora <= 19:
    print("Hora de pico")
else:
    print("Hora tranquilo")
