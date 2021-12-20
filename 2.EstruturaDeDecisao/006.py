###########################
# EstruturaDeDecisao
###########################
"""
Faça um Programa que leia três números e mostre o maior deles.
"""

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))

if n1 > n2 and n1 > n3:
    print(f'O maior número digitado é o primeiro numero, sendo {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número digitado é o segundo numero, sendo {n2}')
else:
    print(f'O maior número digitado é o terceiro numero, sendo {n3}')
