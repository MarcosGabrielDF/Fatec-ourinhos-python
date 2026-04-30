"""

3) O IMC – Indice de Massa Corporal é um critério da Organização
Mundial de Saúde para dar uma indicação sobre a condição de
peso de uma pessoa adulta. A fórmula é IMC = peso / ( altura )2
Elabore um script que leia o peso e a altura de um adulto e mostre
sua condição de acordo com a tabela abaixo.

IMC em adultos Condição
Abaixo de 18,5 Abaixo do peso
Entre 18,5 e 25 (18,5 <= imc <= 25) Peso normal
Entre 25 e 30 (25 < imc < 30) Acima do peso
Acima de 30 Obeso

"""

# Ler peso e altura
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Calcular IMC
imc = peso / (altura ** 2)

# Mostrar IMC
print(f"Seu IMC é {imc:.2f}")

# Verificar condição
if imc < 18.5:
    print("Condição: Abaixo do peso")
elif 18.5 <= imc <= 25:
    print("Condição: Peso normal")
elif 25 < imc < 30:
    print("Condição: Acima do peso")
else:
    print("Condição: Obeso")