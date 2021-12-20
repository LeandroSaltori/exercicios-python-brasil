###########################
# EstruturaSequencial
###########################
"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

valor_hora = float(input('Digite quanto você ganhar por hora: '))
hora = float(input('Digita quantas horas trabalhadas: '))
bruto = valor_hora*hora
desconto_ir = - bruto - (bruto * 0.11)
desconto_inss = bruto - (bruto * 0.8)
desconto_sind = bruto - (bruto * 0.5)
salario_liq = bruto - (desconto_ir + desconto_inss + desconto_sind)

print(f'Salário Bruto ................... (+) R$ {bruto:.2f}')
print(f'Desconto IR -11% ................ (-) R$ {bruto * 0.11:.2f}')
print(f'Desconto INSS -8% ............... (-) R$ {bruto * 0.08:.2f}')
print(f'Desconto Sindicato -5% .......... (-) R$ {bruto * 0.05:.2f}')
print(f'Salário Liquido ................. (+) R$ {salario_liq:.2f}')