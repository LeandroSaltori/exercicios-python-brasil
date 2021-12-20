###########################
# EstruturaDeDecisao
###########################
"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

* Salários até R$ 280,00 (incluindo) : aumento de 20%
* Salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
* Salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
* Salários de R$ 1500,00 em diante : aumento de 5% 

Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
######################################

print('-='*30)
print(f'{"BEM VINDO A ORGANIZAÇÕES TABAJARA !!!" :^20}')
print('-='*30)
salario = float(input('Digite seu salário: '))
novo_salario = 0

if salario <= 280:
    aumento = (salario*20) / 100
    novo_salario = salario + aumento
    print (f'Seu salário era de R$ {salario:.2f}, teve um aumento de 20%, sendo o valor de R$ {aumento:.2f}. Seu novo salário será de R$ {novo_salario:.2f}')

if salario > 280 and salario <=700:
    aumento = (salario*15) / 100
    novo_salario = salario + aumento
    print (f'Seu salário era de R$ {salario:.2f}, teve um aumento de 15%, sendo o valor de R$ {aumento:.2f}. Seu novo salário será de R$ {novo_salario:.2f}')

if salario > 700 and salario <=1500:
    aumento = (salario*10) / 100
    novo_salario = salario + aumento
    print (f'Seu salário era de R$ {salario:.2f}, teve um aumento de 10%, sendo o valor de R$ {aumento:.2f}. Seu novo salário será de R$ {novo_salario:.2f}')

    
if salario > 1500:
    aumento = (salario*5) / 100
    novo_salario = salario + aumento
    print (f'Seu salário era de R$ {salario:.2f}, teve um aumento de 5%, sendo o valor de R$ {aumento:.2f}. Seu novo salário será de R$ {novo_salario:.2f}')



