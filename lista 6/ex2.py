"""
2. SISTEMA DE LOGIN SIMPLES
Solicite um nome de usuário e uma senha.
• Se o nome for "admin" e a senha for "1234", mostre "Acesso concedido".
• Se o nome estiver certo, mas a senha errada, mostre "Senha incorreta".
• Caso contrário, exiba "Usuário não encontrado".
"""

#Captar informações
nome = input("Informe seu nome: ")
senha = input("Informe seu senha: ")

#Ajustar dados
nome  = nome.lower()

#Verificar informações
if nome == 'admin' and senha == '1234':
    print("Acesso concedido")
elif nome == 'admin' and senha != '1234':
    print("Senha incorreta")
else:
    print("Usuśrio não encontrado")
