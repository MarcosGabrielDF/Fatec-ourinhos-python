"""
4) Faça um script que leia um nome de curso e verifique se tem Dados no nome do curso;
"""

curso = input('Digite o nome do curso: ')
curso = curso.lower().split()

if 'dados' in curso:
    print(f'A palavra dados está no seu curso.')
else:
    print('A palavra dados não está no seu curso.')
