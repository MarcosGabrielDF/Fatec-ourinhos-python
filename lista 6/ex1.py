"""
1. VERIFICAÇÃO DE INGRESSO DE CINEMA
Peça a idade e o valor do ingresso pago por uma pessoa.
• Se a pessoa tiver menos de 12 anos ou mais de 60, e o ingresso for menor que 20 reais, exiba "Ingresso promocional válido".
• Caso contrário, mostre "Ingresso comum".
"""

#Entrada
idade = int(input("Informe a sua idade: "))
preco_ingreco = float(input("Informe o valor do ingresso: "))

#Processamento e saida.
if idade < 12 or idade > 60 and preco_ingreco < 20:
    print("Ingresso promocional válido")
else:
    print("Ingresso comum")