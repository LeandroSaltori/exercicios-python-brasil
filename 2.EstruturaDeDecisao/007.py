###########################
# EstruturaDeDecisao
###########################
"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

# Resolução do exercicio com IF:

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))

maior = menor = n1

#Verificando o maior
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print(f'O MAIOR número é {maior}')
#Verificando o menor
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f'O MENOR número é {menor}')


##################################

# Resolução do exercicio com lista:

# numero = list()

# numero.append(float(input('Digite um número: ')))
# numero.append(float(input('Digite outro número: ')))
# numero.append(float(input('Digite mais um número: ')))
# print('*'*30)
# print(f'O MAIOR número digitado foi {max(numero)} \nO MENOR número digitado foi {min(numero)}')

