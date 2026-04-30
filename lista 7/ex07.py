"""
7) Elabore um script que calcule o que deve ser pago por um produto, considerando
o preço normal de etiqueta e a escolha da condição de pagamento. Utilize os
códigos da tabela a seguir para ler qual a condição de pagamento escolhida e
efetuar o cálculo adequado.

Código Condição de pagamento
1 À vista em dinheiro ou cheque, recebe 10% de desconto
2 À vista no cartão de crédito, recebe 15% de desconto
3 Em duas vezes, preço normal de etiqueta sem juros
4 Em três vezes, preço normal de etiqueta mais juros de 10%
"""

print(
"""====Tipos de pagamentos====
[1] À vista em dinheiro ou cheque, recebe 10% de desconto
[2] À vista no cartão de crédito, recebe 15% de desconto
[3] Em duas vezes, preço normal de etiqueta sem juros
[4] Em três vezes, preço normal de etiqueta mais juros de 10%""")

pagamento = int(input("Digite o número da forma de pagamento: "))

preco = float(input('Preço do produto: '))

if pagamento == 1:
    preco_final = preco - (preco * 0.10)
    print(f'O preço do produto é {preco_final}')
elif pagamento == 2:
    preco_final = preco - (preco * 0.15)
    print(f'O preço do produto é {preco_final}')
elif pagamento == 3:
    preco_final = preco / 2
    print(f'O preço cheio é {preco}, mas dividido em 2 vezes fica {preco_final}')
elif pagamento == 4:
    preco_juros = (preco * 0.10) + preco
    preco_final = preco_juros / 3
    print(
        f"O preço original é R$ {preco:.2f}, com acréscimo de 10% de juros (R$ {preco * 0.10:.2f}), totalizando R$ {preco_juros:.2f}, dividido em 3x de R$ {preco_final:.2f}.")
