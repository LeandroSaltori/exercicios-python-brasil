###########################
# EstruturaDeDecisao
###########################
"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

semana = ['','Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado',]

num = int(input(('Digite um numero entre 1 a 7: ')))

if num in range(1,8):
    print(f'{semana[num]}')
 
else:
    print('Número inválido!')

##############################################

#Resolução com IF

num = int(input(('Digite um numero entre 1 a 7: ')))

if num == 1:
    print('Domingo')
elif num == 2:
    print('Segunda')
elif num == 3:
    print('Terça')
elif num == 4:
    print('Quarta')
elif num == 5:
    print('Quinta')
elif num == 6:
    print('Sexta')
elif num == 7:
    print('Sádabo')
else:
    print('Número Inválido.')


