###########################
# EstruturaDeDecisao
###########################
"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

Primeiro = float(input('Digite o preço do primeiro produto: '))
Segundo = float(input('Digite o preço do segundo produto: '))
Terceiro = float(input('Digite o preço do terceiro produto: ')) 

barato = Primeiro

if Segundo < barato:
    barato = Segundo
    print('Você deve comprar o SEGUNDO produto!')
if Terceiro < barato:
    barato = Terceiro
    print('Você deve comprar o TERCEIRO produto!')
else:
    print('Voce deve comprar o PRIMEIRO produto!')