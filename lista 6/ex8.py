"""
8. SISTEMA DE EMPRÉSTIMO BANCÁRIO
Solicite a renda mensal e o valor da parcela desejada.
• Se a parcela for maior que 30% da renda, mostre "Empréstimo negado".
• Se a renda for maior que 5000 ou a parcela for menor que 1000, mostre "Empréstimo aprovado".
• Caso contrário, "Em análise".
"""

#Captação
renda_mensal = float(input("Informe o valor da renda mensal: "))
parcela = int(input("Informe o valor da parcela: "))

#Conta
renda_parcela = parcela / renda_mensal
Quanti_de_parcelas = renda_mensal / parcela

if renda_parcela > 0.30:
    print("Empréstimo negado")
elif renda_parcela > 5000 or parcela < 1000:
    print("Empréstimo aprovado")
    print(f"Vai ter {Quanti_de_parcelas: g} parcelas")
else:
    print('Em análise')
