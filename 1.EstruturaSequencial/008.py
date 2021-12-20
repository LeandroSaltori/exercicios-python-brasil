###########################
# EstruturaSequencial
###########################
"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

valor_hora = float(input('Quanto você recebe por hora trabalhada? '))
hora = float(input('Quantas horas por mês você trabalha? '))
salario = valor_hora * hora
print(f'Seu salário é de: R$ {salario:.2f}')
